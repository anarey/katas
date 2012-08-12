import re

class Url:
    def __init__(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def correct_site(self, site_search):
        site = ""

        pattern = re.compile("(\w\w\w\.)?[a-z0-9]+\.[a-z0-9]+")

        if pattern.search(site_search):
            site_search = pattern.search(site_search)
            site = site_search.group(0)
        return site

    def delete_slash(self, site):

        if re.search("/", site):
            site = re.split("/", site)
            site = site[0]

        return site 

    def split_double_slash_dot(self):

        split_url = ["",""]
        if re.search("://", self.url):
            protocol_search = re.split("://", self.url)
            split_url[0] = protocol_search[0] 
            split_url[1] = protocol_search[1]
        else:
            split_url[0] = ""
            split_url[1] = self.url
        return split_url


    def get_protocol(self):

        protocol = self.split_double_slash_dot()
        
        return protocol[0]

    def get_site(self):
        site = ""

        site_split = self.split_double_slash_dot()
        site_search = site_split[1]
        
        if site_search != "":
            site_without_slash = self.delete_slash(site_search)
            site = self.correct_site(site_without_slash)

        return site

    def get_path(self):
        path = ""
         
        site = self.get_site()
        
        if site != "":
            path_search = re.split(site, self.url)
            path = path_search[1]
            if re.search("^/", path):
                path = re.split("^/", path)[1]
        return path

    def parse_url(self):
        protocol = self.get_protocol()
        site = self.get_site()
        
        if site != "": 
            path = self.get_path()
        else:
            path = ""
        return protocol, site, path

def main():
    
    if __name__ == '__main__':
        main()

