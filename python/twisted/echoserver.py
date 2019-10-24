from twisted.internet import protocol, reactor


class CustomEchoServer(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class CustomEchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return CustomEchoServer()


reactor.listenTCP(8000, CustomEchoFactory())
reactor.run()