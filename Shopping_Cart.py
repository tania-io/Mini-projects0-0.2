
# PROJECT 5: Shopping Cart

print("Wellcome to you own Shopping cart 🛍️")
print("=== M E N U === \n➕ ADD ITEM \n👁️ VIEW CART \n✒️MODIFY ITEMS \n⛔ REMOVE ITEMS \n📤 CHECKOUT: ")

shopping_cart = []

def view_cart(shopping_cart):
    if not shopping_cart:
        input("📂 Nothing to View in Cart.")

    else:
        print("=" * 70)
        print(f"{'Sl.No':<6} | {'Name':<15} | {'Price':>12} | {'Quantity':>12} | {'Amount':>12}")
        print("-" * 70)

        total_quantity = 0
        total_amount = 0

        for index, item in enumerate(shopping_cart, start=1):
            name, price, quantity = item
            amount = quantity * price

            print(f"{index:<6} | {name:<15} | {price:>12.2f} | {quantity:>12} | {amount:>12.2f}")

            total_quantity += quantity
            total_amount += amount

        tax = total_amount * 18 / 100

        print("=" * 70)
        print(f"{'Total':<43}{total_quantity:>12}  {total_amount:>12.2f}")
        print(f"{'TAX 18%':<55}  {tax:>12.2f}")

        print("-" * 70)

        print(f"{'To Pay':<55}  {total_amount + tax:>12.2f}")
        print("-" * 70)


while True:

    option = input("Press any key to continue:\n 1️⃣ to ADD ITEM 2️⃣ to VIEW CART 3️⃣ to MODIFY ITEM 4️⃣ to REMOVE ITEM 5️⃣ to CHECKOUT: ")

    if option == "1":
        new_item = input("📥 Enter your item to add: ")

        try:
            item_price = float(input("🏷️ Enter your item price: "))
        except:
            print("Enter a valid price!")
            continue

        try:
            quantity = int(input("🛒 Enter your quantity: "))
        except:
            print("Enter a valid quantity!")
            continue

        shopping_cart.append((new_item, item_price, quantity))  #<-- stored as tuples

        print(f"{new_item, item_price, quantity} is added to your shopping cart. ✅")

        add_more = input("➕ Want to add more items? Yes(y)/ No(n): ")
        if add_more == "y":
            continue

        else:
            print("⚠️ Invalid Input!")
            continue

    elif option == "2":
            view_cart(shopping_cart)

    elif option == "3":

        while True:
            if not shopping_cart:
                print("Nothing to Modify!")
                break

            for index, item in enumerate(shopping_cart, start=1):
                print(f"📌 {index}. {item} ")

            try:
                modify_item = int(input("📝 Enter the item number to modify: "))

            except:
                print("🔢 Please enter a number!")
                continue

            valid_item = 1 <= modify_item <= len(shopping_cart)

            if valid_item:

                selected_item = shopping_cart[modify_item - 1]

                name, price, quantity = selected_item

                print(f"1. Name: {name}\n2. Price: {price}\n3. Quantity: {quantity}")

                modify_choice = input("✒️ Enter your choice from 1 to 3: ")

                if modify_choice == "1":
                    new_modified_item = input("📥 Enter the new item: ")
                    name = new_modified_item
                    print("Item modified successfully! ✅")

                elif modify_choice == "2":
                    try:
                        new_price = float(input("🏷️ Enter the new item price: "))
                        price = new_price
                        print("Item price modified successfully! ✅")

                    except:
                        print("🔢 Enter the valid number!")
                        continue

                elif modify_choice == "3":
                    try:
                        new_quantity = int(input("🛒 Enter the new quantity: "))
                        quantity = new_quantity
                        print("Item quantity modified successfully! ✅")
                    except:
                        print("🔢 Enter the valid number!")
                        continue

                else:
                    print("⚠️ Invalid input!")
                    continue

                shopping_cart[modify_item - 1] = (name, price, quantity)

                modify_again = input("📝 Do you want to modify anything else? Yes(y)/ No(n): ")

                if modify_again == "y":
                    continue

                elif modify_again == "n":
                    break
                else:
                    print("⚠️ Enter y or n!")

            else:
                print("⚠️ Invalid item number!")

    elif option == "4":
        while True:
            if not shopping_cart:  # also same as if shopping_cart == 0:
                print("📂 Nothing to remove!")
                break

            for index, item in enumerate(shopping_cart, start = 1):
                print(f"📌 {index}. {item} ")

            try:
                delete_item = int(input("⛔ Enter the item number to remove: "))

            except:
                print("🔢 Please enter a number!")
                continue

            valid_item = 1 <= delete_item <= len(shopping_cart)

            if valid_item:
                removed_item = shopping_cart.pop(delete_item - 1)
                print(f"{removed_item} is removed from your shopping cart ☑️.")

                delete_more = input("⛔ Want to remove another item? Yes(y)/ No(n): ")

                if delete_more == "y":
                    continue

                elif delete_more == "n":
                    break
                else:
                    print("⚠️ Enter y or n!")

            else:
                print("⚠️ Invalid input.")

    elif option == "5":

            print("====   FINAL CHART   ====")
            view_cart(shopping_cart)

            if not shopping_cart:  # also same as if shopping_cart == 0:
                print("📂 Empty Chart!")

            checkout = input("💭 Procced to Checkout? Yes(y)/ No(n): ")

            if checkout == "y":
                break

    else:
        print("⚠️ Invalid option. Please try again.")
