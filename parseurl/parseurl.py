class NotProtocolFound(Exception):
    pass

class NotSiteFound(Exception):
    pass

def get_protocol(url):
    if url.find("://") < 0:
        raise NotProtocolFound
    url_splitted = url.split(":")
    protocol = url_splitted[0]
    return protocol

def get_site(url):
    url_splitted = url.split("://")
    if len(url_splitted) == 2:
        site_splitted = url_splitted[1]
        if site_splitted == "":
            raise NotSiteFound
        site = site_splitted.split("/")[0]
    else:
        site_splitted = url_splitted[0]
        site = site_splitted.split("/")[0]
    return site

