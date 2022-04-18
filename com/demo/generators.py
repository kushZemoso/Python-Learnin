# without using generators
def square_number(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result

my_nums=square_number([1,2,3,4,5])

print(my_nums)


def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums=square_numbers([5,4,3,2,1])

for num in my_nums:
    print(num)


my_nums=[x*x for x in [1,2,3,4,5]]