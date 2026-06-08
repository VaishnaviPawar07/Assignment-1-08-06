#Emp record search
employee_ids = [57,25,3,45]

eid = int(input("Enter Employee ID: "))

if eid in employee_ids:
    print("Employee Record Available")
else:
    print("Employee Record Not Available")