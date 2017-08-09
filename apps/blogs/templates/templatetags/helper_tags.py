from django import template
from apps.blogs.models import Category

register = template.Library()

@register.assignment_tag
def get_categories(id):
    return list(Category.objects.filter(post__pk=id).values_list('name', flat=True))