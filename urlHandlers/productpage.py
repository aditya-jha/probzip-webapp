from django.http import HttpResponse
from django.shortcuts import render

def index(request, category_slug, product_slug):
    return HttpResponse(product_slug)
