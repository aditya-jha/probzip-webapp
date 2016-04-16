
def getIDFromSlug(slug):
    slug = slug.split('-')
    return int(slug[len(slug)-1])
