from django.conf.urls import url
from . import views


# Basically this is the express router equivalent. It matches a url path with regular expressions and then calls 
# the view with a response object. 
# url(regex, view, kwargs, name)
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^menu/', views.menu, name='menu')
]

