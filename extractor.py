import urllib2
import json
from bs4 import BeautifulSoup


class Extractor:
    def get_data(self, source):
        try:
            page = urllib2.urlopen(source)
        except urllib2.HTTPError:
            return  # we have no guaranties that some specific page exists so if it was not found then just skip it

        data = page.read()

        page.close()

        return data

    def get_soup(self, source):
        data = self.get_data(source)

        if data:
            return BeautifulSoup(data, 'html.parser')
        else:
            return None

    def get_json(self, source):
        data = self.get_data(source)

        if data:
            return json.loads(data)
        else:
            return None

    def extract():
        raise Exception('Extract method should be implemented in ancestors!')
