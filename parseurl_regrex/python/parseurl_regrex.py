import re

class NotProtocolFound:
    pass

def get_protocol(url):

    if re.search("://",url):
        eo = re.split("://", url)
        return eo[0]
    else:
        raise NotProtocolFound

def get_site(url):
    return "www.site.com"
