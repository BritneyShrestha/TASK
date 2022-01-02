usr_name = input("Enter your name: ")
 
names = ["Terry", "John", "Michael", "Eric", "Terry","Graham"]
if usr_name in names:
    names.insert(0,usr_name.upper())
    names.remove(usr_name)
    print(names)
    