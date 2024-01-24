import random
print('as number of digits:')
a=int (input())
su=0
for b in range (a) :
    c =random.randint(1,228)
    print(c) 
    su=su+c 
print("The sum of all numbers is",su)
input("Enter to exit")