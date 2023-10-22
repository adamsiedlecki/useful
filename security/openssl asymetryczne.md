
### RSA private key
```agsl
openssl genrsa -out key.pem 4096
```

### RSA public from private w formacie PEM
```agsl
openssl rsa -in key.pem -pubout -out public.pem
```

### Wyświetlenie fizycznej zawartości klucza
```
openssl rsa -in key.pem --text
```

----------------
Eliptyczne

Lista krzywych
```agsl
openssl ecparam -list_curves
```

Prywatny
```
openssl ecparam -name prime256v1 -genkey -out key.pem
```
Publiczny na podstawie prywatnego
```
openssl ec -in key.pem -outform PEM -pubout -out public.pem
```

Szyfrowanie publicznym w trybie OAEP i konwertowanie do base64 w jednej linii (w0)
```
openssl pkeyutl -encrypt -pkeyopt rsa_padding_mode:oaep -pubin -inkey public.pem -in key.txt | base64 -w0
```

-------------------------------
### Urząd certyfikacji

1. Utworzneie klucza
```agsl
openssl genrsa -out ca.key 2048
```

Utworzenie certyfikatu
```
openssl req -new -x509 -key ca.key -out ca.crt
```

Wyświetlenie szczegółów certyfikatu:
```agsl
openssl x509 -in ca.crt -text
```

Wykonanie CSR - Certificate Signing Request
```
openssl x509 -req -in cert.csr -CAkey ca.key -CA ca.crt  -out output.crt
```

---------------

### PGP

Generowanie pary kluczy
```agsl
gpg --generate-key
```

Lista kluczy
```agsl
gpg --list-keys
```

Eksport klucza publicznego jako PEM (opcja armor)
```
gpg --export --armor Miller Maxwell
```

Import klucza publicznego
```agsl
gpg --import pub.pem
```

Zaszyfrowanie tekstu z pliku kluczem publicznym
```agsl
gpg --encrypt --recipient odbiorca data.txt
```

Zaszyfrowanie potoku bez znaku końca linii
```agsl
echo -n PHW2QMeTIY4wNmtxUNyB | gpg --encrypt --output a.encrypted --armor --recipient odbiorca
```

Odszyfrowanie pliku encrypted - gpg pyta o hasło
```
gpg --decrypt encrypted
```

