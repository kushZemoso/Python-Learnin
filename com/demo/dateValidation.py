import re

date=input("Enter the date in dd/mm/yy format:")
validDate=(3[1]|[12][0-9]|0[1-9])(1[0-2]|0[1-9])/d{4}$

# month contains 31 days or 30 days and a special month feb contains 28 days
# while in leap year feb conatins 29 days
if re.search(validDate,date):
    print("Valid Date {}".format(Date))
else:
    print("InValid Date")
