############################
django-landing Documentation
############################

About
=====

The best way to prove an idea is to test it. Whether you want to test a new
feature in an existing application or prove an entirely new concept,
django-landing helps you quickly add a landing page to your existing Django
site or create a new landing page base MVP site.

Usage
=====

Settings
--------

* Add 'landing' to your ``INSTALLED_APPS``
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
