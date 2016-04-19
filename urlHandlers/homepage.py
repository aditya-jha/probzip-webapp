from django.shortcuts import render
from django.http import HttpResponseRedirect
from scripts import utils


def index(request):

    data = utils.getAllCategoriesData()

    variables = {
        "page_title": "homepage",
        "sidebar_navigation": {
            "display": True,
            "data": data
        },
        "categories": [1,2,3,4]
    }

    return render(request, 'homepage.html', variables)
