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

![anaekran1](https://user-images.githubusercontent.com/36503536/70397615-d604b900-1a24-11ea-9372-a8fb3d7d19cb.png)
![anaekran3](https://user-images.githubusercontent.com/36503536/70397616-d604b900-1a24-11ea-9cad-f3d1d387d489.png)
![querydetail4](https://user-images.githubusercontent.com/36503536/70397617-d604b900-1a24-11ea-83fc-2b0e4a3516d6.png)
![querydetail5](https://user-images.githubusercontent.com/36503536/70397618-d69d4f80-1a24-11ea-929b-ec258f9fbd7f.png)
![querysecren2](https://user-images.githubusercontent.com/36503536/70397619-d735e600-1a24-11ea-96c7-4394ff09eb5d.png)

## Foursquare Api  

Belli türde mekan kategorisinde   :rose: :school: :pizza: :microphone: :swimmer: :airplane:  :coffee: :hospital: :ferris_wheel: , istenilen konum :tr: dahilinde sorgulama yapılmaktadır. Bu sorgulamaya istenilen limit eklenerek sorgulama sonucu bir tablo halinde listelenmektedir.
Geliştiricilere özel tanımlanan  Foursquare Apı'sinin geliştiriciye özel CLIENT_ID ve CLIENT_SECRET tanımlar. Bu anahtarlar, uygulamayı kullanıcıların hesaplarına bağlamak için önemlidir.

## Android Studio

![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397370-ba98ae80-1a22-11ea-9249-32f425c738ad.jpg)

![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397368-ba001800-1a22-11ea-9820-4fa73befb135.jpg)
![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397380-c71d0700-1a22-11ea-84e5-e1e0f6530331.jpg)

![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397369-ba98ae80-1a22-11ea-8a0e-01441523cb19.jpg)
![queryformandroid1](https://user-images.githubusercontent.com/36503536/70397381-c71d0700-1a22-11ea-9648-27c0644155ed.jpg)

## Heroku 
Heroku bulut bir uygulama platformudur. Geliştirdiğim projeyi Heroku ile yayına aldım. 
Heroku üzerinde database olarak Postgresql kullanma zorunluluğu vardır.

