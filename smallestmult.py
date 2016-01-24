#!/usr/bin/python

counter=40
for i in range(2,21):
  found = True
  print i
  while found == True:
    if counter%i == 0:
      found = True
      print counter,"%",i,":",counter%i,"so found is True"
    else:
      found = False
      print counter,"%",i,":",counter%i,"so found is False."
    counter=counter+1
print i
