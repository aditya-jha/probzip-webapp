from django.shortcuts import render
from django.http import HttpResponseRedirect
from scripts import utils, services
from django.http import Http404


def index(request):
    try:
        data = services.getAllCategoriesData()
    except Exception as e:
        raise Http404()

    variables = {
        "page_title": "homepage",
        "sidebar_navigation": {
            "display": True,
            "data": data
        },
        "categories": [1,2,3,4]
    }

    return render(request, 'homepage.html', variables)
