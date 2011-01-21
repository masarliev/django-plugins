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
        title = '<a href="%s">%s</a>' % (instance.get_admin_url, instance.object_repr)
        body = 'User <b>%s</b> <br /> %s' % (instance.user, instance.change_message)
        m = {'head': title, 'body':body, 'user_id': instance.user.id}
        for cb in self._callbacks :
            cb(m)
        self._callbacks = []

        self._messages.append(m)

    def query(self, cb, user_id) :
        self._callbacks.append(cb)

listener = Channel()