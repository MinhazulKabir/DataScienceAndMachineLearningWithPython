"""
Name: Md. Minhazul Kabir
Email: mdminhazulkabir@gmail.com
Problem Name: 01. Determine if a Number is Even, Odd, or Zero
"""
number = int(input("Enter a number: "))

# Check if the number is zero, even, or odd
if number == 0:
    print("The Number is zero.")
elif number % 2 == 0:
    print("The Number an even number.")
else:
    print("The Number an odd number.")
