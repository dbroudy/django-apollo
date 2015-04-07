from django import forms
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from landing.models import Survey, SurveyAnswer, Question, Answer

class SurveyForm(forms.ModelForm):
  class Meta:
    model = Survey
    exclude = ['button']

class SurveyAnswerForm(forms.ModelForm):
  survey = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput)
  answer = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)

  def __init__(self, *args, **kwargs):
    super(SurveyAnswerForm, self).__init__(*args, **kwargs)

    self.fields['answer'].queryset = Answer.objects.filter(question=self.instance.question.id)

  def question(self):
    return self.instance.question

  class Meta:
    model = SurveyAnswer
    exclude = ['question']

SurveyAnswerFormSet = inlineformset_factory(
    Survey, SurveyAnswer,
    form=SurveyAnswerForm,
    extra = 0,
    can_delete = False
    )

