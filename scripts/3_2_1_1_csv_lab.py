import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name


class Phone:
    def __init__(self, producer):
        self.producer = producer
        self.contacts = []

    def load_contacts_from_csv(self, csv_file_name_):
        with open(csv_file_name_) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.contacts.append(PhoneContact(row["Name"], row["Phone"]))

    def search_contact(self):
        phrase = (input("Search contact: ")).casefold()
        contacts_founded = []
        for contact in self.contacts:
            for value in contact.__dict__.values():
                if phrase in value.casefold():
                    contacts_founded.append(contact)
                    break
        if contacts_founded:
            for contact in contacts_founded:
                print("{} ({})".format(contact.name, contact.phone))
        else:
            print("No contacts found")


csv_file_name = "data/contacts.csv"
my_phone = Phone("samsung")
my_phone.load_contacts_from_csv(csv_file_name)
my_phone.search_contact()  # 'mother'
my_phone.search_contact()  # '103'
my_phone.search_contact()  # 'brother'
