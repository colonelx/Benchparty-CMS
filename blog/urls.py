from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^menu-categories', views.menu_categories),
    url(r'^category/(?P<slug>[a-zA-Z0-9_-]+)', views.category),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)', views.post),
    url(r'', views.index ),
]
