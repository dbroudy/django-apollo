from django.contrib.sites.models import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json
from landing.models import Page, Button


def page(request, slug):
    page = get_object_or_404(Page, slug=slug, site=get_current_site(request))
    content = dict((c.key, c.content) for c in page.content.all())
    return render(request, page.template, {
        'content': content,
        'buttons': page.buttons.all(),
        'button_width': int(12 / page.buttons.count()),

    })

def register(request, button_id):
  button = Button.objects.get(id=button_id)
  button.clicks += 1
  button.save()

  return render(request, 'landing/confirm.html', {
      'button': button
    })

#  return HttpResponse(json.dumps({
#      'confirm': button.confirm,
#      'survey': render(request, 'landing/questions.html', {
#        'question': button.questions
#      }).content
#    }), content_type='applicaiton/json')

def questions(request):
  return HttpResponse(status=202)
