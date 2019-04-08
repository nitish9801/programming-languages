from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource, NoResource

from calendar import calendar


class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = int(year)

    def render_GET(self, request):
        return str.encode("<html><body><pre>%s</pre><body><html>"%(calendar(self.year)))


class CalenderHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(name)
        else:
            return NoResource()

    def render_GET(self, request):
        return "<html><body>Welcome to the calendar server!</body></html>"


resource = CalenderHome()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()