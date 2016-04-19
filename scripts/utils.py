import requests
import json
from decimal import Decimal

def getIDFromSlug(slug):
    slug = slug.split('-')
    return int(slug[len(slug)-1])

def apiBaseURL():
    return "http://localhost:8000/"

def siteBaseURL():
    return "http://localhost:8001/"

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

            for c in categories:
                dict = {}
                dict["displayName"] = c["display_name"]
                dict["name"] = c["name"]
                dict["slug"] = c["slug"]
                dict["id"] = c["id"]
                dict["url"] = siteBaseURL() + c["slug"] + "-" + str(c["id"])
                data.append(dict)
                pass
        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return data

def getCategoryProductsData(category_slug):

    categoryString = "category/"

    categoryQueryParameter = "?categoryID="

    categoryURL = apiBaseURL() + categoryString + categoryQueryParameter + category_slug

    requestResponse = requests.get(categoryURL)

    product_data = []


    if requestResponse.status_code == requests.codes.ok:

        try:
            jsonText = json.loads(requestResponse.text)

            print jsonText["statusCode"]

            if jsonText["statusCode"] != "2XX":
                raise Http404()

            products = jsonText["body"]["products"]

            for p in products:
                dict = {}
                dict["price_per_lot"] = p["price_per_lot"]
                dict["category_id"] = p["category_id"]
                dict["product_id"] = p["product_id"]
                dict["price_per_unit"] = p["price_per_unit"]
                dict["tax"] = p["tax"]
                dict["seller_name"] = p["seller_name"]
                dict["show_online"] = p["show_online"]
                dict["seller_id"] = p["seller_id"]
                dict["lot_size"] = p["lot_size"]
                dict["verification"] = p["verification"]
                dict["category_name"] = p["category_name"]
                dict["name"] = p["name"]
                dict["price_per_lot"] = p["price_per_lot"]
                dict["slug"] = p["slug"]

                product_lots_json = p["product_lot"]

                product_lots = []

                for pl in product_lots_json:
                    dict1 = {}
                    dict1["lot_id"] = pl["lot_id"]
                    dict1["lot_discount"] = pl["lot_discount"]
                    dict1["lot_size_to"] = pl["lot_size_to"]
                    dict1["lot_size_from"] = pl["lot_size_from"]
                    product_lots.append(dict1)

                max_discount = Decimal(product_lots[len(product_lots) - 1]["lot_discount"])
                dict["max_discount"] = '%.2f' %  max_discount
                discounted_price = Decimal(p["price_per_unit"])*(1-max_discount/100)
                dict["discounted_price_per_unit"] = '%.2f' % discounted_price

                dict["product_lot"] = product_lots
                url_string = siteBaseURL() + p["category_slug"] + "-" + str(p["category_id"]) + "/"
                url_string += p["slug"] + "-" + str(p["product_id"])

                dict["url"] = url_string

                product_data.append(dict)
                pass
        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return product_data


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
            p = products[0]

            dict["price_per_lot"] = p["price_per_lot"]
            dict["category_id"] = p["category_id"]
            dict["product_id"] = p["product_id"]
            dict["price_per_unit"] = p["price_per_unit"]
            dict["tax"] = p["tax"]
            dict["seller_name"] = p["seller_name"]
            dict["show_online"] = p["show_online"]
            dict["seller_id"] = p["seller_id"]
            dict["lot_size"] = p["lot_size"]
            dict["verification"] = p["verification"]
            dict["category_name"] = p["category_name"]
            dict["name"] = p["name"]
            dict["price_per_lot"] = p["price_per_lot"]
            dict["slug"] = p["slug"]

            dict["seller_catalog_number"] = p["seller_catalog_number"]
            dict["description"] = p["description"]
            dict["brand"] = p["brand"]
            dict["pattern"] = p["pattern"]
            dict["style"] = p["style"]
            dict["gsm"] = p["gsm"]
            dict["sleeve"] = p["sleeve"]
            dict["neck_collar_type"] = p["neck_collar_type"]
            dict["length"] = p["length"]
            dict["work_decoration_type"] = p["work_decoration_type"]
            dict["colours"] = p["colours"]
            dict["sizes"] = p["sizes"]
            dict["special_feature"] = p["special_feature"]
            dict["manufactured_country"] = p["manufactured_country"]
            dict["warranty"] = p["warranty"]
            dict["remarks"] = p["remarks"]

            product_lots_json = p["product_lot"]

            product_lots = []

            for pl in product_lots_json:
                dict1 = {}
                dict1["lot_id"] = pl["lot_id"]
                dict1["lot_discount"] = pl["lot_discount"]
                dict1["lot_size_to"] = pl["lot_size_to"]
                dict1["lot_size_from"] = pl["lot_size_from"]
                product_lots.append(dict1)

            max_discount = Decimal(product_lots[len(product_lots) - 1]["lot_discount"])
            dict["max_discount"] = '%.2f' %  max_discount
            discounted_price = Decimal(p["price_per_unit"])*(1-max_discount/100)
            dict["discounted_price_per_unit"] = '%.2f' % discounted_price

            dict["product_lot"] = product_lots

        except Exception as e:
            raise Http404()
    else:
        raise Http404()

    return dict
