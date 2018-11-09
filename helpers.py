import csv

def load_domains(file_name, ignore_header=True):
    result = []

    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result.append(row[0])

    if ignore_header:
        result = result[1:]

    return result

# make https://benoit.fashion/products/bedsm-printed-basic-blackt-shirt
# from https://benoit.fashion/products/bedsm-printed-basic-blackt-shirt?view=quick
def remove_arguments_from_url(url):
    return url.split('?')[0]
