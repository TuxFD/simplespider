from myconf.config import DOMAIN, SORTING, CATEGORIES


def urls_generator():
    start_urls = []
    for category in CATEGORIES:
        start_urls.append(DOMAIN + category + SORTING + "1")
    for url in start_urls:
        print(url)


if __name__ == "__main__":
    urls_generator()
