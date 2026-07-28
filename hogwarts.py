students =["her" , "harry" , "Ron"]

print(students[0])
print(students[1])
print(students[2])

for student in students :
    print(student)


for i in range(len(students)):
    print(i +1, students[i])




students={
     "her":"G",
     "Ron":"G",
     "har":"G",
     "Dr":"S"
}

print(students["her"])
print(students["Ron"])
print(students["har"])
print(students["Dr"])

for student in students:
    print(student, students[student], sep= ",")



student=[
    {"name": "her" , "house":"G", "patrounus":"otter"}
    {"name": "her" , "house":"G", "patrounus":"otter"}

     



]



def main():
    print_row(4)
    print_column(3)


def print_row(width):
    print("?" * width)

def print_column(height):
    print("#\n" * height, end="")


    #for _ in range (height):
        #print("#")

main()



def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("# * width")

main()