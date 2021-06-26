from django import template
from homepage.models import *

register = template.Library()

@register.filter
def getChilds(patentID):
    return BlogCategory.objects.filter(parent_id=patentID)

@register.filter
def hasChilds(patentID):
    childs = BlogCategory.objects.filter(dparentid=patentID)
    if (childs is not None):
        if(len(childs) > 0):
            return "True"
    return "False"
