jon_snow=["JOn Snow",30,2.3564]
print(jon_snow)
print(jon_snow[1])
print(len(jon_snow))

num_seq=range(0,100,4)
num_list=list(num_seq)
print(num_list)

world_cup_winner=[[2006,"Italy"],[2010,"Spain"]]
print(world_cup_winner)

print(world_cup_winner[1])
print(world_cup_winner[1][1])
print(world_cup_winner[1][1][0])

part_A=[1,2,3,4,5]
part_B=[6,7,8,9,10]
merge_list=part_A+part_B
print(merge_list)
part_A.extend(part_B)
print(part_A)

world_cup_winner.append([2014,"Germany"])
print(world_cup_winner)

rank=[1,2,3,4]
last_rank=rank.pop()
print(last_rank)
print(rank)
rank.remove(2)
print(rank)

print(world_cup_winner.index([2006,"Italy"]))
world_cup_winner.sort()
print(world_cup_winner)

num_new=[n*2 for n in num_list if n%4!=0]
print(num_new)

list_1=[30,50,110,40,15,75]
list_2=[10,60,20,50]

sum_list=[(n1,n2) for n1 in list_1 for n2 in list_2 if n1+n2>100]
print(sum_list)