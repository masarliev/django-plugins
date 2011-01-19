'''
Created on Jan 19, 2011

@author: masarliev
'''
from django.db import models
from cms.models import CMSPlugin
from tagging.models import Tag
from django.contrib.auth.models import User
from zinnia.models import Entry
from zinnia.models import Category
from django.utils.translation import ugettext_lazy as _

class PiecemakerLatestEntriesPlugin(CMSPlugin):
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True, null=True)
    authors = models.ManyToManyField(User, verbose_name=_('authors'), blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), blank=True, null=True)
    
    number_of_entries = models.IntegerField(_('number of entries'), default=5)

    def __unicode__(self):
        return _('%s entries') % self.number_of_entries