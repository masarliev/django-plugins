'''
Created on Jan 21, 2011

@author: masarliev
'''
from stalwart.livelog.decorator import asynchronous
from django.contrib.auth.decorators import login_required
from stalwart.livelog.listener import listener
@login_required
@asynchronous
def history_lp(request, handler):
    def on_new_message_async(message):
        if handler.request.connection.stream.closed():
            return
        handler.finish({'msg':message})
    listener.query(handler.async_callback(on_new_message_async), request.user.id)