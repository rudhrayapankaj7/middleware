# file: middleware_demo/views.py
#  TemplateResponse does not return any data back to the user until it reaches the middleware.

from django.template.response import TemplateResponse


def index(request):
    print("we are in views 1")
    context = {"name":"hey this is pankaj suryawanshi"}
    return TemplateResponse(request, "middleware_demo/index.html", context=context)