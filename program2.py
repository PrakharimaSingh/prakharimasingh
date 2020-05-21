n = int(input(" Number : "))
a , b = 0 , 1
s = str()

for i in range(n):
    s = s + ',' + str(a)
    a , b = b , a+b

print(s.lstrip(" , "))
