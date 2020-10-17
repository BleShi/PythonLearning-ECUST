import math

a = float(input("请输入第一条边长："))
b = float(input("请输入第二条边长："))
c = float(input("请输入第三条边长："))

p = (a+b+c)*0.5
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("三角形的面积为",s)

cosdegree = float((b*b+c*c-a*a)/2/b/c)
degree = math.acos(cosdegree)
print("其中一个角的角度为",degree)