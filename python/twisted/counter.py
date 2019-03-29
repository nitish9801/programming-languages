from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Counter(resource.Resource):
    isLeaf = True
    