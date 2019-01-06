#!/usr/bin/python3
import sys
print ("\n====================")
print ("Iterator and Generator")
print ("====================\n")

print ("\n===============")
print ("Iterator Loop")
print ("===============\n")

list = [1,2,3,4]
it = iter(list) # this builds an iterator object

for x in it:
   print (x, end=" ")

print("\n\nusing next function\n")

it = iter(list) # this builds an iterator object
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this