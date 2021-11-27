# class Contacts:
#
#     all_contacts = []
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contacts.all_contacts.append(self)
#
#     def display(self):
#         print(self.__dict__)
#
# def main():
#     c1 = Contacts('Rohith', 'rohith@gmail.com')
#     c2 = Contacts('Manish', 'manish@gmail.com')
#     print(Contacts.all_contacts)
#
# if __name__ == '__main__':
#     main()

# class Contacts:
#
#     all_contacts = []
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contacts.all_contacts.append(self)
#
#     def display(self):
#         print(self.__dict__)
#
# def main():
#     c1 = Contacts('Rohith', 'rohith@gmail.com')
#     c2 = Contacts('Manish', 'manish@gmail.com')
#
#     # print(Contacts.all_contacts)
#
#     for i in Contacts.all_contacts:
#         i.display()
#
#     # Contacts.all_contacts.display_all_contacts()
#
#     name = 'Rohith'
#     for i in Contacts.all_contacts:
#         if i.name == name:
#             print('Contact Found')
#
# if __name__ == '__main__':
#     main()

class ContactList(list):

    def display_all_contacts(self):
        for i in self:
            i.display()

    def search_contact(self,name):
        for i in self:
            if i.name == name:
                return 'Contact Found'
        return 'Contact Not Found'


class Contacts:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)

    def display(self):
        print(self.__dict__)

def main():
    c1 = Contacts('Rohith', 'rohith@gmail.com')
    c2 = Contacts('Manish', 'manish@gmail.com')

    Contacts.all_contacts.display_all_contacts()
    print(Contacts.all_contacts.search_contact('Rohith'))

if __name__ == '__main__':
    main()