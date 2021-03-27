# Bankamatik Uygulaması

ahmetHesap = {
    "ad": "Ahmet Uçan",
    "hesapNo": "12345678",
    "bakiye": 10000,
    "ekHesap": 10000
}

mehmetHesap = {
    "ad":"Mehmet Emin Uçan",
    "hesapNo":"12348776",
    "bakiye": 156889,
    "ekHesap": 47464
}


def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimi = input("ek hesap kullanılsınmı? (e/h)")

            if ekHesapKullanimi == "e" :    
                ekHesapCekilen = miktar - hesap["bakiye"]
                hesap["ekHesap"] -= ekHesapCekilen
                hesap["bakiye"] = 0
                print(f"paranızı alabilirsiniz ek Hesabınzıda kalan bakiye : {hesap['ekHesap']}")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")        
        else:
            print("üzgünüz bakiyeniz yetersiz.")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}tl ve Ek hesap limitiniz ise {hesap['ekHesap']} tl bulunmaktadır. ")



paraCek(ahmetHesap, 15000) 

bakiyeSorgula(ahmetHesap)
print("********************")

paraCek(ahmetHesap, 5000)
bakiyeSorgula(ahmetHesap)  