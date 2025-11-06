import csv


# The newline='' argument added to the open function protects us from incorrect interpretation of the newline character on different platforms.
with open("data/contacts.csv", newline="") as csvfile:
    # The second argument can be omitted if our file uses the default separator, which is a comma - we've added it to show you how to specify other separators.
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(",".join(row))

with open("data/contacts.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Name"], ":", row["Phone"])

with open("data/contacts_without_fieldnames.csv") as csvfile:
    # If your file doesn't have a header, you must define it using the fieldnames argument.
    fieldnames = ["Name", "Phone"]
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row["Name"], ":", row["Phone"])
