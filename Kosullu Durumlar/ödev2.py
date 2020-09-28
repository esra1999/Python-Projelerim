"""  Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın
"""
a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
c=int(input("üçüncü sayı:"))
if(a>b and a>c):
    print(" a en büyük..")
elif(b>a and b>c):
    print("b en büyük..")
elif(c>a and c>b):
    print("c en büyük..")
