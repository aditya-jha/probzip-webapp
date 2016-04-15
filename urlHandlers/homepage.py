from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
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

    return render(request, 'homepage.html', variables)
