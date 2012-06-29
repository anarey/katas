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
    if site.find(".") < 0: 
        site = ""
    return site

def get_path(url):
    url_splitted = url.split("://")
    len_url_splitted = len(url_splitted)
    path_splitted = url_splitted[len_url_splitted-1].split("/")
    path = ("/").join(path_splitted[1:])
    return path

def parse_url(url):
    
    try: 
        protocol = get_protocol(url)
    except (NotProtocolFound):
        protocol = ""
    try:
        site = get_site(url)
    except (NotSiteFound):
        site = ""
    path = get_path(url)

    return [protocol, site, path]
