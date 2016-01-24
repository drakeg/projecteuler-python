#!/usr/bin/python
 
# function to determine if a number is prime
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

count = 6 
i = 13
while count < 10001:
    i += 2 
    if isPrime(i):
        count += 1
print "The answer is:",i 
