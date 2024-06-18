# username = input("Enter username:")
# print("Username is: " + username)
while True:
    age = input("How old are you ")
    if age == 'stop':
        print("The program has stopped")
        break
    age = int(age)
    if age == 69:
        print("NICE")
    elif age > 17:
        print("You can go in")
    elif age < 1:
        print("Invalid age")
    else: 
        print("You cannot go in")
    
