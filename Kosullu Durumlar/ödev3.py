""" Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF


"""

vize1=int(input("birinci vize:"))
vize2=int(input("ikinci vize:"))
final=int(input("final notu:"))
gno = vize1*30/100 + vize2*30/100 + final*40/100
if (gno >=  90):
    print("AA")

elif (gno >=  85 ):
    print("BA")

elif (gno>=  80):
    print("BB")

elif (gno>=  75):
    print("CB")

elif (gno >=  70):
    print("CC")

elif (gno >=  65):
    print("DC")

elif (gno >=  60):
    print("DD")

elif (gno>=  55):
    print("FD")

elif (gno <  55):
    print("FF")

