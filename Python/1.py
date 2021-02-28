import requests
from bs4 import BeautifulSoup

URL = 'https://www.cossa.ru/imarketing/261951/'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}

def get_html (url, params = None):
	r = requests.get(url, headers = HEADERS, params = params)
	return r

def get_content(html):
		soup = BeautifulSoup(html, 'html.parser')

def pars ():
	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
	else:
		print('ERROR!')	

pars()
