# Django Mini Blog

In this section, we are going to create a Mini Blog using the Djanog framework.
Our blog will have 3 main pages namely, 
- the Home page, 
- All Blogs page,
- All Bloggers page.

Users will also be able to create a profile and sign in to read blog details.

## Create application

In Django, a project is made up of applications. You can think of this as features added to a website. In our case, we will build a website with a blog application. For now, the blog application will be the only feature of the website. However, we can easily add new features by adding new apps. Each app work independently so this makes Django applications modular and portable.

We are going to create a blog app inside our `testsite`. To create an app, run:

```python
python3 manage.py startapp blog
```

Next, we will need to register the app in our project settings, located in `testsite/testsite/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # register our new app here
]
```

