import ntplib
from datetime import datetime
import sys

class ClienteNTP:
    format = "%Y-%m-%d %H:%M:%S%f"
    def __init__(self, imputNtp):
        self.imputNtp = imputNtp

    def conexionNTP(self):
        clienteNTP = ntplib.NTPClient()
        print(f"Servidor NTP Ingresado: {self.imputNtp}")
        print("")
        for x in range(0, 8):
            var = clienteNTP.request(self.imputNtp, version=2)
            print("")
            print(" - - - - - - - -0- - - - - - - -")
            print(f"-              Muestra n°: {x+1}")
            print(f"- (T1) Tiempo original de la hora del sistema (Servidor): {datetime.fromtimestamp(var.orig_timestamp).strftime(ClienteNTP.format)}")
            print(f"- (T2) Recibir el timestamp en la hora del sistema (servidor): {datetime.fromtimestamp(var.recv_timestamp).strftime(ClienteNTP.format)}")
            print(f"- (T3) Transmitir marca de tiempo en la hora del sistema (servidor): {datetime.fromtimestamp(var.tx_timestamp).strftime(ClienteNTP.format)}")
            print(f"- (T4) Marca de tiempo de destino: {datetime.fromtimestamp(var.dest_timestamp).strftime(ClienteNTP.format)}")
            print(f"- Marca de tiempo de referencia en la hora del sistema: {datetime.fromtimestamp(var.ref_timestamp).strftime(ClienteNTP.format)}")
            print(f"- Retraso de ida y vuelta: {var.delay}")
            print(f"- Offset: {var.offset}")
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
                    #server_name = sys.argv[1]
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
            print("Opción Incorrectas")
        except KeyboardInterrupt:
            salir = True
            break
    
if __name__ == "__main__":
    programaPrincipal()