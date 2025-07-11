from django.urls import path, include
from . import views

urlpatterns = [
    path('home',views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
]
