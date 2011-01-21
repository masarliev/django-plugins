'''
Created on Jan 21, 2011

@author: masarliev
'''
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from stalwart.livehistory.views import history_lp
class LogAdmin(admin.ModelAdmin):
    list_display    = ('user', 'content_type','object_repr')
    def get_urls(self):
        from django.conf.urls.defaults import patterns, url
        urls = super(LogAdmin, self).get_urls()
        my_urls = patterns('',
            url(
                r'history',
                self.admin_site.admin_view(history_lp),
                name='admin_lp_history',
            ),
        )
        return my_urls + urls

admin.site.register(LogEntry, LogAdmin)