#### 
import unittest 

def get_protocol(url):
    if url.startswith("http"):
        return "http"
    elif url.startswith("ftp"):
        return "ftp"
    return ""

class test_parseurl(unittest.TestCase):
    def test_protocol_http(self):
        protocol = get_protocol("http://www.site.com")
        self.assertEqual("http", protocol)

    def test_protocol_not_http(self):
        protocol = get_protocol("ftp://www.site.com")
        self.assertNotEqual("http", protocol)

    def test_protocol_ftp(self):
        protocol = get_protocol("ftp://www.site.com")
        self.assertEqual("ftp", protocol)
