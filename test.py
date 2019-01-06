#!/usr/bin/python3

print ("\n===============")
print ("   Loops")
print ("===============\n")


print ("\n===============")
print ("while loops")
print ("===============\n")

count = 0
while count < 5:
   print ('The value of count is :', count)
   count+=1
print ("While loop closed")

print ("\n===============")
print ("while loops with else")
print ("===============\n")


count = 0
while count < 5:
	print ('The value of count is :', count)
	count+=1
else:
	print ("While loop closed")

print ("No Condition here")


print ("\n===============")
print ("for loops")
print ("===============\n")


for val in list(range(5)):
   print ('The value of list item is :', val)   
print ("for loop closed")

print ("\n===================")
print ("for loops using index")
print ("===================\n")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("\n===================")
print ("for loops using else")
print ("===================\n")
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list {} doesnot contain even number'.format(numbers))