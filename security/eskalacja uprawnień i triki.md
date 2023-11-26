-t to tryb interaktywny

```agsl
ssh -t user@192.168.10.10 base64
```


Docelowa lokalizacja:
```agsl
scp nazwa_pliku użytkownik@adres_serwera:docelowa_lokalizacja
```

SUID powoduje uruchomienie pliku z uprawnieniami właściciela, niezależnie od tego,
jaki użytkownik uruchamia ten plik.

GUID powoduje uruchomienie pliku z uprawnieniami grupy, niezależnie od tego, do jakiej
grupy należy użytkownik, który uruchamia ten plik

Wyszukiwanie po uprawnieniach:
```agsl
find . -perm 0667
```

Sticky bit (restricted deletion flag - flaga ograniczonego usuwania) jest uprawnieniem,
które uniemożliwia usunięcie bądź zmianę nazwy pliku przez osoby, które nie są wła-
ścicielem pliku. 

Używane przez programy pliki można podejrzeć w prosty sposób. Aby to zrobić, należy
najpierw przejść do folderu /proc. Jest to folder, który zawiera informacje o aktualnej
konfiguracji systemu i sprzętu oraz informacje o uruchomionych procesach.


Zdalny odczyt secretu:
```agsl
ssh alice@10.0.4.127 -t " cat  /home/alice/secret.txt"
```

Znajdowanie wszystkich programów SUID:
```agsl
find . -perm /4000 
```

Użycie php do hostowania danych roota:
```agsl
php7.4 -S localhost:8000 -t /root
wget localhost:8000/secret.txt
```

Będąc w programie more można uruchomić vi (klawisz v) oraz otworzyć inny plik (:e secret.txt)

Odczytanie pliku usuniętego, ale jakiś proces nadal go używa:
- trzeba zidentyfikować PID procesu
- /proc/PID/fd$ ls