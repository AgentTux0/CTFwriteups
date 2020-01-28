#! python3

import requests
import re

"""Regex"""
url_regex = re.compile(r'url=/([\w-]+)"')
flag_regex = re.compile(r'(rtcp{[\w,-]+})')

def content(site):
	oTag = site.find('<main')
	cTag = site[oTag:].find('</main>')
	content = site[oTag:cTag]
	return content

def getUrl(content):
	try:
		page = url_regex.findall(content)[0]
		return page
	except:
		return None


def getFlag(content):
	try:
		flag = flag_regex.findall(content)[0]
		return flag
	except:
		return None

i = 0
pList = ['uwu']
while True:
	print(f'[*] Searching page {i}: {pList[i]}...')
	page = pList[i]
	r = requests.get(f'https://riceteacatpanda.wtf/{page}').text
	r = content(r)
	page = getUrl(r)
	flag = getFlag(r)
	if flag:
		print(f'[!] Flag found: {flag}')
		break
	elif page:
		pList.append(page)
		i += 1
		continue
	else:
		print('Something went wrong...')
