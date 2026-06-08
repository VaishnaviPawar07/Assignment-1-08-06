#Salary Calculation System

basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10

gross = basic + hra + da

deduction = float(input("Enter Deduction Amount: "))

net = gross - deduction

print("\nGross Salary =", gross)
print("Net Salary =", net)