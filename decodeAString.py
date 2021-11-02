print(" ------------------------------------------------")
print("|                                                |")
print("|    10EncodeAString                             |")
print("|    Name : Rex Woods                            |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
string = input("What is your string? ")
encoded_message = ""
for element in string:
    encoded_element = chr(ord(element)-1)
    encoded_message += encoded_element
print(encoded_message)
