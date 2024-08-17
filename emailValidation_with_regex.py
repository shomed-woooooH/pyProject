#
import re
email_condition = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$' 
userEmail = input("enter your email :")

if re.search(email_condition,userEmail):
    print("Valid email")
else:
    print('Invalid email')

    