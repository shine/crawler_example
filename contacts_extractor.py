import re
from extractor import Extractor


class ContactsExtractor(Extractor):
    sources_template = ['http://<<domain>>/',
                        'http://<<domain>>/pages/about',
                        'http://<<domain>>/pages/about-us',
                        'http://<<domain>>/pages/contact',
                        'http://<<domain>>/pages/contact-us']

    def __init__(self, domain):
        self.sources = []

        for template in ContactsExtractor.sources_template:
            self.sources.append(template.replace('<<domain>>', domain))

        self.email = None
        self.facebook = None
        self.twitter = None

        self.email_re = re.compile(r'mailto')
        self.facebook_re = re.compile(r'facebook\.com')
        self.twitter_re = re.compile(r'twitter\.com')

    def extract(self):
        if not self.email or not self.facebook or not self.twitter:
            self.parse_all()

        return {'email': self.email,
                'facebook': self.facebook,
                'twitter': self.twitter}

    def parse_all(self):
        for source in self.sources:
            soup = self.get_soup(source)

            if not soup:
                continue  # in cases of 'under construction' page for shop lets skip it

            self.parse_one(soup)

            if self.email and self.facebook and self.twitter:
                break  # we don't need to parse all pages if info was already found

    def parse_one(self, soup):
        if not self.email and soup.find('a', {'href': self.email_re}):
            self.email = str(soup.find('a', {'href': self.email_re})['href'].split(':')[1])

        if not self.facebook and soup.find('a', {'href': self.facebook_re}):
            self.facebook = str(soup.find('a', {'href': self.facebook_re})['href'])

        if not self.twitter and soup.find('a', {'href': self.twitter_re}):
            self.twitter = str(soup.find('a', {'href': self.twitter_re})['href'])
