#!/usr/bin/python
 
# function to determine if a number is prime
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
 
    return True

# find all factors in a number
# and return them in an unsorted list
def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

startNo=600851475143
print factors(startNo)

for x in sorted(factors(startNo)):
      if isPrime(x):
        print x,"is prime."
	answer = x
      else:
        print x,"is not prime."
print "The answer is:",answer 
