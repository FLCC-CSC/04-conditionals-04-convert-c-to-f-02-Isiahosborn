# FILE NAME - convert_C_to_F_02.py

# NAME: Isiah Osborn
# DATE: 2025-10-05
# BRIEF DESCRIPTION:  
#   Show a small menu to convert temperatures between Celsius and Fahrenheit.
#   Reads a menu choice and a temperature, then prints the converted value.
#   Output formatting matches the sample (prompts, spacing, and one decimal).



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    print("===== Temperature Converter =====")
    print()
    print("  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius")
    print()
    choice = input("Please choose from the above menu: ").strip()
    value_str = input("Enter a temperature to convert: ").strip()
    print()  # blank line before the result

    temp = float(value_str)

    if choice == "1":
        result = c_to_f(temp)
        print(f"{temp:.1f} degrees Celsius is {result:.1f} degrees Fahrenheit.")
    else:
        result = f_to_c(temp)
        print(f"{temp:.1f} degrees Fahrenheit is {result:.1f} degrees Celsius.")

if __name__ == "__main__":
    main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
The auto grader hates me i learned that the hard way
'''





'''
