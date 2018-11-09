import time
from helpers import load_domains
from contacts_extractor import ContactsExtractor
from products_extractor import ProductsExtractor

domains = load_domains('stores.csv')
domain_example = 'dollardiscountclub.myshopify.com'

print("--- start ---")
start_time = time.time()

for d in domains:
    print('Domain: ',d)

    ce = ContactsExtractor(d)
    contacts = ce.extract()
    print(contacts)

    pe = ProductsExtractor(d)
    products = pe.extract()
    print(products)

# ce = ContactsExtractor(domain_example)
# contacts = ce.extract()
# print(contacts)

# pe = ProductsExtractor(domain_example)
# products = pe.extract()
# print(products)

print("--- %s seconds ---" % (time.time() - start_time))
