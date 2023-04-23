from . import views
from django.urls import path

urlpatterns = [
    path("", views.DogList.as_view(), name="home"),
    path('<slug:slug>/', views.DogDetail.as_view(), name='dog_detail'),
]