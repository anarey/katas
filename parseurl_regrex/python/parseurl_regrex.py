import re

class MyError(Exception):
    def __init__(self, value_exception):
        self.value_exception = value_exception

    def __str__(self):
        return self.value_exception

class NotProtocolFoundError(MyError):
    pass

class NotSiteFoundError(MyError):
    pass

def get_protocol(url):

    if re.search("://", url):
        protocol_search = re.split("://", url)
        protocol = protocol_search[0]
        return protocol
    else:
        raise NotProtocolFoundError("Prococol not found")

def get_site(url):
    pattern = re.compile("www\.[a-z0-9]+\.[a-z0-9]+/?")
    if pattern.search(url):
        site_search = pattern.search(url)
        site = site_search.group(0)
        site = site.split("/")[0]
    else:
        raise NotSiteFoundError("Site not found")
    return site

def get_path(url):
    path = ""
    pattern = re.compile("www\.[a-z0-9]+\.[a-z0-9]+/")
    if pattern.search(url):
        path_search = pattern.split(url)
        path = path_search[1]
    return path

def parse_url(url):

    try:
        protocol = get_protocol(url)
    except (NotProtocolFoundError):
        protocol = ""
    try:
        site = get_site(url)
    except (NotSiteFoundError):
        site = ""
    path = get_path(url)

    return protocol, site, path
