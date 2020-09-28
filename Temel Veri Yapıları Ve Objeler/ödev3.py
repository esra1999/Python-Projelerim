"""  Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
ve sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın. """
yakıt=float(input("kmde yaktıgı yakıt:"))
km=int(input("aldıgı km:"))
odeme=yakıt*km
print("Ödeyeceğiniz miktar:{}".format(odeme))