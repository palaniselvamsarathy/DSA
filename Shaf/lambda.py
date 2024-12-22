list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = list1[4:]
# new_Arr = list(map(lambda value: value-5,list1))
new_Arr = list(filter(lambda value: value>40,list1))

print(new_Arr)
# print(list2)

# arr = [1,2,3,4,5]

# for i in arr:
#     print(i)