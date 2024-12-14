"""
Name: Md. Minhazul Kabir
Email: mdminhazulkabir@gmail.com
Problem Name: 03. Check Voting Eligibility
"""
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? \"yes\" or \"No\". ").lower()

if age >= 18:
    if citizenship == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote due to citizenship status.")
else:
    print("You are not eligible to vote due to age.")
