from . import views
from django.urls import path

urlpatterns = [
    path("", views.DogList.as_view(), name="homing"),
    path('int:<slug:slug>/', views.DogDetail.as_view(), name='dog_detail'),
    path('add/', views.add_dog, name='add_dog'),
    path('edit/<int:dog_slug>/', views.edit_dog, name='edit_dog'),
]