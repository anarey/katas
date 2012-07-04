import unittest 
#from parseurl import get_protocol, get_site, get_path, parse_url
from parseurl_regrex import get_protocol, get_site, get_path
#from parseurl import NotProtocolFound, NotSiteFound
from parseurl_regrex import NotProtocolFound, NotSiteFound

class test_parse_regrex_protocol(unittest.TestCase):
    def test_protocol_http(self):
        protocol = get_protocol("http://www.site.com")
        self.assertEqual("http", protocol)

    def test_protocol_not_http(self):
        protocol = get_protocol("ftp://www.site.com")
        self.assertNotEqual("http", protocol)

    def test_protocolsmb(self):
        protocol = get_protocol("smb://www.site.com")
        self.assertEqual("smb", protocol)

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
        self.assertEqual(site, "www.google.com")
    
    def test_site_twitter(self):
        site = get_site("http://www.twitter.com")
        self.assertEqual(site, "www.twitter.com")

    def test_not_protocol(self):
        site = get_site("www.google.com")
        self.assertEqual(site, "www.google.com")

    def test_long_url(self):
        site = get_site("http://www.anarey.info/aaaa")
        self.assertEqual(site, "www.anarey.info")

    def test_long_url_not_protocol(self):
        site = get_site("www.anarey.info/holamundo/dkef/ed")
        self.assertEqual(site, "www.anarey.info")

    def test_not_site_found(self):
        self.assertRaises(NotSiteFound, get_site, "http://")

class test_parse_path(unittest.TestCase):
    def test_path(self):
        path = get_path("http://www.anarey.info/index.html")
        self.assertEqual(path, "index.html")

    def test_path_notequal(self):
        path = get_path("http://www.anarey.info/index2.html")
        self.assertNotEqual(path, "index.html")

    def test_path_about(self):
        path = get_path("http://www.anarey.info/acerca-de")
        self.assertEqual(path, "acerca-de")

    def test_long_path(self):
        path = get_path("http://www.anarey.info/un/paseo/por")
        self.assertEqual(path, "un/paseo/por")

#    def test_path_url_not_protocol(self):
#        path = get_path("www.anarey.info/un/paseo.html")
#        self.assertEqual(path, "un/paseo.html")
#
#class test_parse_url(unittest.TestCase):
#    def test_return_value(self):
#        protocol, site, path = parse_url("http://www.anarey.info/index.html")
#        self.assertEqual(protocol, "http")
#        self.assertEqual(site, "www.anarey.info")
#        self.assertEqual(path, "index.html")
#
#    def test_parse_url_notequal(self):
#        protocol, site, path = parse_url("https://www.flickr.com/photo/anarey/")
#        self.assertNotEqual(protocol, "http")
#        self.assertNotEqual(site, "www.anarey.info")
#        self.assertNotEqual(path, "photo/anarey")
#
#    def test_parse_url_twitter(self):
#        protocol, site, path = parse_url("ftp://www.twitter.com/anarb/index.html")
#        self.assertEqual(protocol, "ftp")
#        self.assertEqual(site, "www.twitter.com")
#        self.assertEqual(path, "anarb/index.html")
#    
#    def test_parse_url_not_protocol(self):
#        protocol, site, path = parse_url("www.twitter.com/anarb/index.html")
#        self.assertEqual(protocol, "")
#        self.assertEqual(site, "www.twitter.com")
#        self.assertEqual(path, "anarb/index.html")
#
#### Prueba que cumple, no falla inicialmente
##    def test_parse_url_not_path(self):
##        protocol, site, path = parse_url("http://www.twitter.com")
##        self.assertEqual(protocol, "http")
##        self.assertEqual(site, "www.twitter.com")
##        self.assertEqual(path, "")
#
#    def test_parse_url_not_site(self):
#        protocol, site, path = parse_url("http://")
#        self.assertEqual(protocol, "http")
#        self.assertEqual(site, "")
#        self.assertEqual(path, "")
#
#    def test_parse_not_url(self):
#        protocol, site, path = parse_url("ana%243f")
#        self.assertEqual(protocol, "")
#        self.assertEqual(site, "")
#        self.assertEqual(path, "")
#    def test_parse_not_url_2(self):
#        protocol, site, path = parse_url("ssefd/index.html")
#        self.assertEqual(protocol, "")
#        self.assertEqual(site, "")
#        self.assertEqual(path, "")
#
