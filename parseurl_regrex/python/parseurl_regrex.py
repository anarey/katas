import re

def get_protocol(url):
    pattern = re.compile("https|http|ftp|smb")
    post_pattern = pattern.search(url)
    if post_pattern :
        return post_pattern.group()
