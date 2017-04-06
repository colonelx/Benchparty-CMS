from django.http import HttpResponse, Http404, JsonResponse
from django.template.loader import render_to_string
from django import template

# Create your views here.
def page(request, slug='home'):
    try:
        content = render_to_string(slug + '.html')
        return JsonResponse({ 'slug': slug, 'content': content})
    except template.TemplateDoesNotExist:
        raise Http404