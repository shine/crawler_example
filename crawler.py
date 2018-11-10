from csv import DictWriter
from helpers import load_domains
from contacts_extractor import ContactsExtractor
from products_extractor import ProductsExtractor

domains = load_domains('stores.csv')


def parse_domain(d):
    result = {'url': None, 'email': None, 'facebook': None, 'twitter': None,
              'title 1': None, 'image 1': None, 'title 2': None, 'image 2': None,
              'title 3': None, 'image 3': None, 'title 4': None, 'image 4': None,
              'title 5': None, 'image 5': None}
    result['url'] = unicode(d).encode("utf-8")

    contacts = ContactsExtractor(d).extract()
    result['email'] = unicode(contacts['email']).encode("utf-8")
    result['facebook'] = unicode(contacts['facebook']).encode("utf-8")
    result['twitter'] = unicode(contacts['twitter']).encode("utf-8")

    products = ProductsExtractor(d).extract()
    for idx, product in enumerate(products):
        result['title '+str(idx+1)], result['image '+str(idx+1)] = unicode(products[idx]['title']).encode("utf-8"), unicode(products[idx]['image']).encode("utf-8")

    return result


result = []

for domain in domains:
    result.append(parse_domain(domain))

with open('output.csv', 'wb') as f:
    w = DictWriter(f, ['url', 'email',
                       'facebook', 'twitter',
                       'title 1', 'image 1',
                       'title 2', 'image 2',
                       'title 3', 'image 3',
                       'title 4', 'image 4',
                       'title 5', 'image 5'])
    w.writeheader()
    w.writerows(result)
