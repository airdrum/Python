
import telnetlib

HOST = "192.168.2.254"
user = 'root'
password = ''

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"wl -i wl1 rate\n")
tn.write(b"wl -i wl1 nrate\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))