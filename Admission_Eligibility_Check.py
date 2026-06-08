#Admission Eligibility Check
name=input("Enter your name:")
percentage = float(input("Enter your percentage: "))

if percentage >= 97:
    print(f"{name} you are eligible for Admission")
else:
    print(f"{name} you are not eligible for Admission")