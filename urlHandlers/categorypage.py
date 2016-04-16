from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from scripts import utils

def index(request, slug):

    try:
        categoryID = utils.getIDFromSlug(slug)
    except Exception as e:
        raise Http404()

    ## request detials from api

    variables = {
        "page_title": "categories",
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
    
    return render(request, 'categorypage.html', variables)
