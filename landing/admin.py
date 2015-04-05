from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from landing import models

class AnswerInline(admin.TabularInline):
  model = models.Answer
  extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(models.Question, QuestionAdmin)

class PageContentInline(admin.StackedInline):
    model = models.PageContent
    extra = 0

class ButtonInline(admin.StackedInline):
    model = models.Button
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline, ButtonInline]

admin.site.register(models.Page, PageAdmin)

class SurveyAnswerInline(admin.StackedInline):
  model = models.SurveyAnswer
  readonly_fields = ['question', 'answer']
  can_delete = False
  extra = 0

class SurveyAdmin(admin.ModelAdmin):
  readonly_fields = ['button']
  inlines = [SurveyAnswerInline]

admin.site.register(models.Survey, SurveyAdmin)
