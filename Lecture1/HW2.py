sira = int(input("Kaçıncı Sıradaki Sayi ? :"))
a = 0
b = 1
if sira <=0:
    print ("Sira Değeri 0'dan Küçük Girilemez.")
else :
    for i in range (1,sira):
        c = a
        a = b
        b = c + b
    print("Fibonacci Sayı Dizisinin",sira,"Numaralı Sayısı : ",a)