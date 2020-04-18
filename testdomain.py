from urllib.parse import urlparse

def get_domain_name(url):
    try:
        result = get_sub_domain_name(url).split('.')
        return result[1]

    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

name = get_domain_name('https://careerhigh.in/')
print(name)
