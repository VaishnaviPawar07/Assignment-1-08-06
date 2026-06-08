#Loan Eligibility
name=input("Enter your name: ")
is_job_holder=input("Do you have a job (Y/N): ")
bank_bal=float(input("Enter your bank balance: "))

if is_job_holder=="Y" and bank_bal>100000:
    print("You are eligible for loan")

else:
    print("You are not eligible for loan")