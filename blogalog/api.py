from models import Entry, File

def list_entries():
    print('API list_entries')
    return Entry.objects.all()

def list_visible_entries():
    return Entry.objects.filter(visible=True)

def list_files():
    print('API list_files')
    return File.objects.all()

def update_entry(pk=None, title=None, entry=None):
    print('API update entry')
    entry = Entry.objects.get(pk=pk)
    ## title entry
    return True

