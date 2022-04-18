# a-z only conatins lower case letter
# 0-9 can conation digits b/w 0 to 9
# . _ must be only 1 before domain
# @ only 1 in email
# . 2,3 pos from last

# sample email-kush1207@gmail.com

import re
# starting with letter
email_condition="^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enetr your Email:")

if re.search(email_condition,user_email):
    print("Valid Email {}".format(user_email))
else:
    print("InValid Email")