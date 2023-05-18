from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')

def our_story(request):
    """ A view to return the story page """

    return render(request, 'our_story.html')
