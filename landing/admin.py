from django.contrib import admin
from landing import models

class PageContentInline(admin.StackedInline):
    model = models.PageContent
    extra = 0

class ButtonInline(admin.StackedInline):
    model = models.Button
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [ButtonInline, PageContentInline]

admin.site.register(models.Page, PageAdmin)
