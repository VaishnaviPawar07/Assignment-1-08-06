#Product Availability Checker
products = ["Lipstick", "Foundation", "Blush", "Eyeliner"]

item = input("Enter product name: ")

if item in products:
    print("Product is available")
else:
    print("Product is not available")