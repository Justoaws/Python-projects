# write a python program with function, that will ask for two numbers (integer and float) 
# and calculate the sum of those two numbers.
# display on the screen : the sum of number1 and number2 is: sum

def calculate_sum():
    number1 = int(input("Please, enter a number: \n"))
    number2 = float(input("Please, enter a second number: \n"))
    
    result = number1 + number2
    print(f"The sum of {number1} and {number2} is: {result}.")

# Call the function
calculate_sum()
