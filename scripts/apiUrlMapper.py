mapper = {
	"base_url": "http://api.probzip.com/",
	"category": "category/",
	"product": "products/",
}

def getUrlFromParams(params):
	url = ""
	keys = params.keys()
	if len(keys):
		for k in keys:
			url += '&' + k + '=' + params[k]
	return url[1:]

def generateUrl(type, params = {}):
	urlFromParams = getUrlFromParams(params)
	url = mapper["base_url"] + mapper[type]
	if urlFromParams:
		url += "?" + urlFromParams
	return url
