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

## Specify the database

At this stage, don't worry much about databases. This is typically where the information about our site is stored. So any time we make a request through our site, the information is retrieved from the database.

> A [database](https://www.oracle.com/database/what-is-database.html) is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.
> Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and querying data.

We'll use the SQLite database for this example, because we don't expect to require a lot of concurrent access on a demonstration database, and also because it requires no additional work to set up! You can see how this database is configured in settings.py (more information is also included below):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Because we are using SQLite, we don't need to do any further setup here. Let's move on!

## Set the url mapper

Hook up the URL mapper, inside the project `url.py` and app `url.py`.
To do this, create `url.py` file in the `blog` directory

