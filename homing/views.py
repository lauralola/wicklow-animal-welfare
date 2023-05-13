from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Dog
from .forms import DogForm

class DogList(generic.ListView):
    model = Dog
    queryset = Dog.objects.filter(status=1).order_by("-created_on")
    template_name = "homing.html"
    paginate_by = 12

class DogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Dog.objects.filter(status=1)
        dog = get_object_or_404(queryset, slug=slug)
        comments = dog.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if dog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "dog_detail.html",
            {
                "dog": dog,
                "comments": comments,
                "liked": liked
            },
        )

def add_dog(request):
    """ Add a dog to the page """
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added dog!')
            return redirect(reverse('add_dog'))
        else:
            messages.error(request, 'Failed to add dog. Please ensure the form is valid.')
    else:
        form = DogForm()
        
    template = 'add_dog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
