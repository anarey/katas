#### 
import unittest 

class NotProtocolFound(Exception):
    pass

def get_protocol(url):
    if url.find("://") < 0:
        raise NotProtocolFound
    url_splitted = url.split(":")
    protocol = url_splitted[0]
    return protocol

class test_parse_protocol(unittest.TestCase):
    def test_protocol_http(self):
        protocol = get_protocol("http://www.site.com")
        self.assertEqual("http", protocol)

    def test_protocol_not_http(self):
        protocol = get_protocol("ftp://www.site.com")
        self.assertNotEqual("http", protocol)

    def test_protocol_ftp(self):
        protocol = get_protocol("ftp://www.site.com")
        self.assertEqual("ftp", protocol)

    def test_protocol_https(self):
        protocol = get_protocol("https://www.site.com")
        self.assertEqual("https", protocol)

    def test_not_protocol(self):
        self.assertRaises(NotProtocolFound, get_protocol, "www.site.com")

class test_parse_site(unittest.TestCase):
    def test_site(self):
        site = get_site("http://www.site.com")
        self.assertEqual(site, "www.site.com")

