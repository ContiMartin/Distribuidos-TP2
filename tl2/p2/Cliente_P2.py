import datetime
from dateutil import parser
from timeit import default_timer as timer
import Pyro4




def synchronizeTime():
    print("")
    name = input("Un nombre por favor.. ").strip()
    greeting_maker = Pyro4.Proxy("PYRONAME:Distribuidos2021")    # use name server object lookup uri shortcut
    request_time = timer()
    HoraServidor = greeting_maker.get_fortune(name)
    
    response_time = timer() 
    
    HoraActual = datetime.datetime.now()
  
    print("")
    print("Hora que devolvio el Servidor: " + str(HoraServidor))
  
    print("")
    print("Hora actual del Cliente: "+ str(HoraActual))
  
    Offset = response_time - request_time
    
    print("")
    print("Offset: " \
          + str(Offset) \
          + " segundos")
  
    
    # synchronize process client clock time
    Client_time = HoraServidor + datetime.timedelta(seconds = (Offset) / 2)
  
    print("")
    print("Tiempo del cliente de proceso de sincronizado: " + str(Client_time))
  
    # calculate synchronization error 
    error = HoraActual + Client_time
    print("Error de sincronizacion: "+ str(error.total_seconds()) + " segundos.")
  
  
  
# Driver function
if __name__ == '__main__':
  
    # synchronize time using clock server
    synchronizeTime()