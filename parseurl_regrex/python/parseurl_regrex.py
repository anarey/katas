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
    if re.search("www\.site\.com", url):
        return "www.site.com"
    elif re.search("www\.site2\.com", url):
        return "www.site2.com"
    elif re.search("www\.google.com", url):
        return "www.google.com"
    else:
        return "www.twitter.com"
