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
        # This check is because if the url
        # has not site (http://) then the url_splitted
        # values are ["http", ""]
        if site_splitted == "":
            raise NotSiteFound
    else:
        site_splitted = url_splitted[0]
    site = site_splitted.split("/")[0]
    return site

def get_path(url):
    if url.endswith("index.html"):
        return "index.html"
    else:
        return ""
