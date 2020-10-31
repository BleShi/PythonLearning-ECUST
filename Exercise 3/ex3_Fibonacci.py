result=[1,1]
for i in range(100):
    if result[-1]+result[-2]>100:
        break
    else:
        result.append(result[-2]+result[-1])
print(result)