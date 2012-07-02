import re

def get_protocol(url):
    pattern = re.compile("http")
    post_pattern = pattern.search(url)
    return post_pattern.group()
