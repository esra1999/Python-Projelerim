""" Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2 """
a = int(input("kenar1:"))
b = int(input("kenar2:"))
c = (a**2 + b**2)**5
print("hipotenus uzunlugu:{}".format(c))

