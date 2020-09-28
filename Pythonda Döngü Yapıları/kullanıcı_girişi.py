print("""Kullanıcı Giriş Ekranı""")
sys_kullanıcı_adı="eesra"
sys_parola="12345"
giriş_hakkı=3
while True:

 kullanıcı_adı = input("kullanıcı adı:")
 parola = input("parola:")
 if(sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("kullanıcı adı hatalı...")
        giriş_hakkı -= 1
 elif(sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
        print("parola adı hatalı...")
        giriş_hakkı -= 1
 elif(sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
            print("kullanıcı adı ve parola hatalı...")
            giriş_hakkı -= 1
 else:
        print("başarı ile giriş yaptınız...")
        break
 if (giriş_hakkı==0):
         print("giriş hakkınız kalmadı..")
         break

