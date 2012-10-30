#This is the local API 
import api
from rpc4django import rpcmethod

#@rpcmethod(name='blogalog.list_entries', signature=['array'], login_required=True)i
@rpcmethod(name='blogalog.list_entries', login_required=True)
def list_entries():
    return list(api.list_entries())

@rpcmethod(name='blogalog.list_files', login_required=True)
def list_files():
    return list(api.list_files())

@rpcmethod(name='blogalog.update_entry', permission='blogalog.change_entry')
def update_entry(pk=None, title=None, entry=None):
    if pk is None or title is None or entry is None:
        raise Exception('Invalid entry update request')
    return api.update_entry(pk, title, entry)
