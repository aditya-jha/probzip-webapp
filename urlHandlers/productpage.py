from django.http import Http404
from django.shortcuts import render

from scripts import utils


def index(request, category_slug, product_slug):

    try:
        productID = utils.getIDFromSlug(product_slug)
        data = utils.getAllCategoriesData()
        product_data = utils.getProductData(str(productID))
    except Exception as e:
        raise Http404()


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
