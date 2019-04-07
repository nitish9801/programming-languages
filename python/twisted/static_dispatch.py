from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.resource import Resource


root = Resource()
root.putChild('', File('../../python'))
root.putChild("tt", File("../../python"))
# root.putChild('bb', File('../../python'))
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()