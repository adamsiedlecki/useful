
Skrypt znajdujący nazwę funkcji haszującej
```python
import hashlib

s = "grJkfHDlGtl0oVPFkrZn".encode("utf-8")
hh = "e707361ee988ec956c7c8dd48d89dbe0835819c4f4b0ccbb6c1aaff5"

for alg in hashlib.algorithms_available:
        try:
                h = hashlib.new(alg)
                h.update(s)
                if h.hexdigest() == hh:
                        print("Alg: ", alg)
        except:
                print("Exception: ", alg)

```

kod uwierzytelniający hmac dla wiadomosci message i klucza x5GSOoGh1JHbgGAW0O0F.
```bash
echo -n "message" | openssl dgst -sha512 -hmac x5GSOoGh1JHbgGAW0O0F
```

Skrót pliku
```bash
openssl dgst -sha256 pass.txt 

SHA2-256(pass.txt)= be06f33bb375f856c34f9705ad9bd47100f02c88b0d120702644662e754fff0f
```