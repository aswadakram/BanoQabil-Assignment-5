def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a  #The "return" will send back the value to the place where function is called.
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(5,3,7))
print(max_of_three(8,9,4))
print(max_of_three(-1,-2,-3))