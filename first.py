age = int(input("Enter your age: "))

if age >= 18:
    citizenship = input("Are you a citizen? (yes/no): ")

    if citizenship == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are under 18.")
