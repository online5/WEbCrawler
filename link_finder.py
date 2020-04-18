from html.parser import HTMLParser
from urllib import parse # To parse the html file
class LinkFinder(HTMLParser):
    """docstring for LinkFinder.
    It returns the links that spiders have crawled though the internet

    """
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
       if tag == 'a':
           for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links;
