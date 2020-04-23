=================
kp_html_meta
=================

kp_html_meta is a Django app to generate html meta tags for improve SEO.


Quick start
-----------

1. Install django-kp-html-meta::

    pip install django-kp-html-meta

2. Add "kp_static_version" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kp_html_meta',
    ]

3. Define default values in you settings.py (optional)::

    # Default values
    KP_META = {
        'kp_meta_title': "Test title",  # ex: <title>Test title</title>
        'kp_meta_description': "Test description",  # ex: <meta name="description" content="Test description"/>
        'kp_meta_keywords': "Test keyword",
        'kp_meta_graph_type': "article ",
        'kp_meta_graph_image': "https://mywebsite.com/logo.jpg",
        'kp_meta_graph_url': "https://mywebsite.com",
        'kp_meta_graph_locale': "en",
        'kp_get_base_url': "https://mywebsite.com",
        'kp_meta_graph_site_name': "mywebsite",
    }

4. Load templatetags into your template::

    {% load kp_meta %}
    <head>
        <meta charset="UTF-8">
        {% kp_meta %}
    </head>

5. Result::

    <title>Test title</title>
    <meta name="description" content="Test description"/>
    <meta name="keywords" content="Test keyword"/>
    <meta property="og:title" content="Test title">
    <meta property="twitter:title" content="Test title">
    <meta property="og:url" content="https://mywebsite.com">
    <meta property="twitter:url" content="https://mywebsite.com">
    <meta property="og:description" content="Test description">
    <meta property="og:image" content="https://mywebsite.com/logo.jpg">
    <meta property="twitter:image" content="https://mywebsite.com/logo.jpg">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="mywebsite">
    <meta property="twitter:site" content="mywebsite">
    <meta property="og:locale" content="en">
    
Customization
-------------

The values defined in the settings.py file are default values.
They are used if no other values exist.
You can customize the content of the HTML tags according to your templates. Example::

    from django.db import models
    from kp_html_meta.models import KPMetaHelper

    class DummyModel(models.Model, KPMetaHelper):
        # ... some fields

    def get_kp_meta_title(self):
        # kp_meta_title in settings.py
        return self.title

    def get_kp_meta_description(self):
        # kp_meta_description in settings.py
        return self.text_of_my_article[:200]

    def get_kp_meta_keywords(self):
        # If None then the value defined in settings.py will be used.
        # kp_meta_keywords in settings.py
        return None

    def get_kp_meta_graph_type(self):
        return None

    def get_kp_meta_graph_image(self):
        return None

    def get_kp_meta_graph_url(self):
        return None

    def get_kp_meta_graph_locale(self):
        return None

    def get_kp_meta_graph_site_name(self):
        """
        Return site name

        for example:

        return "mywebsite.tld"

        or

        from django.conf import settings
        kp_settings = getattr(settings, 'KP_META')
        :return kp_settings['kp_meta_graph_site_name']

        or

        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        return current_site.domain

        """

        return None

    def get_kp_get_base_url(self):
        """
        Return base url

        for example:

        return "https://mywebsite.tld"

        or

        from django.conf import settings
        kp_settings = getattr(settings, 'KP_META')
        :return kp_settings['kp_get_base_url']

        or

        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        return "https://%s" % current_site.domain

        """
        return None

You can extend your templates with predefined fields::

    from kp_html_meta.models import KPMetaGraphFiler

    # if you use django-filer
    class DummyModel(KPMetaGraphFiler):

    from kp_html_meta.models import KPMetaGraphFileBrowser

    # if you use django-filebrowser
    class DummyModel(KPMetaGraphFileBrowser):

If you customize your models, use the templatetags like this::

    {% load kp_meta %}
    <head>
        <meta charset="UTF-8">
        {% kp_meta myobj %}
    </head>
