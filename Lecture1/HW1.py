f = int(input("İşlem Kaç Defa Tekrar Etsin"))
for i in range (0,f) :
    a = int(input("1. Sayıyı Girin :"))
    b = int(input("2. Sayıyı Girin :"))
    islem = input("İşlem Operatörü Seçiniz (+,-,*,/):")


    if islem == "+" :
        print (a+b)

    elif islem == "-" :
        print (a-b)

    elif islem == "*" :
        print (a*b)

    elif b==0 :
        print ("Sıfır ile bölme işlemi yapamazsınız.")
    elif islem =="/" :
        print (a/b)

    elif islem == "exit":
        break
    else:
        print("İşlem operatörü giriniz")
