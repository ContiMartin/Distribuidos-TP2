import Pyro4
import time
import threading
from datetime import datetime, timedelta
from timeit import default_timer

HORA = 3600
MINUTO = 60 
SEGUNDO = 1

class hiloDelReloj(threading.Thread):
    def __init__(self, remote_object, horaCliente):
        self.horaServidor = remote_object
        self.horaCliente = horaCliente

    def algoritmoDeCristian(self):
        inicio = time.time()
        horaServidorFormat = self.horaServidor.dameHoraServidor()
        fin = time.time()
        offset = fin - inicio
                       
        format = "%Y-%m-%d %H:%M:%S:%f"
        horaServidor = datetime.strptime(horaServidorFormat, format)
        
        error = offset/2

        horaCalculada = horaServidor + timedelta(seconds = error)        
        return horaCalculada
        
    def iniciar(self):
        iteracion = 0
        aux = 0
        while True:
            iteracion = iteracion + 1
            inicioDeEjecucion = default_timer()
            if aux == 0:
                horaServidor = self.algoritmoDeCristian()
                dif = horaServidor - self.horaCliente
                dif = dif.total_seconds()
               

                if dif >= MINUTO:
                    deriva = -1
                elif dif >= (MINUTO/2):
                    deriva = -0.7
                elif dif >= SEGUNDO:
                    deriva = -0.5
                
                
                
                elif dif > -SEGUNDO and dif < SEGUNDO:
                    deriva = 0



                elif dif <= -MINUTO:
                    deriva = 12
                elif dif <= -(MINUTO/2):
                    deriva = 7
                elif dif <= -SEGUNDO:
                    deriva = 0.5
                else:
                    deriva = 10

                d = abs(dif) // 2000
                aux = d
            else:
                aux -= 1

            time.sleep(1 + deriva)
            self.horaCliente += timedelta(seconds = 1)
            finEjecucion = default_timer()
            total = timedelta(seconds = finEjecucion - inicioDeEjecucion)
            print(f"Hora Cliente: {self.horaCliente} | Diferencia: {dif} | Deriva: {deriva} | N°Iteracion: {iteracion} | Tiempo de ejecucion: {total}")


def programaPrincipal():
    # Variable para poder salir del while
    salir = False
    while not salir:
        horaServidor = Pyro4.Proxy("PYRONAME:Distribuidos2021")
        #horaLocalDesfasada = datetime(2021, 10, 1, 1, 1, 0)
        #horaLocalDesfasada = datetime(2022, 1, 1, 1, 1, 0)
        horaLocalDesfasada = datetime(2021, 10, 15, 10, 10, 0)
        hilo = hiloDelReloj(horaServidor, horaLocalDesfasada)    
        
        print(" - - - - - - - -0- - - - - - - -")
        print(" Menu - TP2 Sistemas Distribuidos 2021")
        print(" 1 - Ver Hora Servidor")
        print(" 2 - Ver Hora local (desfasada)")
        print(" 3 - ACTUALIZAR HORA ")
        print(" 4 - Salir")
        print(" - - - - - - - -0- - - - - - - -")
        # Opcion ingresada por consola
        camino = input()
        try:
            # Segun la opcion entra en un camino o el otro
            camino = str(camino)
            if camino == "1":
                horaServidorFormat = horaServidor.dameHoraServidor()
                format = "%Y-%m-%d %H:%M:%S:%f"
                horaServidorFormat = datetime.strptime(horaServidorFormat, format)
                print("")
                print(f"Hora del Servidor: {horaServidorFormat}")
                
            if camino == "2":
                print("")
                print(f"Hora del cliente: {horaLocalDesfasada}")

            if camino == "3":
                print("")
                print("INICIANDO")
                hilo.iniciar()
                break
            elif camino == "S":                
                print("")
                print("Saliendo")
                salir = True
                break

            else:
                print("Reimprimir MENU!")
        except ValueError:
            print("Opción Incorrectas")
        except KeyboardInterrupt:
            salir = True
            break

if __name__ == "__main__":
    programaPrincipal()