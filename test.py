#!/usr/bin/python3

'''
Python language supports the following types of operators −

	Arithmetic Operators
	Comparison (Relational) Operators
	Assignment Operators
	Bitwise Operators
	Logical Operators
	Membership Operators
	Identity Operators
'''
a , b = 21 , 10
# a = 21 ; b = 10

# Arithmetic Operators
print("\n======================")
print("\nArithmetic Operators\n")
print("======================\n")

print (a + b)		#	Addition
print (a - b)		#	Subtract
print (a / b)		#	Divide
print (a * b)		#	Multiply
print (a % b)		#	Modulus
print (a ** b)		#	Exponential
print (a // b)		#	Floor Division

a , b = 10 , 20

# Comparison (Relational) Operators
print("\n===================================")
print("\nComparison (Relational) Operators\n")
print("===================================\n")
print (a == b)		#	Equal
print (a != b)		#	Not Equal
print (a > b)		#	Greater
print (a < b)		#	Lesser
print (a >= b)		#	Greater than or equal
print (a <= b)		#	Lesser than or equal

# Assignment Operators
print("\n======================")
print("\nAssignment Operators\n")
print("======================\n")
c = 0
c = a + b; 	print (c)		#	Equals
c += a; 	print (c)		#	
c -= a; 	print (c)		#	
c *= a; 	print (c)		#	
c /= a; 	print (c)		#	
c %= a; 	print (c); c+=2	#	
c **= a; 	print (c)		#


# Bitwise Operators
print("\n===================")
print("\nBitwise Operators\n")
print("===================\n")
a = 60; b = 13;	print("Bitwise Operators for {} and  {}".format(a, b))
a = 60; b = 13;	print ("Binary And for {} and {} is : {}".format(a, b, a&b)) 			#	Binary And
a = 60; b = 13;	print ("Binary OR for {} and {} is : {}".format(a, b, a|b)) 			#	Binary OR
a = 60; b = 13;	print ("Binary XOR for {} and {} is : {}".format(a, b, a^b)) 			#	Binary XOR
a = 60; b = 13;	print ("Binary ~ for {} is : {}".format(a, ~a)) 						#	Binary Complement
a = 60; b = 13;	print ("Binary << for {} and {} is : {}".format(a, 2, a << 2)) 			#	Binary Left Shift
a = 60; b = 13;	print ("Binary >> for {} and {} is : {}".format(a, 2, a >> 2)) 			#	Binary Right Shift

# Logical Operators
print("\n===================")
print("\nLogical Operators\n")
print("===================\n")
a = True; b = False
print("Logical Operators for {} and  {}".format(a, b))
print("Logical Operators for {} and  {} is : {}".format(a, b, a and b))
print("Logical Operators for {} or  {} is : {}".format(a, b, a or b))
print("Logical Operators for not of {} is : {}".format(a, not a))

# Membership Operators
print("\n======================")
print("\nMembership Operators\n")
print("======================\n")
list = [2,5,7,8,9]
tuple = ('A','B','C','D','E')
print("list value is : {} ".format(list))
print("tuple value is : {} ".format(tuple))
print("\nCheck For True\n")
print("is 7 contained in {} : {} ".format(list, 7 in list))
print("is B contained in {} : {} ".format(tuple, 'B' in tuple))
print("\nCheck For False\n")
print("is 3 not contained in {} : {} ".format(list, 3 not in list))
print("is B not contained in {} : {} ".format(tuple, 'B' not in tuple))


# Identity Operators
print("\n======================")
print("\nIdentity Operators\n")
print("======================\n")
a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

