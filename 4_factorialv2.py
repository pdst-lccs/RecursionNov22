# LCCS Python Fundamental Skills Workshop
# Nov 2022
# Purpose: Another programme to find factorial v2

# What type of solution is this?

def factorial(n):
    
    if n == 1:
        return 1
    
    return n * factorial(n-1)

# Test the function 
x = 5
print(x,"! =", factorial(x))

#using string formatting (p74 of manual)
#print("%d! = %d" %(x, factorial(x)))
