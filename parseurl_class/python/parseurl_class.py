import re

class Parseurl:
    def __init__(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_protocol(self):
        protocol = ""
        
        if re.search("://", self.url):
            protocol_search = re.split("://", self.url)
            protocol = protocol_search[0] 
        return protocol 

    def get_site(self):
        site_search = self.url
        site = ""
        
        if re.search("://", self.url):
            site_without_protocol = re.split("://", self.url)
            site_search = site_without_protocol[1]

        if re.search("/", site_search):
            site_search = re.split("/", site_search)
            site_search = site_search[0]

        pattern = re.compile("(\w\w\w\.)?[a-z0-9]+\.[a-z0-9]+")

        if pattern.search(site_search):
            site_search = pattern.search(site_search)
            site = site_search.group(0)
        return site
        
    def get_path(self):
        path = ""
         
        site = self.get_site()
        
        if site != "":
            pattern = re.compile("(\w\w\w\.)?[a-z0-9]+\.[a-z0-9]+")
            if pattern.search(site):
                if re.search(site, self.url):
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

