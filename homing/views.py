from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Dog

# def all_dogs(request):
#     """ A view to show all dogs, including sorting and search queries """

#     dogs = Dog.objects.all()
#     query = None
#     categories = None

#     if request.GET:
#         if 'category' in request.GET:
#             categories = request.GET['category'].split(',')
#             dogs = dogs.filter(category__name__in=categories)
#             categories = Category.objects.filter(name__in=categories)

#         if 'q' in request.GET:
#             query = request.GET['q']
#             if not query:
#                 messages.error(request, "You didn't enter any search criteria!")
#                 return redirect(reverse('products'))
            
#             queries = Q(name__icontains=query) | Q(description__icontains=query)
#             dogs = dogs.filter(queries)

#     context = {
#         'dogs': dogs,
#         'search_term': query,
#         'current_categories': categories,
#     }

#     return render(request, 'index.html', context)

class DogList(generic.ListView):
    model = Dog
    queryset = Dog.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
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