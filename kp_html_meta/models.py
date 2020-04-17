from django.db import models
from django.utils.translation import gettext_lazy as _


class KPMetaHelper(models.Model):
    def get_kp_meta_title(self):
        return None

    def get_kp_meta_description(self):
        return None

    def get_kp_meta_keywords(self):
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

    class Meta:
        abstract = True


class KPMetaBase(KPMetaHelper):
    kp_meta_title = models.CharField(
        verbose_name=_("Title tag"),
        null=True,
        blank=True,
        max_length=120,
    )

    kp_meta_description = models.CharField(
        verbose_name=_("Description meta tag"),
        null=True,
        blank=True,
        max_length=255,
    )

    kp_meta_keywords = models.CharField(
        verbose_name=_("Keywords meta tag"),
        null=True,
        blank=True,
        max_length=255,
    )

    def get_kp_meta_title(self):
        return self.kp_meta_title

    def get_kp_meta_description(self):
        return self.kp_meta_description

    def get_kp_meta_keywords(self):
        return self.kp_meta_keywords

    class Meta:
        abstract = True


class KPMetaGraph(KPMetaBase):
    kp_meta_graph_type = models.CharField(
        verbose_name=_("Graph type tag"),
        null=True,
        blank=True,
        max_length=50,
    )

    kp_meta_graph_url = models.URLField(
        verbose_name=_("Graph url tag"),
        null=True,
        blank=True,
        max_length=250,
    )

    kp_meta_graph_locale = models.CharField(
        verbose_name=_("Graph locale tag"),
        null=True,
        blank=True,
        max_length=5,
    )

    def get_kp_meta_graph_type(self):
        return self.kp_meta_graph_type

    def get_kp_meta_graph_url(self):
        return self.kp_meta_graph_url

    def get_kp_meta_graph_locale(self):
        return self.kp_meta_graph_locale

    class Meta:
        abstract = True


class KPMetaGraphFiler(KPMetaGraph):
    from filer.fields.image import FilerImageField

    kp_meta_graph_image = FilerImageField(
        verbose_name=_("Graph image tag"),
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_related",
        on_delete=models.SET_NULL
    )

    def get_kp_meta_graph_image(self):
        if self.kp_meta_graph_image:
            relative_path = self.kp_meta_graph_image.url
            return "%s%s" % (self.get_kp_get_base_url(), relative_path)

        return None

    class Meta:
        abstract = True


class KPMetaGraphFileBrowser(KPMetaGraph):
    from filebrowser.fields import FileBrowseField

    kp_meta_graph_image = FileBrowseField(
        verbose_name=_("Graph image tag"),
        max_length=250,
        blank=True,
        null=True,
    )

    def get_kp_meta_graph_image(self):
        if self.kp_meta_graph_image:
            relative_path = self.kp_meta_graph_image.url
            return "%s%s" % (self.get_kp_get_base_url(), relative_path)

        return None

    class Meta:
        abstract = True
