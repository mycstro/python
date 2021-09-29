"""write info out to a text file - how to do this is in code academy at the end (input/output)
also probably create an address book class which saves all the info and has a "write to file" method
that writes the address to the file.
if has another method which can search the file and return an address if given a name or address or phone etc
global variables may help?"""

name = input("What would you like to call your address book?")+".txt"
c = open(name, "a")
print (open(name, "a"))


def main_menu():
    # This initiates the address books and allows users to select which feature to use
    choice = input("Press 1 to view your contacts, 2 to enter a new contact and 3 to search your contacts")
    if choice == "1":
        c = open(name, "r")
        file_contents = c.read()
        print (file_contents)
        c.close
    elif choice == "2":
        enter_contacts()
        main_menu()
    elif choice == "3":
        search_contacts()
        main_menu()

def search_contacts():
    # Searches contact list
    choice = input("Search for a contact by any kind of information: ")
    print(choice)
    # c = []
    # c = list(choice)
    # for line in range(0, len(list)):
    #     if choice in line:
    #         print (line)
    #     else:
    #         choice = input("There's no one named " + choice + " in your contact list. Press 2 to enter them now")
    #         if choice == "2":
    #             enter_contacts()
    #         else:
    #             print ("Please choose an item from the menu")


def clean_first():
    # Ensures that the first name of a user is capitalized
    # Ensures that only legal names are accepted in this field
    one = input("First name ")
    f = one[1:10]
    g = one[0]
    return g.upper() + f


def clean_last():
    # Ensures that the first name of a user is capitalized
    # Ensures that only legal names are accepted in this field
    two = input("Last name ")
    a = two[1:10]
    b = two[0]
    return b.upper() + a


def clean_phone():
    # Takes a 10 digit input and presents it in the [(###) ###-####] format
    # Avoids mistakes & stupidity surrounding 10-digit phone numbers
    phone = input('Phone number with area code ')
    if (len(phone) == 10) and phone[0:len(phone)] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
        telephone = "1 " + "(" + phone[0:3] + ")" + " " + phone[3:6] + "-" + phone[6:10]
    else:
        telephone = "Only numerals are accepted in this field"
    return telephone


def clean_media():
    # Presents a contact's social media in a clean manner, with an @ symbol
    # Avoids
    media = input('Social media ')
    if 15 >= len(media) - 1:
        social = "@" + media
    else:
        social = "Social media handles must be 15 characters or less"
    return social


def clean_mail():
    # Ensures that an email is valid before allowing a user to assign it to a contact
    addie = input('E-mail ')
    return addie


def enter_contacts():
    # Collects contact info
    # Saves contact info to a list
    f = clean_first()
    last = clean_last()
    telephone = clean_phone()
    email = clean_mail()
    addie = input('Address ')
    social = clean_media()
    contact = ("[" + f + " " + last + "|" + telephone + "," + email + "|" + addie + " " + social + "]")
    with open(name, "a") as text_file:
        text_file.write(contact)
    print ("The contact " + contact + " has been added to your address book")

main_menu()