""" Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez   """
boy=int(input("boyunuz:"))
kilo=int(input("kilonuz:"))
beden_kitle_indeksi= kilo / boy * boy
if (beden_kitle_indeksi <18.5):
    print("zayıf")
elif (beden_kitle_indeksi >=18.5 and beden_kitle_indeksi < 25):
    print("normal")
elif (beden_kitle_indeksi >=25 and beden_kitle_indeksi <30):
    print("fazla kilolu")
elif(beden_kitle_indeksi>30):
    print("obez")

