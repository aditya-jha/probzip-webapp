

def getIDFromSlug(slug):
	try:
		slug = slug.split('-')
		arr = int(slug[len(slug)-1])
	except Exception as e:
		raise Http404()
	return arr
