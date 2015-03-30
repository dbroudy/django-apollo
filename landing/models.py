from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from multisite.models import Alias


class Page(models.Model):
    site = models.ForeignKey(Site, related_name='landing_pages')
    slug = models.SlugField()
    template = models.CharField(max_length=255, choices=settings.LANDING_PAGE_TEMPLATES)

    class Meta:
        unique_together = ['site', 'slug']

    def __unicode__(self):
        return "%s (in %s)" % (self.slug, self.site)

    def get_absolute_url(self):
        return "/%s" % self.slug # TODO: Add site

class PageContent(models.Model):
    page = models.ForeignKey(Page, related_name='content')
    key = models.SlugField()
    content = RichTextField()

    class Meta:
        unique_together = ['page', 'key']

class Button(models.Model):
    page = models.ForeignKey(Page, related_name='buttons')
    label = models.CharField(max_length=100)
    content = RichTextField()

