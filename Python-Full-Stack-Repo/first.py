
menu = {
    1: {
        "Starters": {
            1: "Manchurian",
            2: "Paneer Tikka",
            3: "French Fries"
        }
    },

    2: {
        "Main Course": {
            1: "Paneer Masala",
            2: "Veg Biryani",
            3: "Dal Tadka"
        }
    },

    3: {
        "Desserts": {
            1: "Gulab Jamun",
            2: "Ice Cream",
            3: "Brownie"
        }
    }
}


order = []

while True:

    print("\n1. Starters")
    print("2. Main Course")
    print("3. Desserts")
    print("4. View Order")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    elif choice == 4:
        print("\nYour Order:")

        for item in order:
            print(item)

    elif choice in menu:

        category = menu[choice]

        for name, items in category.items():

            print("\n", name)

            for number, item in items.items():
                print(number, item)

            item_choice = int(input("Enter item number: "))

            if item_choice in items:
                order.append(items[item_choice])
                print("Item added!")
            else:
                print("Invalid item!")

    else:
        print("Invalid choice!")

