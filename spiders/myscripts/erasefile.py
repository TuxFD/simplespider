from myconf.config import DEFAULT_FILENAME_ERASE


def erasefile():
    for filename in DEFAULT_FILENAME_ERASE:
        f = open(filename, "w+")
        f.close()
        print("Success. File erazed: ", filename)


if __name__ == "__main__":
    erasefile()
