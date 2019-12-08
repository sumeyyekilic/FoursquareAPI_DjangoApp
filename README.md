#  :earth_asia: Mekan Arama Uygulaması : Django, Android

Foursquare Api kullanılarak Django freamework'ü ile bir web uygulaması geliştirildi.Android Studio ile mobil uygulaması yapıldı.
 
Mekan Sorgulama formu ile bilgiler girilerek istenilen mekan türüne ait girilen limit kadar sonuçlar getirilmektedir. 
ilk olarak aranan sonuçlar tablo ile listenmektedir. 
Sorgu sonucu o mekanda anlık aktif bulunan kullanıcı sayısı ve mekan adresi getirildi. 
Mekan paramteresinin id bilgisi ile o mekanın detay bilgilerine erişilmektedir. 
Arama sonucunda listelenen mekan isimlerinden birine tıklanıldığında, kullanıcıyı o mekanın detay sayfasına yönlendirilmesi yapıldı. 
Detay bilgilerinde mekanın fotoğrafı, adresi, telefon, twitter, rating, mekanın beğenisi ve ilk beş kullanıcıya ait mekan ile ilgili yorumlar o kullanıcının profil fotoğrası , ad ve soyad bilgileriyle gelmektedir. 
(kullanıcı limitini api tarafında belirledim).

### Uygulamada Kullanılan Teknolojiler  :link:

- Django
- Foursquare API
- Android Studio
- Heroku
- Bootstrap 3 

###  Django

Mekan Sorgulama uygulamasının [Django Uygulaması](https://github.com/sumeyyekilic/VenueQuery/tree/master/dfas) klasörü içerisindedir. 
Django ile yazılan kaynak kodlar yer alır. 

#### Mekan Sorgulama Web Uygulamasının Ekran Görüntüsü
![](https://github.com/sumeyyekilic/FoursquareAPI_DjangoApp/blob/master/Images/android/QueryFormAndroid1.jpg 200x100)

## Foursquare Api  

Belli türde mekan kategorisinde   :rose: :school: :pizza: :microphone: :swimmer: :airplane:  :coffee: :hospital: :ferris_wheel: , istenilen konum :tr: dahilinde sorgulama yapılmaktadır. Bu sorgulamaya istenilen limit eklenerek sorgulama sonucu bir tablo halinde listelenmektedir.
Geliştiricilere özel tanımlanan  Foursquare Apı'sinin geliştiriciye özel CLIENT_ID ve CLIENT_SECRET tanımlar. Bu anahtarlar, uygulamayı kullanıcıların hesaplarına bağlamak için önemlidir.

## Android Studio

android ekran görüntüsü ekle
