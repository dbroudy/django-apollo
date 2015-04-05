from django.contrib.sites.models import get_current_site
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
import json
from landing.models import Page, Button, Survey, SurveyAnswer, Answer
from landing.forms import SurveyAnswerFormSet

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

  survey = Survey(button=button)
  survey.save()
  for q in button.questions.all():
    survey.answers.create(question=q)
  
  formset = SurveyAnswerFormSet(instance=survey)

  return render(request, 'landing/confirm.html', {
      'button': button,
      'survey': survey,
      'answerform': formset
    })

#  return HttpResponse(json.dumps({
#      'confirm': button.confirm,
#      'survey': render(request, 'landing/questions.html', {
#        'question': button.questions
#      }).content
#    }), content_type='applicaiton/json')

def questions(request, survey_id):
  if request.method != 'POST':
    return HttpResponseNotAllowed(['POST'])
  survey = get_object_or_404(Survey, id=survey_id)

  formset = SurveyAnswerFormSet(request.POST, instance=survey)
  if not formset.is_valid():
    return HttpResponseBadRequest(json.dumps(formset.errors), content_type='application/json')

  formset.save()

  return HttpResponse(status=202)

  # return 200 when done
  #return HttpResponse(status=200)
