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
