from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

# Shows directory listing of folder
resource = File('../../python')
print(resource)
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()