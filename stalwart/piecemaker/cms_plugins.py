'''
Created on Jan 19, 2011

@author: masarliev
'''
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from stalwart.piecemaker.models import PiecemakerLatestEntriesPlugin
from zinnia.managers import authors_published
from zinnia.managers import tags_published
from zinnia.models import Entry
from tagging.models import TaggedItem
class PiecemakerZinniaPlugin(CMSPluginBase):
    module = _('Piecemaker')
    model = PiecemakerLatestEntriesPlugin
    name = _('Latest entries')
    render_template = 'piecemaker/cms/content.html'
    filter_horizontal = ['categories', 'authors', 'tags']
    text_enabled = True

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'authors':
            kwargs['queryset'] = authors_published()
        if db_field.name == 'tags':
            kwargs['queryset'] = tags_published()
        return super(PiecemakerZinniaPlugin, self).formfield_for_manytomany(
            db_field, request, **kwargs)

    def render(self, context, instance, placeholder):
        entries = Entry.published.all()

        if instance.categories.count():
            entries = entries.filter(categories__in=instance.categories.all())
        if instance.authors.count():
            entries = entries.filter(authors__in=instance.authors.all())
        if instance.tags.count():
            entries = TaggedItem.objects.get_union_by_model(
                entries, instance.tags.all())

        entries = entries.distinct()[:instance.number_of_entries]
        context.update({'entries': entries,
                        'object': instance,
                        'placeholder': placeholder})
        return context
plugin_pool.register_plugin(PiecemakerZinniaPlugin)