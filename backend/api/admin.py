from django.contrib import admin

from .models import Quote, Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    # What you see in the list view
    list_display = ('author', 'text_preview', 'owner', 'created_at')
    # Filters on the right sidebar
    list_filter = ('owner', 'created_at', 'tags')
    # Search bar at the top
    search_fields = ('author', 'text')
    # Many-to-many UI improvement
    filter_horizontal = ('tags',)

    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
