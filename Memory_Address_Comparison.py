#Memory Address Comparison
num1 = [25]
num2 = num1

print("Address of num1:", id(num1))
print("Address of num2:", id(num2))

if num1 is num2:
    print("Same memory address")
else:
    print("Different memory addresses")