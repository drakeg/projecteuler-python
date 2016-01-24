#!/usr/bin/python

def isPalindrome(x):
  return str(x) == str(x)[::-1]

answer=0
for x in range(100,1000):
  for y in range(100,1000):
    product = x*y
    if isPalindrome(product):
      if product > answer:
        answer=product
print "The answer is:",answer
