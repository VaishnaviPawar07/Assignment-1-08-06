#shopping bill calcy
num=int(input("Enter the number of items: "))
bill=0
for i in range(num):
    item = input(f"Enter the item {i + 1}: ")

for i in range(num):
    price=float(input(f"Enter the price of item {i + 1}: "))
    bill+=price
print(f"Total Bill: {bill}")