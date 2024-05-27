YusufHesap = {
    'ad': 'Yusuf Yüksel',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar   
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(YusufHesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı? (e/h):')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirisiniz.')
                bakiyeSorgula(YusufHesap)
            elif ekHesapKullanimi == 'h':
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgula(YusufHesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır")


print('----------------------------')

paraCek(YusufHesap, 5000)

print('----------------------------')

