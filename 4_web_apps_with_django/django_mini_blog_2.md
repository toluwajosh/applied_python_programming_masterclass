# Django Mini Blog, Part 2

Now that we have created a working but simplistic home page, we can now add more pages to achieve its purpose. We need;

- A view to show all blogs - Blogs List.
- A view to show all authors - Authors List.
- A view to show each blog's detail - Blog Details.
- A view to show each author's detail - Author Details.

We can do this by using Django's generic class-based views which will also help to reduce the amount of code we have to write for common use cases. We'll also go into URL handling in greater detail, showing how to perform basic pattern matching.
We are using a generic view because it already implements most of the functionality we need and follows Django best-practice, we will be able to create a more robust list view with less code, less repetition and ultimately less maintenance.

> Check out [Built-in class-based generic views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/) (Django docs) for many more examples of what you can do.

## Add List Views

Open `blog/views.py`, and copy the following code into the bottom of the file:

```python
from django.views import generic

# This view queries the database to get all the records 
# for the specified model (Blog) then render a template located at 
# /testsite/blog/templates/blog/blog_list.html
class BlogListView(generic.ListView):
    model = Blog
    # set the maximum number of items on a page.
    paginate_by = 10

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

```

Now add the url paths in `blog/urls.py`. `views.BlogListView.as_view()` and `views.AuthorListView.as_view()` are the functions that will be called if a url matches. The `name` is an identifier for this mapping used in the template.

```python
urlpatterns = [
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("bloggers/", views.AuthorListView.as_view(), name="bloggers"),
]
```

The view function has a different format than before — that's because this view was implemented as a class and we are inheriting from an existing generic view function that already does most of what we want this view function to do, rather than writing our own from scratch. For Django class-based views we access an appropriate view function by calling the class method `as_view()`. This does all the work of creating an instance of the class, and making sure that the right handler methods are called for incoming HTTP requests.

## Create a base generic template

In most cases, some parts of our website will present the same information so we do not need to create a all-new template every time we are creating a view. We can create a base template and let other templates `extend` this `base_generic.html` template. So let us create a base generic template and update our `index.html` to use this base template.

> Template `tags` are functions that you can use in a template to loop through lists, perform conditional operations based on the value of a variable, and so on. In addition to template tags, the template syntax allows you to reference variables that are passed into the template from the view, and use template filters to format variables (for example, to convert a string to lower case).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  {% block title %}<title>Local Library</title>{% endblock %}
</head>
<body>
  {% block sidebar %}<!-- insert default navigation text for every page -->{% endblock %}
  {% block content %}<!-- default content text (typically empty) -->{% endblock %}
</body>
</html>
```

The code snippet below shows how to use the extends template tag and override the content block. The generated HTML will include the code and structure defined in the base template, including the default content you defined in the title block, but the new content block in place of the default one.


## Creating the List View template

## Conditional execution

## For loops

## Accessing Variables

## Creating the Detail View template