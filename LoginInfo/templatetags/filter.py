# 自定义过滤器

from django.template import Library

register = Library()


@register.filter
def mod(phone):
    str = phone[0:3]+"****"+phone[7:11]
    return str