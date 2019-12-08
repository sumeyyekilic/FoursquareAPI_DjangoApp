#  :earth_asia: Mekan Arama Uygulaması : Django, Android

Foursquare Api kullanılarak Django freamework'ü ile bir [web uygulaması](https://github.com/sumeyyekilic/FoursquareAPI_DjangoApp/blob/master/Images/android/QueryFormAndroid1.jpg) geliştirildi.Android Studio ile mobil uygulaması yapıldı.
 

 - Mekan Sorgulama formu ile bilgiler girilerek istenilen mekan türüne ait girilen limit kadar sonuçlar getirilmektedir. 
 - ilk olarak aranan sonuçlar tablo ile listenmektedir. 
 - Sorgu sonucu o mekanda anlık aktif bulunan kullanıcı sayısı ve mekan adresi getirildi. 
 - Mekan paramteresinin id bilgisi ile o mekanın detay bilgilerine erişilmektedir. 
 - Arama sonucunda listelenen mekan isimlerinden birine tıklanıldığında, kullanıcıyı o mekanın detay sayfasına yönlendirilmesi yapıldı. 
 - Detay bilgilerinde mekanın fotoğrafı  :ferris_wheel: adresi :house_with_garden: telefon :phone: twitter :iphone: rating :chart_with_upwards_trend: mekanın beğenisi :ok_hand: ve ilk beş kullanıcıya ait mekan ile ilgili yorumlar :pencil2: .
 - Her yorum kullanıcının profil fotoğrafı; :woman: :man: ad ve soyad bilgileriyle birlikte :name_badge: gelmektedir. (kullanıcı limitini api tarafında belirledim).

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

![anaEkran1](https://github.com/sumeyyekilic/FoursquareAPI_DjangoApp/blob/master/Images/web/anaEkran1.png width="200" height="200")

## Foursquare Api  

Belli türde mekan kategorisinde   :rose: :school: :pizza: :microphone: :swimmer: :airplane:  :coffee: :hospital: :ferris_wheel: , istenilen konum :tr: dahilinde sorgulama yapılmaktadır. Bu sorgulamaya istenilen limit eklenerek sorgulama sonucu bir tablo halinde listelenmektedir.
Geliştiricilere özel tanımlanan  Foursquare Apı'sinin geliştiriciye özel CLIENT_ID ve CLIENT_SECRET tanımlar. Bu anahtarlar, uygulamayı kullanıcıların hesaplarına bağlamak için önemlidir.

## Android Studio

![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397370-ba98ae80-1a22-11ea-9249-32f425c738ad.jpg)

## Heroku 
Heroku bulut bir uygulama platformudur. Geliştirdiğim projeyi Heroku ile yayına aldım. 
Heroku üzerinde database olarak Postgresql kullanma zorunluluğu vardır.

