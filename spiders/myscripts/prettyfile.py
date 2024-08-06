from myconf.config import (
    DEFAULT_FILENAME_PRETTYFILE,
    HEADERS,
    FILENAME_SUMMARY,
    IN_STOCK_TRUE,
    IN_STOCK_FALSE,
)


def prettyfile():
    filename_cooked = FILENAME_SUMMARY
    f = open(filename_cooked, "w+")
    f.close()

    no_headers = True

    for filename_raw in DEFAULT_FILENAME_PRETTYFILE:

        lines = []
        headers = True

        with open(filename_raw, "r") as fr:
            lines = fr.readlines()

        with open(filename_cooked, "a") as fc:
            if no_headers:
                fc.write(HEADERS)
                no_headers = False

            for line in lines:

                if headers:
                    headers = False
                    continue

                newline = (
                    line.replace("  ", "")
                    .replace("Katalogpreis: ", "")
                    .replace(",https", " ,https")
                    .replace(',"\n', ',"')
                    .replace("Derzeit nicht auf Lager.,\n", "")
                    .replace(IN_STOCK_TRUE, "Да")
                    .replace(IN_STOCK_FALSE, "Нет")
                )
                fc.write(newline)

        print("Success. File prettified: ", filename_cooked)


if __name__ == "__main__":
    prettyfile()
