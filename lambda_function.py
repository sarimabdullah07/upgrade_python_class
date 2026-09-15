import math
print((lambda a:math.sqrt(a)+a**2)(25))
print((lambda a,b,c:a if a>b>c else(b if b>a>c else c))(82,43,98))
print(list(map((lambda a:0 if a%2==0 else 1),([32,45,23,60,12,57]))))
print((lambda a: "verified" if a==2190 else "Incorrect passward")(2190))
print((lambda a:a.upper())("python"))

