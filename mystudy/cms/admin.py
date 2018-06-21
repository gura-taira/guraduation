from django.contrib import admin
from cms.models import Affair


class AffairAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'name', 'time', 'content',)
    list_display_links = ('id', 'name',)


admin.site.register(Affair, AffairAdmin)
