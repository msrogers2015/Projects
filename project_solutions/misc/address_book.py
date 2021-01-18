import sqlite3 as sl3
import os

class AddressBook:
    def __init__(self, db):
        # Variables
        action = None
        self.db = db

        try:
            conn = sl3.connect(self.db)
            c = conn.cursor()
        except Exception as e:
            print(e)
        finally:
            c.close()
            conn.close()
        self.startup()

    
    def startup(self):
        os.system('cls')
        print('Welcome to a CLI addressbook. What would you like to do?')
        action = input('Add Entry\nEdit Entry\nDelete Entry\n').lower()
        if action != None:
            os.system('cls')
            if action == "add entry" or action == "add":
                self.add("","","","","","","","","")
            if action = "edit entry" or action == 'edit':
                self.edit()
            if action = "delete entry" or action == 'delete':
                self.delete()


    def add(self, fname, lname, phone, email, address1, address2, city, state, zipcode):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode

        os.system('cls')
        fname = input('Please enter first name:')

        os.system('cls')
        lname = input('Please enter last name:')

        os.system('cls')
        while True:
            phone = input('Please enter phone number(10 digits numbers only):')
            if phone.isdigit() and len(phone) == 10:
                break
            else:
                os.system('cls')
                print('Sorry, invalid format. Please try again')
                phone = input('Please enter phone number(5558881111):')

        os.system('cls')    
        email = input('Please enter email:')

        os.system('cls')
        address1 = input('Please enter address line 1:')

        os.system('cls')
        address2 = input('Please enter address line 2:')

        os.system('cls')
        city = input('Please enter city:')

        os.system('cls')
        state = input('Please enter state:')

        os.system('cls')
        zipcode = input('Please enter zipcode:')


    def edit(self):
        pass


    def delete(self):
        pass


if __name__ == "__main__":
    app = AddressBook('addressbook.db')
