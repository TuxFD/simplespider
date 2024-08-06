DEFAULT_FILENAME = "../spiders/files/raw/output.csv"


def erasefile(filename=DEFAULT_FILENAME):

    f = open(filename, "w+")
    f.close()
    print("Success. File erazed: ", filename)


if __name__ == "__main__":
    erasefile()
