
Lista wspieranych algorytmów:
```bash
openssl enc -ciphers
```

Odszyfrowanie pliku zaszyfrowanego aes-256-cbc z użyciem pliku pwd.pass jako klucza(wygenerowanego przez PBKDF2):
```agsl
openssl enc -d -aes-256-cbc -in cs.out -kfile=pwd.pass -pbkdf2
```

Odszyfrowanie tekstu w base64 zaszyfrowanego 3des
```agsl
echo U2FsdGVkX1/tgZuuECsrUdgIsheIfIy6MexYmLlFh5c= | openssl enc -des-ede3 -d -a -k 0e765937-123b-4d05-bcbe-de8f1c82148f -pbkdf2
```

Odszyfrowanie z uwzględnieniem iteracji
```agsl
echo U2FsdGVkX18LuPK2YF8MPCmacV4AIGApsUK7/1KUryI= | openssl enc -d -aes-256-ecb -k 28dea6c6-989a-4ed8-91ea-3e62361569f7 -base64 -iter 14958
```

Szukanie algorytmu którym coś zaszyfrowano (znając klucz) jako skrypt.sh
```bash
while read cipher;
do
    if [[ ${#cipher} -gt 8 ]] ; then
	    echo "------"
	    echo $cipher
	    openssl enc -d -a $cipher -in data.enc -kfile pwd.pass -pbkdf2
	    echo ""
    fi
    
done;
```

```bash
openssl enc -ciphers | tr ' ' '\n' | bash skrypt.sh
```
gdzie tr podmienia spacje na nowe linie

można też wyfiltrować przez grep
```bash
openssl enc -ciphers | tr ' ' '\n' | grep ecb | bash skrypt.sh
```