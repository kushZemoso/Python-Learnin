my_string="Hello"

def exclamation(my_string):
    my_string="!!"+my_string+"!!"
    return  my_string

my_string=exclamation(my_string)
print(my_string)

n=50
num_list=[10,4,23,6,18,27,47]

for num1 in num_list:
    print()
    print(num1)
    for num2 in num_list:
        print(num2,end=" ")

        if num1+num2==n:
         print(num1,num2)



