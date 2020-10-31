sum= 1
i = 1
new = 1

while True:
    i = i + 1
    new = new * (i-1)/(2*i-1)
    sum = sum + new       
    
    if i>=1000:
        break

print(sum)