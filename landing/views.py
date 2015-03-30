from django.contrib.sites.models import get_current_site
from django.shortcuts import render, get_object_or_404
from landing.models import Page


def page(request, slug):
    page = get_object_or_404(Page, slug=slug, site=get_current_site(request))
    content = dict((c.key, c.content) for c in page.content.all())
    return render(request, page.template, {
        'content': content,
        'buttons': page.buttons.all(),
        'button_width': int(12 / page.buttons.count()),

    })