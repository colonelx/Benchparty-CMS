from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^categories', views.categories),
    url(r'^category/(?P<slug>\w+)', views.category),
    url(r'', views.index ),
]
