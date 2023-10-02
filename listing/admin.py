from django.contrib import admin
from .models import Properties

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "price", "list_date")
    list_display_links = ("name", "location")
    list_filter = ("agent_id",)
    search_fields = ("name", "location", "id")
    list_per_page = 25


admin.site.register(Properties, PropertyAdmin)