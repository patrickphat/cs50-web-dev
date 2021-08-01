from django.urls import path
from . import views

urlpatterns = [    
    path("", views.index, name="index"),
    path("hey_cutie_octopus/", views.hey_cutie_octopus, name="hey_cutie_octopus"),
    path("hey_patrick/", views.hey_patrick, name="hey_patrick"),
    path("coolest_page/", views.coolest_page, name="coolest_page"),
    path("<str:name>", views.greet, name="greet"),
]
