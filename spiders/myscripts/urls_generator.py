DOMAIN = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="

CATEGORIES = [
    # "Rohrverbindungen/",
    "Rohrverbindungen/Verschraubungen/",
    "Rohrverbindungen/Flanschverbindungen/",
    "Rohrverbindungen/Clampverbindungen/",
    "Rohrverbindungen/Schlauchverbindungen/",
    "Rohrverbindungen/Industriefittings/",
]


start_urls = []


def urls_generator():
    for category in CATEGORIES:
        start_urls.append(DOMAIN + category + SORTING + "1")
    for url in start_urls:
        print(url)
    ...


if __name__ == "__main__":
    urls_generator()
