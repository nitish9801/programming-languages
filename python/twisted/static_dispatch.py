from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File

root = Resource()
root.putChild("foo", File("../../python/"))
root.putChild("bar", File("../../python/"))
root.putChild("baz", File("../../python/"))
# Getting no resource error.
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()