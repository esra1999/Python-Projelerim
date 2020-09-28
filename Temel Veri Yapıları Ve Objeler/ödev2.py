"""Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m)**2"""
kilo = int(input("kilo:"))
boy = int(input("boy:"))
beden_kitle_endeksi= kilo / boy**2
print("beden kitle endeksiniz: {}".format(beden_kitle_endeksi))
