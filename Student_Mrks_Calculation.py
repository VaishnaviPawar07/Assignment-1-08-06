#student marks calculator
from pyparsing import dictOf

print("Enter 4 subjects")
s1=input("Enter subject 1: ")
s2=input("Enter subject 2: ")
s3=input("Enter subject 3: ")
s4=input("Enter subject 4: ")

m1=float(input(f"Enter marks for {s1}"))
m2=float(input(f"Enter marks for {s2}"))
m3=float(input(f"Enter marks for {s3}"))
m4=float(input(f"Enter marks for {s4}"))

#Calculate total marks
Total = m1+m2+m3+m4
print(Total)
Average = Total/4
print(Average)
print("Percentage :",Total/400*100)



