from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol


class QuoteServer(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1

    def dataReceived(self, data):
        print("Number of active connections: %d" % (
            self.factory.numConnections,))
        print(self.getQuote())
        self.transport.write(self.getQuote())
        self.updateQuote(data)

    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, quote):
        self.factory.quote = quote


class QuoteFactory(Factory):
    numConnections = 0

    def __init__(self):
        self.quote = 'Hello world'.encode()

    def buildProtocol(self,  addr):
        return QuoteServer(self)


reactor.listenTCP(8000, QuoteFactory())
reactor.run()

