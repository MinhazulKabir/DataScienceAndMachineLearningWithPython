int_var = 1027
float_var=3.14159
str_var= "2025"
print(f"values= {int_var} and types = {type(int_var)}")
print(f"values= {float_var} and types = {type(float_var)}")
print(f"values= {str_var} and types = {type(str_var)}")

int_str= int(str_var)
print(f"\nConverts the string to an integer {int_str}")
int_float= int(float_var)
print(f"Converts the float to an integer {int_float}")