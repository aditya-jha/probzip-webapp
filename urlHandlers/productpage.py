from django.http import Http404
from django.shortcuts import render

from scripts import utils

def index(request, category_slug, product_slug):
    try:
        productID = utils.getIDFromSlug(product_slug)
    except Exception as e:
        raise Http404()
    variables = {
        "page_title": "homepage",
        "sidebar_navigation": {
            "display": True,
            "data": [
                {
                    "displayName": "Kurti",
                    "url": "kurti"
                },
                {
                    "displayName": "Kurti",
                    "url": "kurti"
                },
                {
                    "displayName": "Kurti",
                    "url": "kurti"
                }
            ]
        },
        "categories": [1,2,3,4]
    }

    return render(request, 'productpage.html', variables)
