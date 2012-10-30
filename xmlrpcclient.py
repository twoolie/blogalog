
from django.utils.datastructures import SortedDict
import xmlrpclib

from rpc4django.utils import CookieTransport

#username = 'testuser'
username = 'william'
password = '1'
hostname = 'localhost'
port = 8000
#proxy = xmlrpclib.ServerProxy("http://%s:%s@%s:%s/rpc" 5 (username, password, hostname, port), allow_none=False)
#proxy = xmlrpclib.ServerProxy("http://%s:%s/rpc" % (hostname, port), allow_none=False)

proxy = xmlrpclib.ServerProxy("http://%s:%s/rpc" % (hostname, port), transport=CookieTransport())

print('%s' % proxy.system.listMethods() )

print('%s' % proxy.system.login(username, password))

if proxy.system.login(username, password):
    print('%s' % proxy.blogalog.list_entries() )
    #print('%s' % proxy.blogalog.update_entry(1, 'Test', 'New text') )
    proxy.system.logout()

