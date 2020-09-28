print("""
faktöriyel bulma
cıkmak için 'q' a basın
""")
while True:
    sayı=input("sayı:")
    if(sayı=="q"):
        print("programdan cıkılıyor..")
        break
    else:
        sayı=int(sayı)

        faktöriyel=1

        for i in range(2,sayı+1):
            faktöriyel*= i
        print("faktöriyel",faktöriyel)