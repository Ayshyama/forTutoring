from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag
def hello_world():
    return "Hello World!"


@register.inclusion_tag('testapp/footer.html')
def render_footer(company_name='My Company'):
    return {'company_name': company_name}


@register.simple_tag
def current_time():
    cur_time = datetime.now()
    formatted_time = cur_time.strftime('%H:%M:%S')
    return formatted_time


@register.filter
def reverse(string):
    return string[::-1]
