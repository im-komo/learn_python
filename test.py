#!/usr/bin/python3

print ("\n===============")
print ("Control Statements")
print ("===============\n")

print ("\n===============")
print ("Break Statements")
print ("===============\n")


for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("\n=================")
print ("Continue Statements")
print ("=================\n")

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)


print ("\n=================")
print ("Pass Statements")
print ("=================\n")

for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
