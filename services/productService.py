from django.http import Http404

from decimal import Decimal
import requests, json
from scripts import apiUrlMapper


def getProductData(productID):

    params = {
        "productID": productID
    }
    productAPIURL = apiUrlMapper.generateUrl("product", params)
    requestResponse = requests.get(productAPIURL)
    print requestResponse
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
