import math 
  
a = 2.3
  
# returning the ceil of 2.3 
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
  
# returning the floor of 2.3 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a)) 

b = -10
  
c= 5
  
# returning the absolute value. 
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(b)) 
  
# returning the factorial of 5 
print ("The factorial of 5 is : ", end="") 
print (math.factorial(c)) 

# returning the copysigned value. 
print ("The copysigned value of -10 and 5.5 is : ", end="") 
print (math.copysign(5.5, -10)) 
  
# returning the gcd of 15 and 5 
print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(5,15)) 