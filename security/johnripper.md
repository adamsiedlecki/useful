
W rockyou są hasła w plaintext, w pass.txt jest hasło do złamania w md5.
```
john --wordlist=rockyou.txt --format=raw-md5 pass.txt
```