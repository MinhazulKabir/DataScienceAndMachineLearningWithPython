def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for i in numbers:
        if i % 2 == 0:
            even_sum += i  # Add to even_sum if the number is even
        else:
            odd_sum += i   # Add to odd_sum if the number is odd

    # Return the sum of even and odd numbers as a tuple
    return even_sum, odd_sum

numbers_list = [74, 94, 80, 61, 25, 42, 95, 31, 18, 64]

# Call the function and unpack the returned into two variables
even_n, odd_n = sum_even_odd(numbers_list)

# Output the results
print("Sum of even numbers:", even_n)  # Print the sum of even numbers
print("Sum of odd numbers:", odd_n)   # Print the sum of odd numbers
