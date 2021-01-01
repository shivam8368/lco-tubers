from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.
class YTadmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'channel_name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type', 'channel_name')
    list_display_links = ('name', 'channel_name')
    list_editable = ('is_featured' ,)
    list_filter = ('city', 'camera_type')

admin.site.register(Youtuber, YTadmin)