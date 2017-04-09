from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.template.loader import render_to_string
from django import template

# Create your views here.
def page(request, slug='home'):
    if (slug == 'blog'):
        return HttpResponseRedirect('/blog/');

    try:
        content = render_to_string(slug + '.html')
        return JsonResponse({ 'slug': slug, 'content': content})
    except template.TemplateDoesNotExist:
        raise Http404