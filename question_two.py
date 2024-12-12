
list = [4,7,2,9,12,15]
new_list = [num for num in list if num % 2 ==1]
print(new_list)


sum = 0
for num in new_list:
  sum +=num
print(sum)
