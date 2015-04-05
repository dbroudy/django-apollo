from django import forms
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from landing.models import Survey, SurveyAnswer, Question, Answer

class SurveyAnswerForm(forms.ModelForm):
  survey = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput)
  question = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)
  answer = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)

  def __init__(self, *args, **kwargs):
    super(SurveyAnswerForm, self).__init__(*args, **kwargs)
    #if 'initial' in kwargs:
    #  question = kwargs['initial'].get('question', None)
    #  if not question:
    #    raise TypeError('\'question\' argument is required')

    self.fields['question'].queryset = Question.objects.filter(id=self.instance.question.id)
    self.fields['answer'].queryset = Answer.objects.filter(question=self.instance.question.id)

  class Meta:
    model = SurveyAnswer

SurveyAnswerFormSet = inlineformset_factory(
    Survey, SurveyAnswer,
    form=SurveyAnswerForm,
    extra = 0,
    can_delete = False
    )


#  button = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput)
#  answer = forms.ModelMultipleChoiceField(queryset=None, widget=forms.HiddenInput)
#
#  def __init__(self, *args, **kwargs):
#    super(QuestionForm, self).__init__(*args, **kwargs)
#    self.fields['button'].queryset = Button.objects.filter(pk=kwargs['button'].pk)
