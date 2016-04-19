

def getIDFromSlug(slug):
    slug = slug.split('-')
    return int(slug[len(slug)-1])

def apiBaseURL():
    return "http://localhost:8000/"

def siteBaseURL():
    return "http://localhost:8001/"


