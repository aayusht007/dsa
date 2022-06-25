# 1. Write a Python program to calculate the sum of a list of numbers.

# def sum(n):
#     no=1
#     if n==1 or n==0:
#         return n

#     add =no+sum(n-1)
#     return add
# if __name__=="__main__":
        
#     print(sum(29))

# Write a Python program of recursion list sum. Go to the editor
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
#####################################################################################################################

# def sum(n):
#     total=0
#     for i in n:
#         if type(i)== type([]):
#             total=total+sum(i)
#         else:
#             total=total+i
#     return total

# if __name__=='__main__':
#     print(sum([1, 2, [3,4],[5,6]]))

#######################################################################################################

#  Write a Python program to get the factorial of a non-negative integer.

# def factorial(no):
#     # 4!=4*3*2*1
#     if no<=1:
#         return 1
#     else:
#         return no*(factorial(no-1))

# if __name__=="__main__":
#     print(factorial(5))

###############################################################################
# 5. Write a Python program to solve the Fibonacci sequence using recursion
# def fib(no):
#     if no==0 or no==1:  #0+1+2+3
#         return no
#     return fib(no-1) + fib(no-2)

    
# if __name__=="__main__":
#     print(fib(7))

#######################################################################
# 6. Write a Python program to get the sum of a non-negative integer. Go to the editor
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

# def sumdigit(n):
#     if n==0:
#         return n
#     else:
#         new= n%10 + sumdigit(int(n/10))
#         return new

# if __name__=="__main__":
#     print(sumdigit(344))

##################################################################################
# Write a Python program to calculate the value of 'a' to the power 'b'.

# Test Data:
# (power(3,4) -> 81

# def power(a,b)

# return a*power(a,b-1)

##############################################################
# Write a Python program to find the greatest common divisor (gcd) of two integers.
def gcd(a,b):
    low=min(a,b)
    high=max(a,b)
    if low==0:
        return high
    elif low==1:
        return 1
    return gcd(low,high%low)

if __name__=="__main__":
    print(gcd(21,49))