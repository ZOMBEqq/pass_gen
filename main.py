from random import choice

all_number = "1234567890"   
all_sogl = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
all_glas = "eyuioaEYUIA"
password = ""
for i in range(5):
    password += choice(all_sogl) + choice(all_glas)
for i in range(3):
    password += choice(all_number) 
print(password)