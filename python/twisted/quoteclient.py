from twisted.internet import protocol, reactor


class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.sendQuote()

    def sendQuote(self):
        self.transport.write(self.factory.quote)

    def dataReceived(self, data):
        print('Received Data: %s' %(data,))
        self.transport.loseConnection()


class QuoteClientFactory(protocol.ClientFactory):
    def __init__(self, quote):
        self.quote = quote

    def buildProtocol(self, addr):
        return QuoteProtocol(self)

    def clientConnectionFailed(self, connector, reason):
        print('connection failed:', reason.getErrorMessage())
        maybeStopReactor()

    def clientConnectionLost(self, connector, reason):
        print('connection lost:', reason.getErrorMessage())
        maybeStopReactor()


def maybeStopReactor():
    global quote_counter
    quote_counter -=1
    if not quote_counter:
        reactor.stop()


quotes = [
    "Hello India",
    "Hello Brazil",
    "Hello Spain"
]

quote_counter = len(quotes)
for quote in quotes:
    reactor.connectTCP('localhost', 8000, QuoteClientFactory(quote.encode()))
reactor.run()
