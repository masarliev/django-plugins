'''
Created on Jan 21, 2011

@author: masarliev
'''
from django.utils.translation import ugettext_lazy as _
class Channel(object) :
    def __init__(self) :
        self._messages = []
        self._callbacks = []

    def message(self, instance) :
        if instance.action_flag == 1:
            cssClass = 'add;ink'
        if instance.action_flag == 2:
            cssClass = 'changelink'
        if instance.action_flag == 3:
            cssClass = 'deletelink'
            
        if instance.content_type:
            cType = str(instance.content_type.name).capitalize()
        else:
            cType = 'Unknown'
        if instance.is_deletion:
            title = '%s <a href="#" class="%s"> &nbsp; %s</a>' % (cType, cssClass, instance.object_repr)
        else:   
            title = '<a href="%s" class="%s"> &nbsp; %s</a>' % (cType, instance.get_admin_url, cssClass, instance.object_repr)
        body = 'User <b>%s</b> <br /> %s' % (instance.user, instance.change_message)
        m = {'head': title, 'body':body, 'user_id': instance.user.id}
        for cb in self._callbacks :
            cb(m)
        self._callbacks = []

        self._messages.append(m)

    def query(self, cb, user_id) :
        self._callbacks.append(cb)

listener = Channel()