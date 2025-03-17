#Run and observe the output
'''
Why Use Lambda?
1-> It’s a shortcut for small functions.
2->No need to write def and return.
3->Useful for quick, one-time calculations.'''

#Task 1- Modify the lambda function to triple the number instead of doubling it. 
#Then, print the result for 5

#This is using a lambda function for quick calculations.
double = lambda x: x * 2  
print(double(4))  


# This is a regular function definition.
def double(x):
    return x*2
print(double(4))  

#Both functions gives the same result.
