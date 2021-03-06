import re

class MyError(Exception):
    def __init__(self, value_exception):
        self.value_exception = value_exception

    def __str__(self):
        return self.value_exception

class NotProtocolFoundError(MyError):
    def __init__(self, value_exception):
        MyError.__init__(self, value_exception)

class NotSiteFoundError(MyError):
    def __init__(self, value_exception):
        MyError.__init__(self, value_exception)

def get_protocol(url):

    if re.search("://", url):
        protocol_search = re.split("://", url)
        protocol = protocol_search[0]
        return protocol
    else:
        raise NotProtocolFoundError("Prococol not found")

def get_site(url):
    if re.search("://", url):
        site_without_protocol = re.split("://", url)
        site_search = site_without_protocol[1]
    else:
        site_search = url

    if re.search("/", site_search):
        site_search = re.split("/", site_search)
        site_search = site_search[0]

    pattern = re.compile("(\w\w\w\.)?[a-z0-9]+\.[a-z0-9]+")
    if pattern.search(site_search):
        site_search = pattern.search(site_search)
        site = site_search.group(0)
    else:
        raise NotSiteFoundError("Site not found")

    return site

def get_path(url):
    path = ""
    try:
        site = get_site(url)
    except NotSiteFoundError:
        raise NotSiteFoundError("Site not found")

    pattern = re.compile("(\w\w\w\.)?[a-z0-9]+\.[a-z0-9]+")
    if pattern.search(site):
        if re.search(site, url):
            path_search = re.split(site, url)
            path = path_search[1]
            if re.search("^/", path):
                path = re.split("^/", path)[1]

    return path

def parse_url(url):

    try:
        protocol = get_protocol(url)
    except NotProtocolFoundError:
        protocol = ""

    try:
        site = get_site(url)
    except NotSiteFoundError:
        site = ""

    try:
        path = get_path(url)
    except NotSiteFoundError:
        path = ""

    return protocol, site, path
