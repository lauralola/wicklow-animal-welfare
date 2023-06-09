from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
BOOKED = (("Available", "Available"), ("Booked", "Booked"))
SEX = (("Male", "Male"), ("Female", "Female"))
SIZE = (("Small", "Small"), ("Medium", "Medium"), ("Large", "Large"))


class Dog(models.Model):

    dog_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    about = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    booked = models.CharField(max_length=200, choices=BOOKED,
                              default='Available')
    size = models.CharField(max_length=200, choices=SIZE, default=False)
    sex = models.CharField(max_length=200, choices=SEX, default=False)
    likes = models.ManyToManyField(
        User, related_name='dog_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.dog_name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,
                            related_name="comments")
    username = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('dog_detail', args=[self.dog.slug])
