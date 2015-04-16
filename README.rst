############################
django-apollo Documentation
############################

About
=====

The best way to prove an idea is to test it. Whether you want to test a new
feature in an existing application or prove an entirely new concept,
django-apollo helps you quickly add a landing page to your existing Django
site or create a new landing page based MVP site.

Usage
=====

Installation
------------

``pip install django-apollo``

Dependencies
------------

In addition to Django, the following python packages are required by this
package, and should be installed automatically by ``pip``:

* ``django-ckeditor >= 4.4``
* ``django-widget-tweaks >= 1.3``

Bootstrap 3 and jQuery are also required, but because there are so many ways to
add these to your project, they have not been made dependencies. 

Settings
--------

* Add 'apollo' to your ``INSTALLED_APPS``
* Create a list of ``LANDING_PAGE_TEMPLATES`` that will be used in your landing
  pages. You must create at least one. Typically these will be in your site's
  root template directory.

Admin Configuration
-------------------

* Configure your **Site** as appropriate.
* Create a **Page** including key and landing template.
* Add **Question** if needed.

Templates
=========

The templates include a flexible layout scheme that allows you to define named
blocks in your template file and type the content into the **Page** using the
Django Admin.

Here is an example landing page template that you can include in your Django Site::

    {% extends "base.html" %}

    {% block content %}

        <div class="jumbotron">
            <div class="container">
                {{ content.main|safe }}
            </div>
        </div>

        {% include "apollo/buttons.html" %}
    {% endblock %}

This assumes that you have a ``base.html`` template that defines your overall
site layout and contains a content block.

Save this to a file ``landing1.html`` in your templates directory and then
configure ``LANDING_PAGE_TEMPLATES``::

    LANDING_PAGE_TEMPLATES = (
        ('landing1.html', 'Landing Page One'),
    )

Variable Page Content
---------------------

Note the ``content.main`` template variable in the above example. Any Page
Content that you add in the Django Admin for the **Page** will be added with
the key into this content dictionary. You can arrange these in your landing
page templates however you'd like, then easily update them in the admin site.

In addition to regular variables, you can expose a list by ending your keys
with an index. For example use keys in the format ideas[0], ideas[1]... to
create a template that iterates over a variable ``content.ideas``::

    {% for i in content.ideas %}
      ...
    {% endfor %}

