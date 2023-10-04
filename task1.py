#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""
q1 = "what is the number:"
print(input(q1))
Thenumberislargerthan100 = True
Thenumberissmallerthan100 = False
Thenumberis100 = False

if Thenumberislargerthan100 :
    print("the number is larger than 100")

if Thenumberissmallerthan100:
    print("the number is 100")

if Thenumberis100:
    print("the number is smaller than 100")