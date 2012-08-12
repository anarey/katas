import unittest 
import parseurl_class
#from parseurl_class import Parseurl#,iget_site # get_site, get_protocol, get_path, parse_url

class test_parse_regrex_protocol(unittest.TestCase):
    def test_protocol_http(self):
        url_parse = "http://www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("http", url.get_protocol())

    def test_protocol_not_http(self):
        url_parse = "ftp://www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertNotEqual("http", url.get_protocol())

    def test_protocolsmb(self):
        url_parse = "smb://www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("smb", url.get_protocol())

    def test_protocol_https(self):
        url_parse = "https://www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("https", url.get_protocol())

    def test_not_protocol(self):
        url_parse = "www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("", url.get_protocol())

    def test_put_protocol(self):
        url_parse = "http://www.google.com"
        url = parseurl_class.Url(url_parse)
        url.set_protocol("ftp")
        self.assertEqual("ftp", url.get_protocol())

    def test_put_protocol_2(self):
        url_parse = "www.google.com"
        url = parseurl_class.Url(url_parse)
        url.set_protocol("http")
        self.assertEqual("http", url.get_protocol())

    def test_put_protocol_3(self):
        url_parse = "http://"
        url = parseurl_class.Url(url_parse)
        url.set_protocol("ftp")
        self.assertEqual("", url.get_protocol())

class test_parse_site(unittest.TestCase):
    def test_site(self):
        url_parse = "http://www.site.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.site.com", url.get_site())
    
    def test_not_site(self):
        url_parse = "http://www.site2.com"
        url = parseurl_class.Url(url_parse)
        self.assertNotEqual("www.site.com", url.get_site())
    
    def test_site_google(self):
        url_parse = "http://www.google.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.google.com", url.get_site())
    
    def test_site_twitter(self):
        url_parse = "http://www.twitter.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.twitter.com", url.get_site())


    def test_not_protocol(self):
        url_parse = "www.google.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.google.com", url.get_site())

    def test_long_url(self):
        url_parse = "www.anarey.info/aaaaa"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.anarey.info", url.get_site())

    def test_long_url_not_protocol(self):
        url_parse = "www.anarey.info/holamundo/dkef/ed"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("www.anarey.info", url.get_site())

    def test_not_site_found(self):
        url_parse = "htttp://"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("", url.get_site())

    def test_site_notwww(self):
        url_parse = "http://github.org"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("github.org", url.get_site())


    def test_site_notwww_notprotocol(self):
        url_parse = "twitter.com"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("twitter.com", url.get_site())

    def test_put_site(self):
        url_parse = "http://www.google.com"
        url = parseurl_class.Url(url_parse)
        url.set_site("www.twitter.com")
        self.assertEqual("www.twitter.com", url.get_site())

    def test_put_site2(self):
        url_parse = "www.google.com"
        url = parseurl_class.Url(url_parse)
        url.set_site("www.twitter.com")
        self.assertEqual("www.twitter.com", url.get_site())

    def test_put_site3(self):
        url_parse = "www.google.com/aboutme"
        url = parseurl_class.Url(url_parse)
        url.set_site("www.twitter.com")
        self.assertEqual("www.twitter.com", url.get_site())

    def test_put_site4(self):
        url_parse = "www.google.com/aboutme/YO/ANA"
        url = parseurl_class.Url(url_parse)
        url.set_site("www.twitter.com")
        self.assertEqual("www.twitter.com", url.get_site())

class test_parse_path(unittest.TestCase):
    def test_path(self):
        url_parse = "http://www.anarey.info/index.html"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("index.html", url.get_path())

    def test_path_notequal(self):
        url_parse = "http://www.anarey.info/index2.html"
        url = parseurl_class.Url(url_parse)
        self.assertNotEqual("index.html", url.get_path())

    def test_path_about(self):
        url_parse = "http://www.anarey.info/acerca-de"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("acerca-de", url.get_path())

    def test_long_path(self):
        url_parse = "http://www.anarey.info/un/paseo/por"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("un/paseo/por", url.get_path())

    def test_path_url_not_protocol(self):
        url_parse = "www.anarey.info/un/paseo.html"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("un/paseo.html", url.get_path())

    def test_path_not_path(self):
        url_parse = "www.anarey.info"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("", url.get_path())

    def test_path_not_www(self):
        url_parse = "anarey.info/info/aboutme"
        url = parseurl_class.Url(url_parse)
        self.assertEqual("info/aboutme", url.get_path())

    def test_set_path_aboutme(self):
        url_parse = "http://www.anarey.info"
        url = parseurl_class.Url(url_parse)
        url.set_path("aboutme")
        self.assertEqual("aboutme", url.get_path())

    def test_set_path_aboutme(self):
        url_parse = "www.anarey.info"
        url = parseurl_class.Url(url_parse)
        url.set_path("aboutme/aa")
        self.assertEqual("aboutme/aa", url.get_path())
    
    def test_set_path_aboutme(self):
        url_parse = "http://"
        url = parseurl_class.Url(url_parse)
        url.set_path("aboutme/aa")
        self.assertEqual("", url.get_path())

class test_parse_url(unittest.TestCase):
    def test_return_value(self):
        url_parse = "http://www.anarey.info/index.html"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "http")
        self.assertEqual(site, "www.anarey.info")
        self.assertEqual(path, "index.html")

    def test_parse_url_notequal(self):
        url_parse = "https://www.flickr.com/photo/anarey/"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertNotEqual(protocol, "http")
        self.assertNotEqual(site, "www.anarey.info")
        self.assertNotEqual(path, "index.html")

    def test_parse_url_twitter(self):
        url_parse = "ftp://www.twitter.com/anarb/index.html"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "ftp")
        self.assertEqual(site, "www.twitter.com")
        self.assertEqual(path, "anarb/index.html")
    
    def test_parse_url_not_protocol(self):
        url_parse = "www.twitter.com/anarb/index.html"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "")
        self.assertEqual(site, "www.twitter.com")
        self.assertEqual(path, "anarb/index.html")

    def test_parse_url_not_path(self):
        url_parse = "http://www.twitter.com"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "http")
        self.assertEqual(site, "www.twitter.com")
        self.assertEqual(path, "")

    def test_parse_url_not_site(self):
        url_parse = "http://"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "http")
        self.assertEqual(site, "")
        self.assertEqual(path, "")

    def test_parse_not_url(self):
        url_parse = "na%243f"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        
        self.assertEqual(protocol, "")
        self.assertEqual(site, "")
        self.assertEqual(path, "")

    def test_parse_not_url_2(self):
        url_parse = "ssefd/index.html"
        url = parseurl_class.Url(url_parse)
        protocol, site, path = url.parse_url()
        self.assertEqual(protocol, "")
        self.assertEqual(site, "")
        self.assertEqual(path, "")
