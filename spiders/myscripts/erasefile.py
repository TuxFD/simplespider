def erasefile():
    # filename = "../spiders/files/raw/output.csv"
    filenames = [
        "files/raw/output_1.csv",
        "files/raw/output_2.csv",
        "files/raw/output_3.csv",
        "files/raw/output_4.csv",
        "files/raw/output_5.csv",
    ]

    for filename in filenames:
        f = open(filename, "w+")
        f.close()
        print("Success. File erazed: ", filename)


if __name__ == "__main__":
    erasefile()
