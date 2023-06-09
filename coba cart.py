import csv
import os

# Function to display the available products
def display_products(products):
    print("Available Products:")
    print("-------------------")
    for product in products:
        print(f"{product['name']}: ${product['price']}")

# Function to add products to the shopping cart
def add_to_cart(products, cart):
    display_products(products)
    product_name = input("Enter the name of the product: ")
    quantity = int(input("Enter the quantity: "))

    # Search for the product in the product list
    for product in products:
        if product['name'] == product_name:
            cart.append({'name': product['name'], 'price': product['price'], 'quantity': quantity})
            print(f"{quantity} {product_name}(s) added to the cart.")
            return

    # If the product is not found
    print("Product not found.")

# Function to display the shopping cart
def display_cart(cart):
    if len(cart) == 0:
        print("Your shopping cart is empty.")
    else:
        total = 0
        print("Shopping Cart:")
        print("--------------")
        for item in cart:
            print(f"{item['name']}: ${item['price']} x {item['quantity']}")
            total += item['price'] * item['quantity']
        print(f"Total: ${total}")

# Function to remove an item from the shopping cart
def remove_from_cart(cart):
    display_cart(cart)
    item_name = input("Enter the name of the item to remove: ")

    for item in cart:
        if item['name'] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from the cart.")
            return

    print("Item not found in the cart.")

# Function to clear the shopping cart
def clear_cart(cart):
    cart.clear()
    print("Your shopping cart has been cleared.")

# Function to import products from a CSV file
def import_products_from_csv(laguPop):
    products = []
    with open(laguPop, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

#clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)

# Main program
def main():
    # Import products from CSV
    products = import_products_from_csv('laguPop.csv')

    cart = []

    while True:
        print("\nMenu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Clear cart")
        print("4. Display cart")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            clear_screen()
            add_to_cart(products, cart)
        elif choice == '2':
            clear_screen()
            remove_from_cart(cart)
        elif choice == '3':
            clear_screen()
            clear_cart(cart)
        elif choice == '4':
            clear_screen()
            display_cart(cart)
        elif choice == '5':
            clear_screen()
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
