from django.shortcuts import render
from django.views import generic

# Create your views here.
from blog.models import Author, Blog, BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin # for class based views


def index(request):
    """View function for home page of site."""

    # For now, Let us just show the number of blogs
    # and number of authors on the home page.
    # This is how you generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        "num_blogs": num_blogs,
        "num_authors": num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


# This view queries the database to get all the records
# for the specified model (Blog) then render a template located at
# /testsite/blog/templates/blog/blog_list.html
class BlogListView(generic.ListView):
    model = Blog
    # set the maximum number of items on a page.


class AuthorListView(generic.ListView):
    model = Author


class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
