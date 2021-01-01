from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src={} width=40> '.format(object.photo.url))

    list_display = ('id','myphoto' ,'first_name', 'role', 'created_date')
    list_display_links = ('first_name', )
    search_fields = ('first_name', 'CEO')
    list_filter = ('role', )


class SliderAdmin(admin.ModelAdmin):

    def Slider_Image(self, object):
        return format_html('<img src={} width=80>'.format(object.photo.url))
    
    list_display = ('headline', 'Slider_Image', 'button_text')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
