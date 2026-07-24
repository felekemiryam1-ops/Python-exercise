name = input("What is your name?").strip() .title()
age  = input("How old are you?")
hometown = input("What is your home town?")
print(f"My name is {name} 'I'm {age} My home town is {hometown}")

sibling = int(input("How many sibilings do you have?"))
print(sibling)

birthday = 23
(birthday + 1)



text = "miryam"
print(type(text))
whole_number = int(5)
decimal = float(5.4)


#Exercise 5 – Mini Profile
name = input("What is ur name?")
country = input ("Where are you from?")
Dream_Job = input("What is your dream job?")
print(f"My name is {name}, I'm from {country} ,and my dream job is {Dream_Job}")

#Exercise 6 – Simple Calculator
x = int(input("type numbers"))
y = int(input ("type number"))
print(x + y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)


#Exercise 7 – Name Formatter

name = input("What is your full name? ")

print("Original:", name)
print("Stripped:", name.strip())
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())

#Exercise 8 – Split the Name

name = input("What is your full name?")
first, last = name.split()

#Exercise 9 – Shopping Receipt
item = input("What is ur item name?")
price = float(input("What is the price?"))
print(f"item name is", {item} , "and the price is"{price})

#Exercise 10 – Temperature Converter
temperature = int(input("Write the temperature in Celsius"))
#F=(temp*1.8)+32
x = 1.8
print (f"the temperature in farhenite is {(temperature * x)+32}" )

#Exercise 12 – Return Practice
def main():
    x = int(input("write a number"))
    result = multiplier(x)
    print(result)

def multiplier(x):
    return x* 2

main()

#Exercise 13 – Return Two Values
def main():
    name = input("What is your full name?")
    first , last = namesplitter(name)
    print (first)
    print(last)

    
def namesplitter(name):
    first,last = name.split()


    return first,last
main()

#Exercise 14 – Build a User Card
name= input("What is your name?" )
Age= int(input ("How old are you?"))
City = input("City you live?")
Fav_food = input("What is your fav food?")
print(f"name= {name}\n Age = {Age}\n City={City}\n Fav food = {Fav_food}\n")

print(type(name))
print(type(Age))
print(type(City))
print(type(Fav_food))

print(Age + 5)
            