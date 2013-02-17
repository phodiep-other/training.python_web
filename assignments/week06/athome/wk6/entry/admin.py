from django.contrib import admin
from entry.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'text', 'published_today')
    list_filter = ('pub_date',)
    ordering = ('pub_date',)

admin.site.register(Entry, EntryAdmin)
