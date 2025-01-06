import csv


def read(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if "computer" in row[1].lower():
                print(row)


read("students.csv")
