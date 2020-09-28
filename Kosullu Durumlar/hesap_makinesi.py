print("""
********************************************
HESAP MAKİNESİ PROGRAMI
1.Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme İşlemi
********************************************
""")
a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
işlem=input("işlem seçiniz:")
if işlem=="1":
    print("{} ve {}'nin toplamı {}'dir.".format(a , b , a+b))
elif işlem=="2":
    print("{} ve {}'nin farkı {}'dir.".format(a, b, a - b))
elif işlem == "3":
    print("{} ve {}'nin çarpımı {}'dir.".format(a, b, a * b))
elif işlem == "4":
    print("{} ve {}'nin bölümü {}'dir.".format(a, b, a / b))
else:
    print("geçersiz işlem...")