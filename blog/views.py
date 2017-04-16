from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
import datetime
import json
# Create your views here.
from blog.models import Post, Category


def index(request):
    posts = Post.objects.all()
    data = serializers.serialize("json", posts)
    return HttpResponse(data);

def menu_categories(requst):
    categories = Category.objects.filter(level=0)
    data = serializers.serialize("json", categories)
    return HttpResponse(data);

def post(request, slug):

    posts = Post.objects.filter(slug=slug)

    data = serializers.serialize("json", posts, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data);

def category(requst, slug):
    categories = Category.objects.filter(slug=slug);
    category=categories.first();
    posts = Post.objects.filter(categories__in=category.get_descendants(include_self=True))

    vm_model = {
        'category': category.name,
        'posts': list(posts.values())
    }

    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    return HttpResponse(
        json.dumps(vm_model, default=datetime_handler),
        content_type='application/javascript; charset=utf8'
    )


    #return HttpResponse(data);