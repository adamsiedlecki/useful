
W rockyou są hasła w plaintext, w pass.txt jest hasło do złamania w md5.
```bash
john --wordlist=rockyou.txt --format=raw-md5 pass.txt
```

## ZIP

Jest plik .zip zabezpieczony hasłem
```bash
zip2john 63752542-6756-4973-907f-53f78a39f56e.zip >  zip.hash
```

Łamanie hasła (można użyć --wordlist=rockyou.txt)
```bash
john zip.hash
```

Odpakowanie:
```bash
unzip 63752542-6756-4973-907f-53f78a39f56e.zip
```

Można zobaczyć już złamane hasło:
```bash
john zip.hash --show 
```