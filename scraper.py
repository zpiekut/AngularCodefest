from lxml import html
import requests
from pymongo import MongoClient
import re

client = MongoClient('mongodb://localhost/')
db = client.codefest

page = requests.get('http://www.pittsburghparent.com/Calendar/')
tree = html.fromstring(page.text)
try:
	titles = tree.xpath('//div[@id="calendar-body"]/table/tr/td/h3/a/text()')
	links = tree.xpath('//div[@id="calendar-body"]/table/tr/td/h3/a/@href')
	tempDates = tree.xpath('//div[@id="calendar-body"]/table/tr/td/h4/text()')
	for ii in range(0, len(titles)):
		matchMonth = re.findall('[\w]*', tempDates[ii])
		matchYear = re.findall('[\d*]+', tempDates[ii])
		# print matchMonth
		# print matchYear
		if ( matchMonth[0] == 'Feb' ):
			date = '02'
		else:
			date = matchMonth[0]
		date = matchYear[1] + '-' + date + '-' + matchYear[0]
		# print date
		event = {"title": titles[ii],
		"link": links[ii],
		"start": date}
		post_id = db.events.save(event)

except Exception as exc:
	print exc

client.disconnect()