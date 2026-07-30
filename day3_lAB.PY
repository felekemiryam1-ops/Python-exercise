#Exercise 1.5 — Count to 5


"""i=1

while i<=5:
    print(i)
    i=i+1"""

#Exercise 2 — Countdown

"""i=10

while i>=1:
  print(i)
  i=i-1
print("Blast off!")"""

#Exercise 3 — Print Your Name

"""name=input("What is ur name?")
counter= 1


while counter <=5:
    print(name)
    counter=counter+1"""


#Exercise 4 — Even Numbers

"""i=2


while i<=20 :
    print(i)
    i=i+2"""



#Exercise 5 — Positive Number

"""
while True:
    question = int(input("Enter a positve number"))

    if question >0:
        print("Thank you")
        break"""

#Exercise 6— Password Checker

"""while True:
    password=input("password")

    if password =="python123":
        print("Acess Granted")
        break"""

#Section 2 — For Loops
#Exercise 6 — Print 1–20

"""for n in range(1,21):
    print(n)"""

#Exercise 7 — Even Numbers (for Loops)

"""for n in range(1,21):
 if n%2==0:
   print(n)"""

"""for n in range(2,21,2):
  print(n)"""
    
#Exercise 8 — Odd Numbers

"""for n in range(1,20,2):
    print (n)"""

#Exercise 9 — Multiplication Table

"""n= int(input("type any number"))
#i=range(1,13)

for i in range(1,13):
    print(n,"*",i,"=", n*i)"""

#Exercise 10 — FizzBuzz

"""for n in range(1,31):
    if n%3==0 and n%5==0:
        print("fizzbzz")
    elif n%3==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    else:
        print(n)"""

#Exercise 11 — Secret Word
"""s="python"
while True:
    n=input("Whhat is the secret code")
    if n==s:
        print("correct")
        break"""
#Exercise 12 — Guess the Number
"""s=7
while True:
    n=int(input("Guess the number"))
    if n==s:
        print("you got it!")
        break"""
#Exercise 13 — Skip Even Numbers (continue)

"""for n in range(1,10):
    if n%2==0:
       continue
    print(n)"""
#Exercise 14 — Skip Multiples of 3

"""for n in range(1,21):
    if n%3==0:
        continue
    print(n)"""


#Exercise 15 — Skip Vowels
"""word="programming"



for letter in word:
    if letter in "aeiou":
        continue
    print(letter)"""


#Exercise 16 — Count Even Numbers

"""count=0

for n in range(1,21):
    if n%2==0:
        count=count+1
print(count)"""

#Exercise 17 — Find the Largest Number
"""numbers = [12, 7, 25, 3, 18, 9, 1, 14]

largest=numbers[0]

for n in numbers:
    if n>largest:
        largest=n


print(largest)"""

#Exercise 18 — Find the Smallest Number

"""numbers=[12, 7, 25, 3, 18, 9, 1, 14]

smallest=numbers[0]

for n in numbers:
    if n<smallest:
        smallest=n

print(smallest)"""

#Exercise 19 — Find the Total (Sum)

"""numbers = [5, 10, 15, 20, 25]

total=0

for n in numbers:
   total = total+n

   

print(total)"""

#Exercise 20 — Count Positive Numbers

"""numbers = [-3, 7, -1, 10, 0, 5, -8]
count=0

for n in numbers:
    if n>0:
        count=count+1
print(count)"""



#xercise 21 — Find the Largest Even Number

"""numbers = [11, 24, 7, 18, 35, 42, 9, 16]
largest=numbers[0]

for n in numbers:
    if n%2==0 and n>largest:
        largest=n

print(largest)"""


#Exercise 22 — Print Every Food

"""foods = ["Pizza", "Burger", "Pasta", "Rice", "Salad"]


for n in foods:
    print(n)"""


#Exercise 23 — Print the First and Last Item

"""foods = ["Pizza", "Burger", "Pasta", "Rice", "Salad"]

print(foods[0], foods[4], sep="\n")"""

#Exercise 24 — Add a New Food

"""new_food= input("Add a new food")
foods = ["Pizza", "Burger", "Pasta", "Rice", "Salad"]
foods.append(new_food)

print(foods)"""

#Exercise 25 — Remove a Food


"""foods = ["Pizza", "Burger", "Pasta", "Rice", "Salad"]
print(foods)
remove=input("remove ur desired food")
foods.remove(remove)
print(foods)"""


#Section 8 — Iterating Lists

"""skills = ["Python", "AWS", "Linux", "Docker"]

for number, skill in enumerate(skills, start=1):
    print(f"{number}. {skill}")"""


#Exercise 27 — Count the Skills
"""skills = ["Python", "AWS", "Linux", "Docker"]

print(len(skills))"""

#Exercise 28 — Create a Student Dictionary and Print Individual Values

"""dictionary={
    'name': "John",
    'age': 20,
    'grade':"A"

}

print(dictionary['name'], dictionary['age'], dictionary['grade'],sep="\n")"""

    
#Ex 30

"""name=input("name")
Age=input("Age")
City=input("City")



dictionary={
    'name': name,
    'Age': Age,
    'City': City,

}

print(dictionary)"""

#ex31

"""Students=[
{ 'name':"Miryam",
    'grade':95,},

{'name':"john",
    'grade':88,},

{'name':"Anna",
        'grade':91,}
]



for n in Students:
   print(n['name'],"-", n['grade'])"""

#ex 33

for row in range(5):
   print("*", end='')
   for column in range(4):
    print("*", end='')
        
    




















        
    



    
