from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from landing import models

class AnswerInline(admin.TabularInline):
  model = models.Answer
  extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class PageContentInline(admin.StackedInline):
    model = models.PageContent
    extra = 0

class ButtonInline(admin.StackedInline):
    model = models.Button
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [PageContentInline, ButtonInline]

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Page, PageAdmin)
