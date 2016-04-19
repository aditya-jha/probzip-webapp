import requests
import json
from django.http import Http404
from decimal import Decimal
from .utils import *

def getAllCategoriesData():

    categoryString = "category/"

    categoryURL = apiBaseURL() + categoryString

    requestResponse = requests.get(categoryURL)

    data = []

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

    categoryString = "category/"

    categoryQueryParameter = "?categoryID="

    categoryURL = apiBaseURL() + categoryString + categoryQueryParameter + category_slug

    requestResponse = requests.get(categoryURL)

    product_data = []

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


def getProductData(product_slug):

    productString = "product/"

    productQueryParameter = "?productID="

    productURL = apiBaseURL() + productString + productQueryParameter + product_slug

    requestResponse = requests.get(productURL)

    dict = {}

    if requestResponse.status_code == requests.codes.ok:
        try:
            jsonText = json.loads(requestResponse.text)

            if jsonText["statusCode"] != "2XX":
                raise Http404()

            products = jsonText["body"]["products"]

        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return products[0]