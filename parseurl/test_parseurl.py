#### 
import unittest 
from parseurl import get_protocol, get_site, NotProtocolFound

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

    def test_not_site(self):
        site = get_site("http://www.site2.com")
        self.assertNotEqual(site, "www.site.com")
    
    def test_site_google(self):
        site = get_site("http://www.google.com")
        self.assertEqual(site,"www.google.com")
    
    def test_site_twitter(self):
        site = get_site("http://www.twitter.com")
        self.assertEqual(site,"www.twitter.com")
