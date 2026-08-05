def main():
    number=get_positive_int("Enter a positive integer")
    print(number)
    


def get_positive_int(prompt):
  while True:
     try:

            
     
                num = int(input(prompt))
                if num >0:
                    return num
                print("integer must be > 0")

              
              
     except ValueError:
        print("Invalid")
main()