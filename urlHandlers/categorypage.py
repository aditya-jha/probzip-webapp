from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from scripts import utils, services

def index(request, category_slug):

    try:
        categoryID = utils.getIDFromSlug(category_slug)
        data = services.getAllCategoriesData()
        products_data = services.getCategoryProductsData(str(categoryID))
    except Exception as e:
        raise Http404()

    ## request detials from api




    variables = {
        "page_title": "categories",
        "sidebar_navigation": {
            "display": True,
            "data": data
        },
        "categories": [1,2,3,4],
        "products_data":products_data
    }

    return render(request, 'categorypage.html', variables)
