def two_sum_hash_table(A, target):
  ht = dict()
  for i in range(len(A)):
    if target-A[i] in ht:
      print(target-A[i], A[i])
      return True
    else:
      ht[A[i]] =1
      # print(ht)
  return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A,target))


name="Kushagra"
name1='..'.join(name)
print(name1)

