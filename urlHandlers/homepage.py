from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404

from scripts import utils
from services import categoryService


def index(request):
    ## fetch relevant data from API
    data = categoryService.getAllCategoriesData()

    variables = {
        "page_title": "homepage",
        "sidebar_navigation": {
            "display": True,
            "data": data
        },
        "categories": [1,2,3,4]
    }

    return render(request, 'homepage.html', variables)
