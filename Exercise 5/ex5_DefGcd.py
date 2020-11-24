num1 = int(input())
num2 = int(input())

def fun(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    vari1 = num1 * num2
    vari2 = num1 % num2

    while vari2 != 0:
        num1 = num2
        num2 = vari2
        vari2 = num1 % num2

    vari1 /= num2

    aws = (num2,vari1)
    
    print(aws)

fun(num1,num2)