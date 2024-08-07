from myconf.config import (
    DOMAIN,
    SORTING,
    CATEGORIES_FULL,
    FILENAME_FULLSITE_URLS
)


def urls_generator():
    with open(FILENAME_FULLSITE_URLS, "w+") as f:
        for category in CATEGORIES_FULL:
            url = DOMAIN + category + SORTING + "1\n"
            f.write(url)
    f.close()
    print("Success. Urls updated: ", FILENAME_FULLSITE_URLS)


if __name__ == "__main__":
    urls_generator()
