from django.shortcuts import render
from django.http import HttpResponse, Http404

from scripts import utils
from services import categoryService

def index(request, category_slug):

    categoryID = utils.getIDFromSlug(category_slug)
    data = categoryService.getAllCategoriesData()
    products_data = categoryService.getCategoryProductsData(str(categoryID))

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
