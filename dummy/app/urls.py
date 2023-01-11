from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("section/<int:num>", views.section, name="section")
    ]
urlpatterns += staticfiles_urlpatterns()