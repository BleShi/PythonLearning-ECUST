j = 0
for num in range(1,151):
    if num >= 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num,end=' ')
            j += 1
            if j % 9 == 0:
                print("\n")