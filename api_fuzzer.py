# -*- coding: utf-8 -*-

'''
api_fuzzer.py

@author: Noirdemort

LICENSE: GPL v3
'''  

import random
import string
import argparse
import requests
from pprint import pprint


tags = {
		"<int>": ['0.0', 
					'', 
					'1.3', 
					'-2', 
					'9999999999999999999', 
					'-9999999999999999999999999999999999', 
					"hello", 
					'0003432'],
 
		"<str>": ["", 
					'4', 
					'0', 
					'-4', 
					"\x41\x42\x46\34"]
}


def _fuzzer(url):
	'''
		Creates fuzzed url with tags dict

		url: string

		returns: List of urls
	'''
	fizzy = []
	first_round = True
	for tag in tags:
		if first_round:
			for val in tags[tag]:
				fizzy.append(url.replace(tag, val))
			first_round = False
			continue

		if tag not in url:
			continue
		
		x = []
		for furl in fizzy:
			for val in tags[tag]:
				x.append(furl.replace(tag, val))
		fizzy = x.copy()

	sample = random.choice(fizzy)
	disc = sample.split('&')
	while len(disc) > 1:
		disc.pop(-1)
		fizzy.append('&'.join(disc))	
	return fizzy


pprint(_fuzzer("http://services/preferences?customerid=<int>&group_id=<str>"))


def deploy_hell(urls):
	'''
	Creates json consisting of ['cookies', 
								'elapsed',
								'encoding',
								'headers', 
								'is_permanent_redirect', 
								'is_redirect', 
								'json', 
								'status_code', 
								'text', 
								'url']

	urls: fuzzed list of urls

	:return none
	'''

	records = []
	for url in urls:
		r = requests.get(url)
		data =  {	
					'cookies': r.cookies, 
					'elapsed_seconds': r.elapsed.total_seconds(), 
					'encoding': r.encoding, 
					'headers': r.headers,
					'is_permanent_redirect': r.is_permanent_redirect, 
					'is_redirect': r.is_redirect, 
					'status_code': r.status_code, 
					'text': r.text, 
					'url': r.url
			}

		try:
			js = r.json()
			data['json'] = js
		except:
			pass

		records.append(data)
	
	with open("fuzzed_data.json", "w") as f:
		json.dump({"records": records})

	pprint(records)



# TODO: extend api fuzzing for different mime formats and extend for more complex cases.

if __name__=='__main__':
	parser = argparse.ArgumentParser(prog="A pi fuzzer", description="Api fuzzer to test and document fuzzed api response")
	parser.add_argument("--url", help="URL to fuzz", required=True)
	
	args = parser.parse_args()
	
	urls = _fuzzer(args.url)
	pprint(urls)
	
	deploy_hell(urls)
	
