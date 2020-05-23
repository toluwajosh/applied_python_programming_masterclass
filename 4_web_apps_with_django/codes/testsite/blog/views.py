from django.shortcuts import render

# Create your views here.
from blog.models import Author, Blog, BlogComment

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
