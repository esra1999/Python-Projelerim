print("""
******************
atm makinesi 
1- bakiye sorgulama 
2-para yatırma
3-para cekme
programdan cıkmak için 'q'ya basın..
*******************
""")
bakiye=1000
while True:
    işlem=input("işlemi seciniz")

    if (işlem == "q"):
        print("yine bekleriz")
        break

    elif(işlem==("1")):
        print("bakiyeniz:{} tldir".format(bakiye))

    elif(işlem==("2")):
        miktar=int(input("miktarı giriniz:"))
        bakiye+=miktar

    elif(işlem==("3")):
        miktar=int(input("miktarı giriniz:"))

        if(bakiye - miktar < 0):
            print("böyle bir miktar cekemezsiniz..")
            continue
            bakiye-=miktar



    else:
        print("gecersiz işlem..")

