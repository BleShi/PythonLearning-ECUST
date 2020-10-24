linea = float(input("请输入三角形的第一条边："))
lineb = float(input("请输入三角形的第二条边："))
linec = float(input("请输入三角形的第三条边："))

if linea <=0 or lineb <=0 or linec<=0 or linea + lineb <= linec or lineb + linec <= linea or linec + linea <= lineb :
    print("不是三角形")
elif linea == lineb == linec :
    print("是等边三角形")
elif linea == lineb or lineb == linec or linec == linea :
    print("是等腰三角形")
elif linea*linea + lineb*lineb == linec*linec or linea*linea + linec*linec == lineb*lineb or lineb*lineb +linec*linec == linea*linea :
    print("是直角三角形")
else:
    print("是三角形")