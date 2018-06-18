# PythonAGHWebsite

Jest to strona napisana w Django (przy użyciu PyCharm). Główne pliki znajdują się w folderze spoldzielnia oraz templates.
W templates przechowuje wszytkie widoki html natomiast w spoldzielnia znajduje sie views oraz models.
Views odpowiada za widoki i je kontroluje natomiast w models jest zapisany szkielet bazy danych.
Ponadto w zad3 znajduje się przykładowa już wypełniona baza.
Strona zawiera funkcjonalność CRUD dla każdych z 3 modeli: flats(mieszkania), residents(mieszkańcy), payments(opłaty).
Modele zależne są od siebie: flat has many residents, resident has many payments.
Ponadto w modelu residents atrybut NIN(National Identification Number- PESEL) jest unikalny toteż przy dodaniu/edycji tego samego NIN nic się nie zmienia.
