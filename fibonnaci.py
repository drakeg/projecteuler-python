#!/usr/bin/python

def isEven(number):
   if number%2 == 0:
	return 1
   else:
        return 0

fibonnaci=[1,2]
sum=0
counter=0
total=2
i=1
while(True):
  sum = fibonnaci[i] + fibonnaci[i-1]
  if sum < 4000000:
    if isEven(sum):
      total=total+sum
    i += 1
    fibonnaci.append(sum)
  else:
    break
print "The final list is: ",fibonnaci, "\n"
print "The answer is: ", total, "\n"
