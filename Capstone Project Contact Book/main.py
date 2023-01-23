# Create contact.txt file
import datetime
class ContactBook:
    while True:
        from datetime import date
        filename = str("contactbook_" + str((date.today()).strftime("%d-%m-%Y")) + ".csv")
        # take input from user upon his need
        selection = input ('to Create: enter (C) \nto Delete: enter (D) \nto update: Enter (U) \nto Quit: Enter (Q) \nyour answer is:' )
        if selection == 'C':
        #create contact
            with open(filename, 'a') as f:
                name = input ('please enter your name: ')
                phone_no = input ('please enter your phone number: ')
                email = input ('please enter your email: ')
                adress = input ('please enter your address: ')
                insertion_Date = (date.today()).strftime("%d/%m/%Y")
                f.writelines((name,':',phone_no,':',name,':',phone_no,':', insertion_Date,'\n'))
        elif selection == 'U':
            # take the new input to replace the old one
            old_contact = input('Enter the old (Name,Phone,Email,Address):')
            new_contact = input('Enter the new (Name,Phone,Email,Address):')
            with open(filename, 'r') as f:
                newline = []
                file = f.readlines()
                for word in file:
                    newline.append(word.replace(old_contact, new_contact))
            with open(filename, "w") as f:
                for line in newline:
                    f.writelines(line)
        elif selection == 'D':
            # take contact input to delete the record
            delete_contact = input("Delete:")
            with open(filename, 'r') as f:
                file = f.readlines()
            with open(filename, "w") as f:
                for line in file:
                    if not line.strip("\n").startswith(delete_contact):
                        f.write(line)
            # exit the loop
        else:
            break