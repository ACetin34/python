# HW1

arr ve temarr adında iki array oluşturulur.arr 100 elemanlı,temparr 99 elemanlıdır.for döngüsü kullanılarak arr arrayinin içine 1'den 100'e kadar sayılar girilir.arr[0] boş kalır random olarak 1,99 arası bir değer alır.Random komutu kullanılarak arraydeki elemanların yerleri değiştirilir.for döngüsü kullanılarak temparr içine atılan elemanlar kontrol edilir eğer sayı "None" değerine gelirse işlem devam eder fakat sayı "None" olmayan bir değere gelirse işlem tamamlanır ve Duplicate Sayı bulunur.

# HW2
Kullanıcıdan klavyeden input girilmesi istenir.Klavyeden girilen input değeri "lower" komutu ile lowercase işlemi yapılır,eğer yapılmazsa ASCII tablosundaki karakter farkından dolayı duplicate harfte yazılır."tmp" isminde bir array oluşturulur.Klavyeden girilen input array'in içine aktarılır.İki değer if-else ile karşılaştırılır duplicate olan harf yazılmaz.

# HW3
Input girilir."lower" komutu ile lowercase işlemi yapılır."arr" ve "arr2" isminde iki array oluşturulur.Girilen input arraylerin içine aktarılır."ort" ile girilen inputun ortasındaki karakter bulunur.Eğer girilen input'un ortasındaki değer virgüllü sayı ise int ile virgül ortadan kaldırılır."for" döngüsü 0'dan başlayıp "ort" değerine kadar devam eder karakterlerin yerlerini değiştirip kontrol eder eğer karakterler eşit ise "Palindromdur." değilse "Palindrom değildir." çıktısını verir.

# HW4
"reverse" isminde method tanımlanır."x" değişkeni "str"nin length değerine eşitlenir."arr" isminde boş bir array tanımlanır.For döngüsü "str"nin length değeri kadar tekrar eder.Input'un "ort" değeri bulunur eğer çıkan sayı virgüllü ise int ile virgülü atarız.Tekrardan bir "for" döngüsü oluştururuz ve kelimenin "ort" değerine kadar bir baştan bir sondan karakterlerin yerini değiştirmesini isteriz."join" ile arrayin içindeki karakterlerin birleşik olarak yazılmasını sağlarız."return" ile methodu tamamlarız.Input girilmesini isteriz ve bu input'u "reverse methodu" ile işleme alırız.

# HW5
app ve ext isminde iki method oluştururuz."app" methoduna "arr,arr2" adında iki adet array tanımlarız."arr" arrayi sabit "arr2" arrayi ise input değeri içine aktarır."arr2" inputu içine yazdıktan sonra "arr2" arrayi "arr" arrayine append olur.

ext methodu da aynı şekilde çalışır fakat "arr2" inputu içine yazdıktan sonra "arr2" arrayini "arr" arrayine expend ederiz.

İşlemler tamamlandıktan sonra append ve extend arasındaki işlem zamanı farkını ve "arr"ye append ve extend olmuş değeri ekrana yazdırırız.
