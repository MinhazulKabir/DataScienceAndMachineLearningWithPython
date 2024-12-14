"""
Name: Md. Minhazul Kabir
Email: mdminhazulkabir@gmail.com
Problem Name: 04. Student Scholarship Eligibility
"""
grade = float(input("Enter your grade: "))
income = float(input("Enter your family income: "))

if grade >= 85:
    if income < 40000:
        print("You are eligible for a full scholarship.")
    else:
        print("You are eligible for a partial scholarship.")
else:
    print("You are not eligible for a scholarship.")
