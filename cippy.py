import requests, json, random, re, sys, time

userId = '';

appVersion = '3';
os = 'iPhone OS';
device = 'iPhone';
culture = 'DE';
osv = '7.1.1';

#Get Pushover notifications
pushoverId = ''
pushoverUser = ''
pushover = True

print "Cippy Bot (Python)"
msg = ""

def getData(url, sujetType):
	sujetData = '{"UserID":"'+userId+'","AppVersion":'+appVersion+',"RequestTime":"/Date('+'1402846713099'+'-0000)/","Operatingsystem":"'+os+'","Devicetype":"'+device+'","Culture":"'+culture+'","OperatingsystemVersion":"'+osv+'","SujetListType":'+sujetType+',}';
	headers = {
		"Host": "service.cippy.it",
		"Authorization": "4863f25d57230256b687a9428aeae615",
		"Content-Type": "application/json; charset=utf-8",
		"Accept": "*/*",
		"Accept-Language": "de, en, fr, zh-Hans, zh-Hant, ja, nl, it, es, es-MX, ko, pt, pt-PT, da, fi, nb, sv, ru, pl, tr, uk, ar, hr, cs, el, he, ro, sk, th, id, ms, en-GB, en-AU, ca, hu, vi, en-us;q=0.8",
		"Accept-Encoding": "gzip",
		"Connection": "keep-alive",
		"User-Agent": "it.firstavenue.cippy/1.6.4 (unknown, iPhone OS 7.1.1, iPhone, Scale/2.000000)"
	}
	res = requests.put(url, data=sujetData, headers=headers)

	data = json.loads(res.content)
	list = []
	for w in data['SujetListItems']:
		list.append(w['SujetObjectID'])
	print "ID: "+userId+"\tType: "+sujetType+"\t\tItems: "+str(len(list))
	return list

def rate(list):
	global msg
	sys.stdout.write('[0/'+str(len(list))+']')
	sys.stdout.flush()
	n=0;
	for ident in list:
		n=n+1
		sys.stdout.write('\r['+str(n)+'/'+str(len(list))+']')
		sys.stdout.flush()
		rand = (random.randint(0,2)+2)*2
		sujetData = '{"UserID":"'+userId+'","Voting":'+str(rand)+',"AppVersion":'+appVersion+',"RequestTime":"/Date('+'1402866751507'+'-0000)/","Operatingsystem":"'+os+'","Devicetype":"'+device+'","Culture":"'+culture+'","OperatingsystemVersion":"'+osv+'","SujetObjectID":"'+ident+'"}';
		headers = {
			"Host": "service.cippy.it",
			"Authorization": "f9ed1629daa0a7f2c3befe7eada5752a",
			"Content-Type": "application/json; charset=utf-8",
			"Accept": "*/*",
			"Accept-Language": "de, en, fr, zh-Hans, zh-Hant, ja, nl, it, es, es-MX, ko, pt, pt-PT, da, fi, nb, sv, ru, pl, tr, uk, ar, hr, cs, el, he, ro, sk, th, id, ms, en-GB, en-AU, ca, hu, vi, en-us;q=0.8",
			"Accept-Encoding": "gzip",
			"Connection": "keep-alive",
			"User-Agent": "it.firstavenue.cippy/1.6.4 (unknown, iPhone OS 7.1.1, iPhone, Scale/2.000000)",
			"Content-Type": "application/json"
		}
		res = requests.put("http://service.cippy.it/FARESTService/Vote", data=sujetData, headers=headers, allow_redirects=False)
		data = json.loads(res.content)
		msg = data['Message']
	print ''

rate(getData("http://service.cippy.it/FARESTService/GetSujetList", "1"))
#rate(getData("http://service.cippy.it/FARESTService/GetSujetList", "0"))
count = re.findall(re.compile(r'[1-9]+'), msg)

message = "You have now "+count[0]+" votes!"
if pushover:
	res = requests.post("https://api.pushover.net/1/messages.json", data="token="+pushoverId+"&user="+pushoverUser+"&message="+message)
	print res.status_code
print message
