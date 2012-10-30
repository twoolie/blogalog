from models import Entry, File
from django.contrib import admin


#class EntryAdmin(reversion.VersionAdmin):
#    pass
#
#admin.site.register(Entry, EntryAdmin)

class EntryAdmin(admin.ModelAdmin):
    pass

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(File, FileAdmin)
