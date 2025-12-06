def islem_yap(secim, sayi1, sayi2):
    if secim == '1':
        return sayi1 + sayi2
    elif secim == '2':
        return sayi1 - sayi2
    elif secim == '3':
        return sayi1 * sayi2
    elif secim == '4':
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem"

print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("Seçiminiz (1/2/3/4): ")
s1 = float(input("Birinci sayı: "))
s2 = float(input("İkinci sayı: "))

print("Sonuç:", islem_yap(secim, s1, s2))
