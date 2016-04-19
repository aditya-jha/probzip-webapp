import requests
import json
from django.http import Http404
from decimal import Decimal
from scripts import apiurlmapper


def getProductData(product_slug):

    productString = apiurlmapper.mapper["product_page_url"]

    productQueryParameter = apiurlmapper.mapper["product_query_string"]

    productURL = apiurlmapper.mapper["base_url"] + productString + productQueryParameter + product_slug

    requestResponse = requests.get(productURL)

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