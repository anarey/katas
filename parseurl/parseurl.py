class NotProtocolFound(Exception):
    pass

def get_protocol(url):
    if url.find("://") < 0:
        raise NotProtocolFound
    url_splitted = url.split(":")
    protocol = url_splitted[0]
    return protocol

def get_site(url):
    url_splitted = url.split("://")
    site = url_splitted[1]
    return site

