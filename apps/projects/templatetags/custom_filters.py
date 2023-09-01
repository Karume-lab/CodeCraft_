from django import template

register = template.Library()

@register.filter
def get_progress_color(progress):
    if progress >= 75:
        return 'green'
    elif progress >= 50:
        return 'yellow'
    elif progress >= 25:
        return 'orange'
    else:
        return 'red'

