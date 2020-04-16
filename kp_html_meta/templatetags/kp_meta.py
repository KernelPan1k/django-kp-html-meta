from django import template
from django.conf import settings
from django.utils.html import strip_tags

try:
    from html import unescape
except ImportError:
    try:
        from html.parser import HTMLParser
    except ImportError:
        from HTMLParser import HTMLParser  # python 2.x
    unescape = HTMLParser().unescape

register = template.Library()


def sanitize(txt):
    if not txt:
        return None

    txt = unescape(txt)
    txt = strip_tags(txt)
    txt = txt.strip()

    return txt


@register.inclusion_tag('kp_meta/meta.html')
def kp_meta(obj=None):
    kp_settings = getattr(settings, 'KP_META', {})

    list_fields = [
        'kp_meta_title',
        'kp_meta_description',
        'kp_meta_keywords',
        'kp_meta_graph_type',
        'kp_meta_graph_url',
        'kp_meta_graph_locale',
        'kp_meta_graph_image',
        'kp_meta_graph_site_name',
    ]

    context = {}

    for field_name in list_fields:
        field_value = None

        if obj:
            field_method = getattr(obj, "get_%s" % field_name, None)
            field_value = field_method() if field_method else None

        if not field_value:
            field_value = kp_settings.get(field_name, None)

        context[field_name] = sanitize(field_value)

    return context
