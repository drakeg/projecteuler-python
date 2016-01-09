#!/usr/bin/python

def isPalindrome(x):
  if str(x) == str(x)[::-1]:
    return True
  else:
    return False

answer=0
for x in range(100,1000):
  for y in range(100,1000):
    product = x*y
    if isPalindrome(product):
      if product > answer:
        answer=product
print "The answer is:",answer
