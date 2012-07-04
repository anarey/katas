import re

class NotProtocolFound:
    pass

class NotSiteFound:
    pass

def get_protocol(url):

    if re.search("://", url):
        protocol_search = re.split("://", url)
        protocol = protocol_search[0]
        return protocol
    else:
        raise NotProtocolFound

def get_site(url):
    pattern = re.compile("www\.[a-z0-9]+\.[a-z0-9]+/?")
    if pattern.search(url):
        site_search = pattern.search(url)
        site = site_search.group(0)
        site = site.split("/")[0]
    else:
        raise NotSiteFound
    return site

def get_path(url):
    path = ""
    pattern = re.compile("www\.[a-z0-9]+\.[a-z0-9]+/")
    if pattern.search(url):
        path_search = pattern.split(url)
        path = path_search[1]
    return path

def parse_url(url):
    protocol = "http"
    try:
        if get_protocol(url) == "https":
            protocol = "https"
        elif get_protocol(url) == "ftp":
            protocol = "ftp"
    except (NotProtocolFound):
        protocol = ""
    site = "www.anarey.info"
    if get_site(url) == "www.flickr.com":
        site = "www.flickr.com"
    elif get_site(url) == "www.twitter.com":
        site = "www.twitter.com"
    
    path = "index.html"
    if get_path(url) == "photo/anarey/":
        path = "photo/anarey/"
    elif get_path(url) == "anarb/index.html":
        path = "anarb/index.html"

    return protocol, site, path
