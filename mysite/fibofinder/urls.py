from . import views
from django.conf.urls import include, url

urlpatterns =[
   url(r'^$', views.opening_page, name='opening_page')
]