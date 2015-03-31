from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.db import models

class Question(models.Model):
  stem = models.CharField(max_length=100)

  def __unicode__(self):
    return "#%d: %s" % (self.pk, self.stem)

class Answer(models.Model):
  question = models.ForeignKey(Question, related_name='answers')
  label = models.CharField(max_length=100)

  def __unicode__(self):
    return "#%d" % (self.pk)


class Page(models.Model):
    site = models.ForeignKey(Site, related_name='landing_pages')
    slug = models.SlugField()
    template = models.CharField(max_length=255, choices=settings.LANDING_PAGE_TEMPLATES)

    class Meta:
        unique_together = ['site', 'slug']

    def __unicode__(self):
        return "%s (in %s)" % (self.slug, self.site)

    def get_absolute_url(self):
        return reverse('landing.views.page', args=[self.slug])

class PageContent(models.Model):
    page = models.ForeignKey(Page, related_name='content')
    key = models.SlugField()
    content = RichTextField()

    class Meta:
        unique_together = ['page', 'key']

    def __unicode__(self):
        return "%s" % (self.key)

class Button(models.Model):
    page = models.ForeignKey(Page, related_name='buttons')
    label = models.CharField(max_length=100)
    content = RichTextField()
    confirm = RichTextField()
    questions = models.ManyToManyField(Question, blank=True, related_name='+')
    clicks = models.IntegerField(editable=False)

    def __unicode__(self):
        return "#%d" % (self.pk)
