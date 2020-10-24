import math

num1=int(input("请输入正整数："))
num2=int(input("请再输入一个正整数："))

min=num1

if num1>num2:
    min=num2
for i in range(min,1,-1):
    if num1%i==0 and num2%i==0:
        print(num1,"和",num2,"的最大公约数是：",i)
        break

if num1<= 0 or num2 <= 0:
    print("两个数必须是正整数")
    exit(0)

if num1>num2:
    max=num1
    min=num2
else:
    max=num2
    min=num1
    
for i in range(1,min+1):
    numtemp=max*i
    if numtemp % min == 0:
        numresult=numtemp
        break

print("最小公倍数是：",numresult)

print(num1,"和",num2,"的最大公约数是：",math.gcd(num1,num2))