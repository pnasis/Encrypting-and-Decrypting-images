import math
from operator import mod

print("Prime number check:\n");

def isprime_3(n):
    if n<=1:
        return False
    t = 2
    while t*t <= math.floor(n): 
        if mod(n,t) == 0:
            return t, False
        t = t+1
    return n, True
    
#As parameters, type the numbers you want.
print (isprime_3(10))
print (isprime_3(131))