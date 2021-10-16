# 1. Implemente un servidor de hora empleando Python y llamadas a procedimientos
# remotos. Desarrollar un cliente que emule un reloj (utilizar hilos para la actualización del
# mismo) y que se sincronice dicho reloj con el servidor de hora implementado, utilizando
# el algoritmo de Cristian. Al utilizar la hora patrón, tome un grupo de valores (por ejemplo
# 5), eligiendo el que haya demandado menor tiempo de tránsito de los mensajes.


# Version 1
# saved as greeting-client.py
#import Pyro4

#uri = input("What is the Pyro uri of the greeting object? ").strip()
#name = input("What is your name? ").strip()

#greeting_maker = Pyro4.Proxy(uri)         # get a Pyro proxy to the greeting object
#print(greeting_maker.get_fortune(name))   # call method normally

# saved as greeting-client.py
import Pyro4

name = input("What is your name? ").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:Distribuidos2021")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))