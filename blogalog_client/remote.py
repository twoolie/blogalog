import xmlrpclib
from rpc4django.utils import CookieTransport

class xmlrpc:

    #How do we choose between the different transports avaliable?
    #We probably need a configuration of some kind somewhere, if we want to choose between
    #Cookie and remote transports later. 
    #### TODO - We need a better SSL transport!!!!
    #### How do we handle the server going away and coming back?
    def __init__(self, url,):
        self.proxy = xmlrpclib.ServerProxy("%s" % (url) , transport=CookieTransport())
        self.transaction = xmlrpclib.MultiCall(self.proxy)

