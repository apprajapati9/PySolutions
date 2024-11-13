import re #regular expressions

#Format for correct phone number 333-112-3333
#Without using RegEx.
def is_phone_number(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False  #No area code.

        if text[3] != '-':
            return False  #No - delimiter after 3 digits

        for i in range(4,7):
            if not text[i].isdecimal():
                return False  #no first 3 digits

        if text[7] != '-':
            return False

        for i in range(8,12):
            if not text[i].isdecimal():
                return False  #no first 3 digits

        return True


#With regex makes code much concise and readable.
def is_phone_number_with_regex(text):
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phone_numbers = phone_regex.search(text) #search returns only 1
    #findall returns all occurrences.
    all_numbers = phone_regex.findall(text)
    return all_numbers


print(is_phone_number("111-111-0111"))
print(is_phone_number("111-111--111"))

message = "Call me at 333-322-2333 tomorrow, or at 999-122-1222"
foundNumber = False

for i in range(len(message)):
    if i.is_integer():
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print("phone number found: "+ chunk)
            foundNumber = True
if not foundNumber:
    print("Couldn't find any phone numbers")

print(is_phone_number_with_regex(message))