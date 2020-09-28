"""Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir
 dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa,
ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs()
fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5
"""
şekil=input("Üçgenin mi dörtgenin mi değerini bulmak istiyorsunuz?")

if(şekil=="üçgen"):
    print("lütfen 3 kenar uzunluğunu giriniz.")
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
if(a==b==c):
    print("eşkenar ücgen")
elif(a==b or b==c or a==c):
    print("ikizkenar ücgen")
else:
    print("çesitkenar ücgen")


elif(şekil=="dörtgen"):
    print("lütfen dört kenar uzunluğunu giriniz.")
    d = int(input("1.kenar"))
    e = int(input("2.kenar"))
    f = int(input("3.kenar"))
    g = int(input("4.kenar"))

if( a==b and a==c and a==d):
    print("kare")
elif(d==g and f==e ):
    print("dikdörtgen")
else:
    print("cesitkenar dortgen")