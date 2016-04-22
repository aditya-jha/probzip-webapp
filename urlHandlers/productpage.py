from django.http import Http404
from django.shortcuts import render

from scripts import utils
from services import productservice, categoryservice


def index(request, category_slug, product_slug):

    productID = utils.getIDFromSlug(product_slug)
    data = categoryservice.getAllCategoriesData()
    product_data = productservice.getProductData(str(productID))

    variables = {
        "page_title": "products",
        "sidebar_navigation": {
            "display": True,
            "data": data
        },
        "categories": [1,2,3,4],
        "product_data" : product_data
    }

    return render(request, 'productpage.html', variables)
