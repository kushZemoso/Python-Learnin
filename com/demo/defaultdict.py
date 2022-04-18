from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')
print(words)
reg_dict = defaultdict(int)
for word in words:
  reg_dict[word] += 1
print(reg_dict)