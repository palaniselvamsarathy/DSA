numbers = [1,2,3,4,5,6,7,8,9,10]

num1 = list(filter(lambda x: x%2==0,numbers))
num2 = list(map(lambda x: x*3,numbers))

print(num1)
print(num2)