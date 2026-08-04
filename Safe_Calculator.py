def main():
    calculator("numbe?")
    


def calculator(prompt):
  while True:
    try:
       x = int(input(prompt))
        
       while True:
            c = input("choose an operator(+, - , * , /)")
            if c in("+","-","*","/"):
                   break
            print("invalid operator")
                   
       y = int(input(prompt))

       if c == "+":
                print(x + y)

       elif c == "-":
            print(x - y)
       elif c == "*":
                print(x * y)
       elif c == "/":
                print(x / y)
           
       break
    except ValueError:
                    print("put a number")
        
                       
    except ZeroDivisionError :
            print("u can't devide by 0")

main()
