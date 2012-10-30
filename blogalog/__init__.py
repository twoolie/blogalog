#This is the local API
from views import EntryListView 
from rpc4django import rpcmethod

#### I need to find a better way of dealing with this, so that perhaps the request
#### Or at least the request user can go to the View?
#### Or do I just do the permissions seperately?

#### Is using the view as an api really the best thing to do?

#@rpcmethod(name='blogalog.list_entries', signature=['array'], login_required=True)i
@rpcmethod(name='blogalog.list_entries', login_required=True)
def list_entries():
    return list(EntryListView().get_queryset())

#@rpcmethod(name='blogalog.list_files', login_required=True)
#def list_files():
#    return list(api.list_files())

@rpcmethod(name='blogalog.update_entry', permission='blogalog.change_entry')
def update_entry(pk=None, title=None, entry=None):
    if pk is None or title is None or entry is None:
        raise Exception('Invalid entry update request')
    #return api.update_entry(pk, title, entry)
    return True
