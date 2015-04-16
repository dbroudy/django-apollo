import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-apollo',
    version='0.2.1',
    packages=['apollo'],
    include_package_data=True,
    license='MIT',
    description='A simple landing page Django app with quick setup, minimal dependencies, but still managable from Django admin pages.',
    keywords='landing page mvp minimum viable project launch',
    long_description=README,
    url='https://github.com/dbroudy/django-apollo/',
    author='David Broudy',
    author_email='dave@broudy.net',
    install_requires=[
        'django-ckeditor>=4.4.4',
        'django-widget-tweaks>=1.3',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
