from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path("", views.DogList.as_view(), name="homing"),
    path('int:<slug:slug>/', views.DogDetail.as_view(), name='dog_detail'),
    path('like/<slug:slug>', views.DogLike.as_view(), name='dog_like'),
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('add/', views.add_dog, name='add_dog'),
    path('edit/<int:dog_id>/', views.edit_dog, name='edit_dog'),
    path('delete/<int:dog_id>/', views.delete_dog, name='delete_dog'),
]
