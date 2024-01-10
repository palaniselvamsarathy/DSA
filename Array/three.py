# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

n = int(input("Enter Max Number:"))

a=[]

for i in range(n):
    if i%2!=0:
        a.append(i)

print(a)
    