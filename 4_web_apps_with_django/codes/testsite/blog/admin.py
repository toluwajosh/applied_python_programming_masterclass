from django.contrib import admin

# Register your models here.
from .models import Author, Blog, BlogComment

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogComment)