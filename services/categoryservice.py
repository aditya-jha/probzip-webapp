import requests
import json
from django.http import Http404
from decimal import Decimal
from scripts import apiurlmapper

def getAllCategoriesData():

    categoryString = apiurlmapper.mapper["category_page_url"]

    categoryURL = apiurlmapper.mapper["base_url"] + categoryString

    requestResponse = requests.get(categoryURL)

    if requestResponse.status_code == requests.codes.ok:
        try:
            jsonText = json.loads(requestResponse.text)
            if jsonText["statusCode"] != "2XX":
                raise Http404()
            categories = jsonText["body"]["categories"]

        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return categories

def getCategoryProductsData(category_slug):

    categoryString = apiurlmapper.mapper["category_page_url"]

    categoryQueryParameter = apiurlmapper.mapper["category_query_string"]

    categoryURL = apiurlmapper.mapper["base_url"] + categoryString + categoryQueryParameter + category_slug

    requestResponse = requests.get(categoryURL)

    if requestResponse.status_code == requests.codes.ok:
        try:
            jsonText = json.loads(requestResponse.text)
            print jsonText

            if jsonText["statusCode"] != "2XX":
                raise Http404()


            products = jsonText["body"]["products"]

        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return products