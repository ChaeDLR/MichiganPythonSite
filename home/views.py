from django.http import HttpResponse, Http404
from django.template import loader, Template
from django.template.exceptions import TemplateDoesNotExist


def index(request) -> HttpResponse:
    try:
        template: Template = loader.get_template("home/index.html")
    except TemplateDoesNotExist:
        return Http404()
    return HttpResponse(template.render(request=request))


def about(request) -> HttpResponse:
    try:
        template: Template = loader.get_template("home/about.html")
    except TemplateDoesNotExist:
        return Http404()
    return HttpResponse(template.render(request=request))
