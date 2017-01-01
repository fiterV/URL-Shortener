from django.conf.urls import url, include
from django.contrib import admin
from shortener import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
    url(r'^(?P<code>[\w-]+)/', views.KirrCBView.as_view()),


]
