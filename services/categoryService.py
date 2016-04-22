from django.http import Http404

from scripts import apiUrlMapper

import requests, json
from decimal import Decimal

def getAllCategoriesData():

    categoryAPIURL = apiUrlMapper.generateUrl('category')
    requestResponse = requests.get(categoryAPIURL)

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

def getCategoryProductsData(categoryID):

    params =  {
        "categoryID": categoryID
    }
    categoryAPIURL = apiUrlMapper.generateUrl('category', params)
    requestResponse = requests.get(categoryAPIURL)

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
