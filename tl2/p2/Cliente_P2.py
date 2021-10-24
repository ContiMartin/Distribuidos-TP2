import ntplib
from datetime import datetime
from datetime import timedelta
import sys

class ClienteNTP:
    format = '2021-%m-%d %H:%M:%S%f'
    
    def __init__(self, imputNtp):
        self.imputNtp = imputNtp
        
    def conexionNTP(self):
        clienteNTP = ntplib.NTPClient()
        print(f"Servidor NTP Ingresado: {self.imputNtp}")
        print("")
        for x in range(0, 8):
            var1 = clienteNTP.request(self.imputNtp, version=3)
            print(" - - - - - - - -0- - - - - - - -")
            print(f"-              Muestra n°: {x+1}")
            print(f"- (T1) Tiempo original de la hora del sistema (Servidor): {(datetime.fromtimestamp(var1.orig_timestamp).strftime(ClienteNTP.format))}")
            print(f"- (T2) Recibir el timestamp en la hora del sistema (servidor): {datetime.fromtimestamp(var1.recv_timestamp).strftime(ClienteNTP.format)}")
            print(f"- (T3) Transmitir marca de tiempo en la hora del sistema (servidor): {datetime.fromtimestamp(var1.tx_timestamp).strftime(ClienteNTP.format)}")
            print(f"- (T4) Marca de tiempo de destino: {datetime.fromtimestamp(var1.dest_timestamp).strftime(ClienteNTP.format)}")
            print(f"- Marca de tiempo de referencia en la hora del sistema: {datetime.fromtimestamp(var1.ref_timestamp).strftime(ClienteNTP.format)}")
            print(f"- Retraso de ida y vuelta: {var1.delay}")
            print(f"- Offset: {var1.offset}")
            print(" - - - - - - - -0- - - - - - - -")

def programaPrincipal():
    # Variable para poder salir del while
    salir = False
    while not salir: 
        print(" - - - - - - - -0- - - - - - - -")
        print(" Menu - TP2 Sistemas Distribuidos 2021")
        print(" 1 - Ingrese Servidor NTP")
        print(" 2 - Salir")
        print(" - - - - - - - -0- - - - - - - -")
        # Opcion ingresada por consola
        camino = input()
        try:
            # Segun la opcion entra en un camino o el otro
            camino = str(camino)
            if camino == "1":
                print("")
                try:
                    print(" - Esperando Servidor NTP..")
                    imputNtp = input()
                    clienteNTP = ClienteNTP(imputNtp)
                    clienteNTP.conexionNTP()
                except IndexError:
                    print("Debe ingresar la ip o nombre del servidor NTP")                
            if camino == "2":
                print("")
                print("Saliendo")
                salir = True
            else:
                print("Reimprimir MENU!")
        except ValueError:
            print("Opción Incorrecta!")
        except KeyboardInterrupt:
            salir = True
            break
    
if __name__ == "__main__":
    programaPrincipal()