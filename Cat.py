#while is for loop 
"""i=3"""
"""while i !=0:
    print("Meow")
    i= i-1"""

"""i = 0

while i<3:
    print("meow")
    i=1+1 #or i+=1


for i in[0,1,2]:
    print("meow")

for i in range(3): #im not using the virable so just bc i fdon't use it we name it _
    print("meow")


print("meow/n" *3, end="")"""
while True:
    n = int(input("What is n?"))
    if n>0:
        break

for _ in range(n):
    print("meow")


"""def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()"""

def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("What is n?"))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()