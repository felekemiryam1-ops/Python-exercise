try:
    file_name = input("What is the file name?")
    file=open(file_name)
    content = file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Permission Denied")
