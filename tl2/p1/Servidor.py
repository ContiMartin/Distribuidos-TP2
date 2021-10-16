# 1. Implemente un servidor de hora empleando Python y llamadas a procedimientos
# remotos. Desarrollar un cliente que emule un reloj (utilizar hilos para la actualización del
# mismo) y que se sincronice dicho reloj con el servidor de hora implementado, utilizando
# el algoritmo de Cristian. Al utilizar la hora patrón, tome un grupo de valores (por ejemplo
# 5), eligiendo el que haya demandado menor tiempo de tránsito de los mensajes.


# saved as greeting-server.py
# Version 1
#import Pyro4

#@Pyro4.expose
#class GreetingMaker(object):
#    def get_fortune(self, name):
#        return "Hello, {0}. Here is your fortune message:\n" \
#               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)
#
#daemon = Pyro4.Daemon()                # make a Pyro daemon
#uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
#
#print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
#daemon.requestLoop()                   # start the event loop of the server to wait for calls

# Version 2
# saved as greeting-server.py
import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register("Distribuidos2021", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls