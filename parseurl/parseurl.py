class NotProtocolFound(Exception):
    pass

def get_protocol(url):
    if url.find("://") < 0:
        raise NotProtocolFound
    url_splitted = url.split(":")
    protocol = url_splitted[0]
    return protocol

def get_site(site):
    if site.endswith("www.site.com"):
        return "www.site.com"
    elif site.endswith("www.google.com"):
        return "www.google.com"
    elif site.endswith("www.twitter.com"):
        return "www.twitter.com"
    else:
        return ""
