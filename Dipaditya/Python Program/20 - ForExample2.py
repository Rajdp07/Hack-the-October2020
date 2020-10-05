try:
    N = int(input())
except:
    print("Invalid Input")

x = 0
y = 0
d = 10

for i in range(1, N+1):
    if i%4 == 1 :
        x = x + d
    if i%4 == 2:
        y = y + d
    if i%4 == 3:
        x = x - d
    if i%4 == 0:
        y = y - d
    
    d += 10

print(x,y)