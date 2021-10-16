import Pyro4
from datetime import datetime


@Pyro4.expose
class HoraServidor(object):
    def dameHoraServidor(self):
        hora = datetime.now()
        horaServidorLocal = hora.strftime("%Y-%m-%d %H:%M:%S:%f")
        print("Hora local del Servidor: " + horaServidorLocal)
        return horaServidorLocal


daemon = Pyro4.Daemon()  # make a Pyro daemon
ns = Pyro4.locateNS()  # find the name server
uri = daemon.register(HoraServidor)  # register the greeting maker as a Pyro object
ns.register("Distribuidos2021", uri)  # register the object with a name in the name server
print("Distribuidos 2021.")
print("")
print("Servidor Listo")
daemon.requestLoop()  # start the event loop of the server to wait for calls
