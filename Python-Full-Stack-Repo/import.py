from next import Product
product_list = []

while True:

    print("\n1. Create Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Apply Discount")
    print("5. Increase Price")
    print("6. Exit")

    choice = int(input("Enter your choice: "))




    if choice == 1:

        p_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = int(input("Enter product price: "))

        product = Product(p_id, name, category, price)
        product_list.append(product)

        print("Product created successfully")

    elif choice == 2:

        if len(product_list) == 0:
            print("No products available")
        else:
            for product in product_list:
                print("\nProduct ID:", product.pid)
                print("Product Name:", product.name)
                print("Category:", product.category)
                print("Price:", product.price)

    elif choice == 3:

        p_id = int(input("Enter product ID to search: "))
        found = False

        for product in product_list:
            if product.pid == p_id:
                print("Product ID:", product.pid)
                print("Product Name:", product.name)
                print("Category:", product.category)
                print("Price:", product.price)

                found = True
                break

        if found == False:
            print("Product not found")

    elif choice == 4:

        p_id = int(input("Enter product ID: "))

        for product in product_list:
            if product.pid == p_id:
                percent = int(input("Enter discount percentage: "))
                product.discount(percent)
                break
        else:
            print("Product not found")

    elif choice == 5:

        p_id = int(input("Enter product ID: "))

        for product in product_list:
            if product.pid == p_id:
                amount = int(input("Enter amount to increase price: "))
                product.increase_price(amount)
                break
        else:
            print("Product not found")

    elif choice == 6:

        print("Thank you")
        break

    else:
        print("Invalid choice")


