from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
BOOKED = ((0, "Available"), (1, "Booked"))
SEX = ((0, "Male"), (1, "Female"))
SIZE = ((0, "Small"), (1, "Medium"), (2, "Large"))

class Dog(models.Model):
    dog_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    about= models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    booked = models.IntegerField(choices=BOOKED, default=0)
    size = models.IntegerField(choices=SIZE, default=False)
    sex = models.IntegerField(choices=SEX, default=False)
    likes = models.ManyToManyField(
        User, related_name='dog_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,
                             related_name="comments")
    username = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

