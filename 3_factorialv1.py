# LCCS Python Fundamental Skills Workshop
# Nov 2022
# Purpose: A solution to factorial v1

# What type of solution is this?

def factorial(n):
    
    answer = 1
    for i in range(n, 1, -1): 
        answer = answer * i
    
    return answer

# Test the function 
x = 5
print(x,"! =", factorial(x))

#using string formatting (p74 of manual)
#print("%d! = %d" %(x, factorial(x)))