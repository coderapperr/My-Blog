from django import template

register = template.Library()


def split_date(value):
    return value.split(',')[0]


register.filter('split_date', split_date)
