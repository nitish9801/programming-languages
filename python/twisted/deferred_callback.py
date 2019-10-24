from twisted.internet.defer import Deferred


def mycallback(result):
    print(result)
    return 'Hello from mycallback'

def mySecondCallback(result):
    print(result)


d = Deferred()
d.addCallback(mycallback)
d.addCallback(mySecondCallback)
d.callback("Started callback")