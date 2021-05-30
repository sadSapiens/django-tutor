from django.shortcuts import render
from django.http import HttpResponse


def posts(request) -> HttpResponse:
    return HttpResponse('<h1>Это страница блогов</h1>')
