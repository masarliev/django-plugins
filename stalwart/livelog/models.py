'''
Created on Jan 21, 2011

@author: masarliev
'''
from django.db.models.signals import pre_save
from django.contrib.admin.models import LogEntry
from stalwart.livehistory.listener import listener
def on_new_event(sender, instance, signal, *args, **kwargs):
    listener.message(instance)

pre_save.connect(on_new_event, LogEntry)