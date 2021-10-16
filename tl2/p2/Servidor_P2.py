import datetime
import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        
        HoraServidor = datetime.datetime.now()
        
        return HoraServidor
    
# function used to initiate the Clock Server
def initiateClockServer():       
    # Clock Server Running forever
    while True: 
        
        daemon = Pyro4.Daemon()                # make a Pyro daemon
        ns = Pyro4.locateNS()                  # find the name server
        uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
        ns.register("Distribuidos2021", uri)   # register the object with a name in the name server

        
        print("Listo TP2 - P2 - Server.")
        daemon.requestLoop()                   # start the event loop of the server to wait for calls
  
  
# Driver function
if __name__ == '__main__':
  
    # Trigger the Clock Server    
    initiateClockServer()