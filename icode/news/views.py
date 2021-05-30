from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello index")


def test(request) -> HttpResponse:
    return HttpResponse("Hello test")
