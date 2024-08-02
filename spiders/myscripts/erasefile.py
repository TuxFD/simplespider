def erasefile():
    # filename = "../spiders/files/raw/output.csv"
    filename = "files/raw/output.csv"
    f = open(filename, "w+")
    f.close()
    print("Success")


if __name__ == "__main__":
    erasefile()
