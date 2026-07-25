#Exercise 1 – Positive, Negative, or Zero
"""number=int(input("is the number greater than zero?"))
if number>0:
    print("positive")
elif number<0:
    print("Negative")
else:
    print("Zero") """

#Exercise 2 – Even or Odd
"""number = int(input("write a number"))
if number%2==0:
    print("Even")
else:
    print("Odd")"""

#Exercise 3 – Age Checker

"""age=int(input("how old are you?"))
if age <13:
    print("Child")
elif 13 <=age <= 19:
    print("Teenager")
else:
    print("Adult")"""

#Exercise 4 – Password Checker
"""password = input("Type password")
correct_password="Python123"

if password== correct_password:
    print("Access Granted")
else:
    print("Accsess Denied")"""

#Exercise 5 – Weather Advisor

"""Q1= (input("Is it raining? (yes/no)"))
Q2= (input("is it snowing (/yes/no)?"))

if Q1 =="yes" or Q2 == "yes":
    print("Take umbrella or wear warm clothes")
else:
    print("Enjoy the weather")"""

#or bool(input("Is it snowing?"))

"""Q1=input("Ist saturday? yes/ no")
Q2= input ("Is is sunaday yes/no")

if Q1== "yes" or Q2=="yes":
    print("weekend")
else:
    print("study")"""


#Exercise 6 – Login System

"""username= input("Type ur username")
correct_username= "admin"
password= input("Type ur password")

correct_password="python" 
if username == correct_username and password ==correct_password:
 print("Log in succesful")
else:
 print("failed")"""


#Exercise 7 – Number Guess

"""n=int(input("Guess the number"))
secret = 15

if n != secret:
 print("wrong guess")
else:
 print("Correct")"""


#Exercise 8 – Smallest Number

"""Q1=int((input("type a number")))
Q2=int((input("type a n")))
Q3=int((input("type a n")))

if Q1 < Q2 and Q1< Q3:
 print(Q1)
elif Q2< Q3 and Q2 > Q1:
 print(Q1)
else:
 print(Q3)"""


 #Exercise 9 – Grade Calculator

"""score= int(input("Student score?"))


if 90<= score <= 100:
 print("A")
elif 80 <= score <= 89 :
 print("B")
elif 70 <= score <= 79:
 print ("C")
elif 60<= score <= 69:
 print("D")
else:
 print("F")

if score >= 60 :
  print("pass")
else:
 print("Fail")"""

#Exercise 10 – FizzBuzz

for n in range(1,31):
 if n%3==0 and n%5==0:
    print("FizzBuzz")
 elif n%3==0:
    print("Fizz")
 elif n%5==0:
    print("Buzz")
 else:
    print(n)


  