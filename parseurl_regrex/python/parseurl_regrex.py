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
    pattern = re.compile("www\..*\..*/?")
    if pattern.search(url):
        site_search = pattern.search(url)
        site = site_search.group(0)
        site = site.split("/")[0]
    else:
        raise NotSiteFound
    return site

def get_path(url):
#    path = ""
    if re.search("www\.[a-z0-9]+\.[a-z0-9]+?/", url):
        path_search = re.split("www\.[a-z0-9]+\.[a-z0-9]+?/", url)
        path = path_search[1]
    return path


