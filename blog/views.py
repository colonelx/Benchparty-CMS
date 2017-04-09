from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    data = serializers.serialize("json", posts)
    return HttpResponse(data);

def categories(requst):
    return HttpResponse('Not Implemented');

def category(requst):
    return HttpResponse('Not Implemented');