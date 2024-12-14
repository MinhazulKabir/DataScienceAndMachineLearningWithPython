"""
Name: Md. Minhazul Kabir
Email: mdminhazulkabir@gmail.com
Problem Name: 05. Nested Restaurant Menu
"""
meal_type = input("Please select a meal type (\"Vegetarian\" or \"Non-Vegetarian\"): ").lower()

if meal_type == "vegetarian":
    print("Available Vegetarian Dishes: Salad and Soup")
    dish = input("Please select a dish (\"Salad\" or \"Soup\"): ").lower()
    if dish == "salad":
        print("You have selected Vegetarian Salad.")
    elif dish == "soup":
        print("You have selected Vegetarian Soup.")
    else:
        print("Invalid dish choice for Vegetarian.")
elif meal_type == "non-vegetarian":
    print("Available Non-Vegetarian Dishes:")
    dish = input("Please select a dish (\"Chicken\" or \"Fish\"): ").lower()
    if dish == "chicken":
        print("You have selected Non-Vegetarian Chicken.")
    elif dish == "fish":
        print("You have selected Non-Vegetarian Fish.")
    else:
        print("Invalid dish choice for Non-Vegetarian.")
else:
    print("Invalid meal type selection. Please select either 'Vegetarian' or 'Non-Vegetarian'.")
