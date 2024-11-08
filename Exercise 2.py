# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 17 
x += 3

print("Answer = " + str(x))
# TODO: Multiply y by 2 using the *= operator
y = 9
y *= 2

print("Answer = " + str(y))
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y

# TODO: Print the value of 'result'
print("Answer is " + str(result))
print(f'Answer is   {round( result ,2)}') 
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 14
b = 17

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)

modulus =  b % 2

if modulus == 0:
    print("b is even")
else:
    print("b is odd")

# TODO: Create a condition that checks if c is less than or equal to a
c = 9 

if c <= a:
    print("c is less than or equal to a")
else:
    print("c is not less than or equal to a")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a > b) or (modulus == 0 and c <= a)

# TODO: Print the value of 'final_condition'
print (final_condition )

# ------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'

score = int(input("Please enter your test score:"))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
grade = ''
if score >= 90 and score<101:
    print('A') 
elif score >= 80 and score <=89:
    print('B')
elif score >= 70 and score <=79:
    print('C')
elif score >= 60 and score <=69:
    print('D')
else:
    print('F')

# TODO: Print the grade for the given score
print (score)
# ------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'

print("Please fill in the following:")

num1 = int(input("No.1:"))
num2 = int(input("No.2:"))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

operation = input("Please choose an operation from the following: '+' or '-' or '*' or '/'")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
answer = 0
if operation == "+":
    answer = num1 + num2
elif operation == "-":
    answer = num1 - num2
elif operation == "*":
    answer = num1 * num2
elif  operation == "/":
    if num2 == 0:
        print("You can not divide by zero")
    else:
        answer = num1 / num2
else:
    print("Please enter valid operation!")
         
# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
 
print(answer)