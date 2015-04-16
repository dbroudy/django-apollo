from django.contrib.sites.models import get_current_site
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
import json
import re
from apollo.models import Page, Button, Survey, SurveyAnswer, Answer
from apollo.forms import SurveyForm, SurveyAnswerFormSet

_content_idx = re.compile('^(.+)\[(\d+)\]$')

def page(request, slug):
    page = get_object_or_404(Page, slug=slug, site=get_current_site(request))
    content = dict()
    arrays = dict()
    for c in page.content.all():
      m = _content_idx.match(c.key)
      if m:
        base = m.group(1)
        idx = int(m.group(2))
        if not base in arrays:
          arrays[base] = list()

        l = len(arrays[base])
        if idx >= l:
          arrays[base] = arrays[base] + [''] * (idx-l+1)

        arrays[base][idx] = c.content
      else:
        content[c.key] = c.content
    for k,a in arrays.items():
      content[k] = a

    #content = dict((c.key, c.content) for c in page.content.all())
    return render(request, page.template, {
        'content': content,
        'buttons': page.buttons.all(),
        'button_width': int(12 / page.buttons.count()),

    })

def register(request, button_id):
  button = Button.objects.get(id=button_id)
  button.clicks += 1
  button.save()

  survey = Survey(button=button)
  survey.save()
  for q in button.questions.all():
    survey.answers.create(question=q)
  
  form = SurveyForm(instance=survey)
  formset = SurveyAnswerFormSet(instance=survey)

  return render(request, 'apollo/confirm.html', {
      'button': button,
      'surveyform': form,
      'answerform': formset
    })

def questions(request, survey_id):
  if request.method != 'POST':
    return HttpResponseNotAllowed(['POST'])
  survey = get_object_or_404(Survey, id=survey_id)

  form = SurveyForm(request.POST, instance=survey)
  if form.is_valid():
    form.save()

  formset = SurveyAnswerFormSet(request.POST, instance=survey)
  formset.save()

  if not form.is_valid() or not formset.is_valid():
    return render(request, 'apollo/forms.html', {
        'surveyform': form,
        'answerform': formset
      }, status=202)


  # return 200 when complete
  return HttpResponse(status=200)
