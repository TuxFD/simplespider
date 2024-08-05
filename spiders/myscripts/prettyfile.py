DEFAULT_FILENAME = "../spiders/files/raw/output.csv"
IN_STOCK_FALSE = "Bitte wenden Sie sich an Ihren zuständigen M&S Vertriebsmitarbeiter"
IN_STOCK_TRUE = "Auf Lager."

def prettyfile():
    filename_raw = DEFAULT_FILENAME
    filename_cooked = DEFAULT_FILENAME.replace("/raw/", "/cooked/")

    lines = []
    no_headers = True

    with open(filename_raw, "r") as fr:
        lines = fr.readlines()

    with open(filename_cooked, "w+") as fc:
        for line in lines:

            if no_headers:
                fc.write(line)
                no_headers = False
                continue

            newline = (
                line.replace("  ", "")
                .replace("Katalogpreis: ", "")
                .replace(",https", " ,https")
                .replace(',"\n', ',"')
                .replace("Derzeit nicht auf Lager.,\n", "")
                .replace(IN_STOCK_TRUE, "Да")
                .replace(IN_STOCK_FALSE, 'Нет')
            )
            fc.write(newline)

    print("Success. File prettified: ", filename_cooked)


if __name__ == "__main__":
    prettyfile()
