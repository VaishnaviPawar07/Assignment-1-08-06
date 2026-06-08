#Employee Bonus Eligibility
name=input("Enter emp name:")
clients_attended=int(input("number of clients attended in this month "))
if clients_attended>=10:
    print(f"{name} you are eligible for Bonus")
else:
    print(f"{name} not eligible for Bonus")