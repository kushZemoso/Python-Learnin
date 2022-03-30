flt_pt=1.23
print(flt_pt)
complex1=complex(10,5)
print(complex1)
f_bool=True
print(f_bool)
got="Game Of  Thrones"
print(got)
print(len(got))
last=got[len(got)-1]
print(last)
# Negative Indexing
print(got[-2])
print(id(got))
name="Kushagra"
print(name[0:5])
print(10.2*3)
print(34.4%2.5)
num1=[2]
num2=[2]
print(num2 is num1)
print(10**2)
print(5>=3)
my_string="123456789"
print(my_string[-2:-6:-2])
x=20
y=5
print(x+True)
print(4-y*False)

num_list=[10,20,30,40]
print(num_list)

def multiply_by_10(my_list):
    my_list[0] +=10
    my_list[1] += 10
    my_list[2] += 10
    my_list[3] += 10

multiply_by_10(num_list)
print(num_list)

string1="Learn Python {version} at {cname}".format(version=3,cname="Educative")
print(string1)

# How to creatye lambdas in python
triple=lambda num:num*3
print(triple(10))

my_func=lambda num:"High"if num>50 else "Low"
print(my_func(30))

def calculator(operation,n1,n2):
    return operation(n1,n2)

result=calculator(lambda n1,n2:n1*n2,10,20)
print(result)

# USing map and filter
num_list=[10,-2,45,67,82]
double_list=list(map(lambda n:n*2,num_list))
print(double_list)
greater_then_10=list(filter(lambda n:n>10,num_list))
print(greater_then_10)