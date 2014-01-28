from lxml import html
import requests
import unicodecsv as csv

urls = {'m': "http://www.rodina.cz/scripts/jmena/default.asp?muz=1", 'f': "http://www.rodina.cz/scripts/jmena/default.asp?muz=0"} 
names = {} 
for key in urls:
    page = requests.get(urls[key])
    tree = html.fromstring(page.text)
    names[key] = tree.xpath('//table[@class="jmena_vse"]//a/text()')
    with open("jmena_" + key + ".csv", 'wb') as fl:
        writer = csv.writer(fl, encoding="UTF-8")
	for row in names[key]:
		writer.writerow(row)
        #writer.writerows(names[key])
"""
print "Male names: ", names['m']
print "Female names: ", names['f']
print "Ambiguous names: ", set(names['m']) & set(names['f'])
"""
