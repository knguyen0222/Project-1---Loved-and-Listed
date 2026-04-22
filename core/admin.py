from django.contrib import admin
from .models import Item, Tag, ItemTag

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'brand', 'category', 'condition', 'purchase_price', 'status', 'platform', 'sold_price']
    list_filter = ['category', 'condition', 'status', 'platform']
    search_fields = ['item_name', 'brand']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

@admin.register(ItemTag)
class ItemTagAdmin(admin.ModelAdmin):
    list_display = ['item', 'tag']