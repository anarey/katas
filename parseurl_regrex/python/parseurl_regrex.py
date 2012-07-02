import re

def get_protocol(url):
    pattern = re.compile("http")
    post_pattern = pattern.search(url)
    if post_pattern :
        return post_pattern.group()
    else:
        pattern = re.compile("ftp")
        post_pattern = pattern.search(url)
        if post_pattern :
            return "ftp"
        else:
            return "smb"
