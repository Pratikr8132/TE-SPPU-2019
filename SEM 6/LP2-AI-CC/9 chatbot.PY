products = ["Shirt", "Pants", "Shoes", "Sunglasses", "Watch"]
colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]
sizes = ["Small", "Medium", "Large", "X-Large"]


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.color.lower() == other.color.lower() and self.size.lower() == other.size.lower()


inventory = [
    Product("Shirt", "Blue", "Large"),
    Product("Pants", "Black", "Medium"),
    Product("Shoes", "Red", "X-Large"),
    Product("Sunglasses", "Green", "Small"),
    Product("Watch", "Yellow", "Large"),

]

print("Welcome to our store! How can I help you?")
user_input = input()

while user_input.lower() != "exit":
    if user_input.lower() == "hello":
        print("Let me ask you a few questions to help narrow down our recommendations.")

        print("What type of product are you looking for? We have the following options:")
        for product in products:
            print("- " + product)
        customer_product = input()

        print("What color do you prefer? We have the following options:")
        for color in colors:
            print("- " + color)
        customer_color = input()

        print("What size do you need? We have the following options:")
        for size in sizes:
            print("- " + size)
        customer_size = input()

        customer_preference = Product(customer_product, customer_color, customer_size)

        print("Here are our recommendations based on your preferences:")
        product_found = False
        for product in inventory:
            if product == customer_preference:
                print("- " + product.color + " " + product.size + " " + product.name)
                product_found = True

        if not product_found:
            print("Sorry, we don't have that product.")

    else:
        print("I'm sorry, I didn't understand your inquiry. Please try again.")

    user_input = input()

print("Thank you for shopping with us! Goodbye.")

























#
#
# Sure! Here's an explanation of the code line by line:
#
# The code defines a list of available products, colors, and sizes.
# A class named Product is defined to represent a product. It has attributes such as name, color, and size.
# The __eq__ method is overridden to enable comparison between two Product objects based on their name, color, and size.
# An inventory list is created, containing instances of the Product class representing the available products.
# The code prints a welcome message to the user.
# The user input is obtained.
# The code enters a loop that continues until the user enters "exit".
# If the user input is "hello" (case-insensitive), it proceeds with the product inquiry process.
# The code prints a message to gather the product type preference from the user.
# It iterates over the available product types and displays them.
# The user input for the product type is obtained.
# The code prints a message to gather the color preference from the user.
# It iterates over the available colors and displays them.
# The user input for the color is obtained.
# The code prints a message to gather the size preference from the user.
# It iterates over the available sizes and displays them.
# The user input for the size is obtained.
# A customer_preference object is created using the user's input for product type, color, and size.
# The code prints a message to display the recommendations based on the customer's preferences.
# A flag variable product_found is set to False to track if a matching product is found.
# It iterates over the inventory to check for products matching the customer's preferences.
# If a match is found, it prints the product's details.
# The product_found flag is set to True.
# If no matching product is found, it prints a message indicating the unavailability.
# If the user input is not recognized as "hello", it prints an error message.
# The user input is obtained again to continue the loop or exit.
# The code prints a farewell message when the user enters "exit".
# Here are some questions and answers related to the code:
#
# Q: What is the purpose of the Product class?
# A: The Product class is used to represent a product with attributes such as name, color, and size. It also overrides the __eq__ method for comparison based on these attributes.
#
# Q: What is the purpose of the inventory list?
# A: The inventory list stores instances of the Product class representing the available products in the store.
#
# Q: How does the code handle case sensitivity for user inputs?
# A: The code converts all user inputs to lowercase when comparing them with specific keywords or attributes. This allows case-insensitive matching.
#
# Q: How are recommendations generated based on the customer's preferences?
# A: The code compares the customer's preferences (product type, color, and size) with each product in the inventory. If a match is found, the details of the product are printed as a recommendation.
#
# Q: What happens if the customer's preferred product is not available in the inventory?
# A: If no matching product is found based on the customer's preferences, the code prints a message stating that the requested product is not available.
#
# Q: How can the user exit the program?
# A: The user can exit the program by entering "exit" (case-insensitive) as their input.