import random 
  
# Initializing list  
li = [1, 4, 5, 10, 2] 
  
# Printing list before shuffling 
print ("The list before shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 
  
# using shuffle() to shuffle the list 
random.shuffle(li) 
  
# Printing list after shuffling 
print ("The list after shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 
  
# using uniform() to generate random floating number in range 
# prints number between 5 and 10 
print ("The random floating point number between 5 and 10 is : ",end="") 
print (random.uniform(5,10)) 