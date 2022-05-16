from django.contrib import admin

from main.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_display_links = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')
    list_filter = ('name', 'description', 'price')


admin.site.register(Item, ItemAdmin)
