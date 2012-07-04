import re

class NotProtocolFound:
    pass

class NotSiteFound:
    pass

def get_protocol(url):

    if re.search("://",url):
        eo = re.split("://", url)
        return eo[0]
    else:
        raise NotProtocolFound

def get_site(url):
    if re.search("www\..*\..*/?", url):
        site_search = re.search("www\..*\..*/?", url)
        site = site_search.group(0)
        site = site.split("/")[0]
    else:
        raise NotSiteFound
    return site
