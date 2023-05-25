from django.http import HttpResponse
from django.shortcuts import render

from os import getcwd
from os.path import join


def index(request) -> HttpResponse:
    with open(
        join(
            getcwd(),
            "public_html/index.html"
        )
    ) as infile:
        index_html: str = infile.read()
    return HttpResponse(index_html)

def about(request) -> HttpResponse:
    with open(
        join(
            getcwd(),
            "public_html/about.html"
        )
    ) as infile:
        about_html: str = infile.read()
    return HttpResponse(about_html)
