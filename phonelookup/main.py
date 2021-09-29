# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import phonenumbers
from phonenumbers import carrier, carrierdata, geocoder, parse, timezone

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def search_number(number):
    # Parsing String to Phone number
    searchNumber = phonenumbers.parse(number)
    # Pass the parsed phone number in below function
    searchTimeZone = timezone.time_zones_for_number(searchNumber)
    # Getting carrier of a phone number
    searchCarrier = carrier.name_for_number(searchNumber, 'en')
    # Getting region information
    searchRegion = geocoder.description_for_number(searchNumber, 'en')
    return(searchNumber, searchTimeZone, searchCarrier, searchRegion)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Mycstro')
    numberInfo = search_number(19712930170)
    print(numberInfo)
    #search_number(19712930170)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
