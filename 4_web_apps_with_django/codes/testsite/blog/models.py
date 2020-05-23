from django.db import models

# for date and time data types
from datetime import date

# to manage users on the site
from django.contrib.auth.models import User

from django.urls import (
    reverse,  # used to generate url by reversing the URL patterns
)


class Author(models.Model):
    """Model representing the author of blogs or comments"""

    # think of model submodules as columns of a table 
    # that store different data types

    # The ForeignKey provides a many-to-one relation
    # by adding a column to the local model to hold the remote value.
    # Here we are using it to store user data since each user is unique
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # The character field is good for short strings
    bio = models.CharField(
        max_length=200, help_text="Write a short bio of the author"
    )

    def get_absolute_url(self):
        """Returns the url to access a particular author instance"""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the model object"""
        return f"{self.name}"


class Blog(models.Model):
    """Model representing the blog posts or comments"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)

    # for date or time based data types 
    post_date = models.DateField(null=True, blank=True)

    # for longer text data types
    body = models.TextField()

    def get_absolute_url(self):
        """Returns the url to access a blog"""
        return reverse("blog-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title}"


class BlogComment(models.Model):
    """Model representing blog comments"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    post_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey("Blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.description}"
