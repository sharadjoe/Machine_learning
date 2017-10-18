
import csv
import urllib2
import requests
from bs4 import BeautifulSoup

url = 'http://www.tradeabook.in/cec_alp/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()
