n = int(input("Enter a number: "))
sum=0
for i in range(n):
    if i%2==0:
        sum+=i

print(f"the sum of all even numbers from 1 to the {n} is = {sum}")