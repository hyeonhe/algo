x = int(input())
num = 0

a, b = 0, 0

line = 1
while x > line:
    x -= line
    line += 1
    
    
if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x
    
print(f"{a}/{b}")