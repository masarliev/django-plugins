'''
Created on Jan 19, 2011

@author: masarliev
'''
from django.template import loader
from django.template.context import Context
from django.http import HttpResponse
from zinnia.models import Entry
from tagging.models import TaggedItem
from stalwart.piecemaker.models import PiecemakerLatestEntriesPlugin
def render_xml(request, object_id):
    template_vars = {}
    #template_vars['slides'] = Slide.objects.all()
    #template_vars['transitions'] = Transition.objects.all()
    t = loader.get_template('piecemaker/cms/content.xml')
    c = Context(template_vars)
    entries = Entry.published.all()
    object = PiecemakerLatestEntriesPlugin.objects.get(pk=object_id)
    if object.categories.count():
        entries = entries.filter(categories__in=object.categories.all())
    if object.authors.count():
        entries = entries.filter(authors__in=object.authors.all())
    if object.tags.count():
        entries = TaggedItem.objects.get_union_by_model(
            entries, object.tags.all())

    entries = entries.distinct()[:object.number_of_entries]
    c.update({'entries': entries, 'object': object})
    return HttpResponse(t.render(c), mimetype="text/xml")