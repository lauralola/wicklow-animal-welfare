from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import *
from .forms import DogForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


class DogList(generic.ListView):

    model = Dog
    queryset = Dog.objects.filter(status=1).order_by("-created_on")
    template_name = "homing.html"
    paginate_by = 12


class DogDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Dog.objects.filter(status=1)
        dog = get_object_or_404(queryset, slug=slug)
        comments = dog.comments.order_by("-created_on")
        liked = False
        if dog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "dog_detail.html",
            {
                "dog": dog,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Dog.objects.filter(status=1)
        dog = get_object_or_404(queryset, slug=slug)
        comments = dog.comments.order_by("-created_on")
        liked = False
        if dog.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.dog = dog
            messages.add_message(request,
                                 messages.INFO, 'Thank you for your comment!')
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "dog_detail.html",
            {
                "dog": dog,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

# View for liking a post


class DogLike(LoginRequiredMixin, View):

    """
    Like/Unlike dog
    """
    def post(self, request, slug, *args, **kwargs):

        dog = get_object_or_404(Dog, slug=slug)
        if dog.likes.filter(id=request.user.id).exists():
            dog.likes.remove(request.user)
            messages.success(request, 'You have unliked this post, thanks!')
        else:
            dog.likes.add(request.user)
            messages.success(request, 'You have liked this post, thanks!')
        return HttpResponseRedirect(reverse('dog_detail', args=[slug]))

# View for deleting logged in user comment


@login_required
def delete_comment(request, comment_id):

    """ Method to delete a comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Your comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'dog_detail', args=[comment.dog.slug]))

# View for editing logged in user comment


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Your comment was successfully updated'


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
            return redirect(reverse('homing'))
        else:
            messages.error(request, 'Failed to add dog. Please check form')
    else:
        form = DogForm()

    template = 'add_dog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_dog(request, dog_id):

    """ Edit a dog profile"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated dog!')
            return redirect(reverse('homing'))
        else:
            messages.error(request, 'Failed to update. Please check form')
    else:
        form = DogForm(instance=dog)
        messages.info(request, f'You are editing {dog.dog_name}')

    template = 'edit_dog.html'
    context = {
        'form': form,
        'dog': dog,
    }

    return render(request, template, context)


@login_required
def delete_dog(request, dog_id):

    """ Delete a dog profile """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    dog = get_object_or_404(Dog, pk=dog_id)
    dog.delete()
    messages.success(request, 'Dog deleted!')
    return redirect(reverse('homing'))
