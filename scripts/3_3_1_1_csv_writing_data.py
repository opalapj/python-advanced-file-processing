import csv


with open("data/exported_contacts.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")

    writer.writerow(["Name", "Phone"])
    writer.writerow(["mother", "222-555-101"])
    writer.writerow(["father", "222-555-102"])
    writer.writerow(["wife", "222-555-103"])
    writer.writerow(["mother-in-law", "222-555-104"])

# Situation where you add a contact containing the separator used to separate the values in the CSV file.
with open("data/exported_contacts.csv", "w", newline="") as csvfile:
    writer = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    writer.writerow(["Name", "Phone"])
    writer.writerow(["grandmother, grandfather", "222-555-105"])
# The code will save the following data to the data/exported_contacts.csv file:
# Name,Phone
# "grandmother, grandfather and auntie",222-555-105
# Presence of quotes can be checked in .txt file or during import data in .xmls file.

with open("data/exported_contacts.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Phone"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Name": "mother", "Phone": "222-555-101"})
    writer.writerow({"Name": "father", "Phone": "222-555-102"})
    writer.writerow({"Name": "wife", "Phone": "222-555-103"})
    writer.writerow({"Name": "mother-in-law", "Phone": "222-555-104"})
    writer.writerow({"Name": "grandmother, grandfather", "Phone": "222-555-105"})
