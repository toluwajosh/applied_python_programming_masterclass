# Introduction to Django Framework

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Django helps you write software that is; complete, versatile, secure, scalable, maintainable and portable.

## What does Django code look like

Django web applications typically group the code that handles each of these steps into separate files:

![django-codes](images/basic-django.png)


- **URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.
- **View:** A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.
- **Models:** Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database. 
- **Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

## Django Hello World



# Bibliography

1. MDN Web Docs, Django Web Framework - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
2. 