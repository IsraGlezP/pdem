from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()

@register.filter
def page_window(page, last, size=5):
    if page < size // 2 + 1:
        return range(1, min(size+1, last + 1)) # remember the range function won't 
                                                # include the upper bound in the output
    else:
        return range(page - size // 2, min(last + 1, page + 1 + size // 2))