from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from models import Startup, Note, Filter, Collection, Profile

# Register your models here.

class StartupResource(resources.ModelResource):
    class Meta:
        model = Startup
        
        
class StartupAdmin(ImportExportModelAdmin):
    resource_class = StartupResource
    pass

class NoteAdmin(admin.ModelAdmin):
    raw_id_fields = ("startup",)
    
class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("following", "hidden",)

admin.site.register(Startup, StartupAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Filter)
admin.site.register(Collection)
admin.site.register(Profile, ProfileAdmin)