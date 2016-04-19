from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from scripts import utils
from services import categoryservice

def index(request, category_slug):

    categoryID = utils.getIDFromSlug(category_slug)
    data = categoryservice.getAllCategoriesData()
    products_data = categoryservice.getCategoryProductsData(str(categoryID))

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
