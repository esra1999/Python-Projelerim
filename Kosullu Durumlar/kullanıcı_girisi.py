print("""
*******************
Kullanıcı Girişi

*******************
""")

sys_kullanıcı_adı="esra"
sys_parola="12345"

kullanıcı_adı=input("kullanıcı adınız:")
parola=input("parolanız:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola == parola):
    print("Basarı ile giriş yaptınız.")
elif( kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parolanız hatalı")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı adınız hatalı.")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı adınız ve parola hatalı.")