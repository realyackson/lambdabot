from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.safestring import mark_safe


def htmlimg(url, mw=150, mh=150):
    return mark_safe(f'<img src="{url}" style="max-width: {mw}px; max-height: {mh}px;">')


def ahref(url, text, newtab=False):
    return mark_safe('<a href="{0}"{1}>{2}</a>'.format(url, newtab and ' target="_blank"' or '', text))


def list_url(model, query_map, text):
    content_type = ContentType.objects.get_for_model(model)
    url = reverse("admin:%s_%s_changelist" % (content_type.app_label, content_type.model)) + '?'
    for k, v in query_map.items():
        url += f'&{k}={v}'
    return ahref(url, str(text))


def object_url(model, obj_id, text):
    content_type = ContentType.objects.get_for_model(model)
    url = reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(obj_id,))
    return ahref(url, str(text))
