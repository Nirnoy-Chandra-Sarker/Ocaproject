from django.contrib import admin
from .models import *
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'advisor']

admin.site.register(Membership)
admin.site.register(Event)
admin.site.register(ClubInfo)
admin.site.register(Achievement)
admin.site.register(Sponsor)
admin.site.register(Room)
admin.site.register(Highlights)
admin.site.register(Budget)
admin.site.register(Transaction)