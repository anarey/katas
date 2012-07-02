import re

class NotProtocolFound:
    pass

def get_protocol(url):

    if re.search("://",url):
        eo = re.split("://", url)
        return eo[0]
#        pattern = re.compile("")
#    if re.search("://", url):
#        pattern = re.compile("https|http|ftp|smb")
#        post_pattern = pattern.search(url)
#        if post_pattern :
#            return post_pattern.group()
    else:
        raise NotProtocolFound
