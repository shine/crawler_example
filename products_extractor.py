import re
from helpers import remove_arguments_from_url
from extractor import Extractor

class ProductsExtractor(Extractor):
    products_page_url_template = 'http://<<domain>>/collections/all'

    def __init__(self, domain):
        self.domain = domain
        self.products_page_url_template = ProductsExtractor.products_page_url_template.replace('<<domain>>', domain)

        self.product_url_re = re.compile(r'^/products/')
        self.product_alternative_url_re = re.compile(r'^/collections/all/products/')

        self.links_to_products = []
        self.products = []

    def get_links_to_products(self, number_of_products=5):
        if not self.links_to_products:
            self.parse_links_to_products(number_of_products)
        
        return self.links_to_products

    def parse_links_to_products(self, number_of_products=5):
        soup = self.get_soup(self.products_page_url_template)

        if not soup: # in cases of 'under construction' page for shop lets skip it
            return

        local_links = soup.find_all('a', {'href': self.product_url_re}) + soup.find_all('a', {'href': self.product_alternative_url_re})

        for link in local_links[:number_of_products]:
            self.links_to_products.append('http://'+self.domain+remove_arguments_from_url(link['href'].encode('utf-8')))

    def extract(self):
        if not self.products:
            self.parse_all()
        
        return self.products

    def parse_all(self):
        links_to_products = self.get_links_to_products()

        for link in links_to_products:
            product_info = self.parse_one(link)

            if product_info:
                self.products.append(product_info)

    def parse_one(self, link):
        json = self.get_json(link+'.json')

        if not json:
            return None

        if not json['product']['image']:
            image = None
        else:
            image = json['product']['image']['src']

        return {'image': image, 'title': json['product']['title']}
