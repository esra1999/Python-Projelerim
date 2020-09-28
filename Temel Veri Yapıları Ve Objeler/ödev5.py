"""Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."""

a=input("a:")
b=input("b:")
print("önceki=a:{},b{}\n".format(a,b))
a,b=b,a
print("sonraki=a:{},b{}".format(a,b))