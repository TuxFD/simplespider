from myconf.config import FILENAME_SELENIUM, FILENAME_BASH_JOB

FILE_HEADER = "#!/bin/sh\n"
FUNC_1 = "python3 myscripts/erasefile.py;\n"
FUNC_2 = 'scrapy crawl SimpleSpiderV3_2 -a start_url="STARTURL_PLACEHOLDER" maxpage="MAXPAGE_PLACEHOLDER" -o files/raw/output_COUNTER_PLACEHOLDER.csv:csv --logfile files/temp/scrapy_output_COUNTER_PLACEHOLDER.log'
FUNC_3 = "python3 myscripts/prettyfile.py;\n"
SEPARATOR = " & "
END_OF_LINE = " && fg;\n"
STARTURL_PLACEHOLDER = "STARTURL_PLACEHOLDER"
MAXPAGE_PLACEHOLDER = "MAXPAGE_PLACEHOLDER"
COUNTER_PLACEHOLDER = "COUNTER_PLACEHOLDER"


def modify_func(i, items):
    maxpage = items[0]
    url = items[1]
    func = (
        FUNC_2.replace(STARTURL_PLACEHOLDER, url)
        .replace(MAXPAGE_PLACEHOLDER, maxpage)
        .replace(COUNTER_PLACEHOLDER, str(i))
    )
    return func


def bash_generator():

    with open(FILENAME_SELENIUM, "r") as fr:
        urls = fr.readlines()

    i = 1
    maxlen = len(urls)
    print(maxlen)

    with open(FILENAME_BASH_JOB, "w+") as fb:

        fb.write(FILE_HEADER)
        fb.write(FUNC_1)

        func_2 = ""

        for url in urls:
            items = url.split(" ")  # item[0] = maxpage, item[1] = url

            if i == 1:
                func = modify_func(i, items)
                func_2 = func + SEPARATOR
                continue

            func = modify_func(i, items)
            func_2 = func_2 + func

            if i == maxlen:
                func_2 = func_2 + END_OF_LINE
                break

            i += 1

        fb.write(func_2)

        fb.write(FUNC_3)
    print("Success, bash job generated:", FILENAME_BASH_JOB)


if __name__ == "__main__":
    bash_generator()
