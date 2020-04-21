from django.contrib import admin
from application.models import theModel

class parkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'objectId', 'apiKey')

admin.site.register(theModel, parkingAdmin)
