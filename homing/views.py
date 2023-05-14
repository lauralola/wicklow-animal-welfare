from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
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

@login_required
def add_dog(request):
    """ Add a dog to the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added dog!')
            return redirect(reverse('dog_detail', args=[dog.id]))
        else:
            messages.error(request, 'Failed to add dog. Please ensure the form is valid.')
    else:
        form = DogForm()
        
    template = 'add_dog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_dog(request, dog_id):
    """ Edit a dog in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated dog!')
            return redirect(reverse('dog_detail', args=[dog.id]))
        else:
            messages.error(request, 'Failed to update dog. Please ensure the form is valid.')
    else:
        form = DogForm(instance=dog)
        messages.info(request, f'You are editing {dog.name}')

    template = 'edit_dog.html'
    context = {
        'form': form,
        'dog': dog,
    }

    return render(request, template, context)

@login_required
def delete_dog(request, dog_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    dog = get_object_or_404(Product, pk=dog_id)
    dog.delete()
    messages.success(request, 'Dog deleted!')
    return redirect(reverse('dogs'))