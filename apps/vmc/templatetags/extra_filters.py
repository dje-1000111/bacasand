"""Extra filters."""
from django import template

register = template.Library()


@register.filter(name="count_msg_by_thread")
def count_msg_by_thread(value, arg):
    """Count msg by thread."""
    return (
        len(value.filter(thread_id=arg)) - 1
        if (len(value.filter(thread_id=arg)) - 1) > 0
        else 0
    )


@register.filter(name="get_current_url_lang")
def get_current_url_lang(url):
    return url.replace("/", "")[0:2]


@register.filter(name="complete_current_url_lang")
def complete_current_url_lang(url):
    return f"{url[4:]}"
