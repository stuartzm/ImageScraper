from bs4 import BeautifulSoup as BS
import urllib.request
from PIL import Image, ImageOps, ImageDraw


maxpages = 2
links = []
images = []
for i in range(1, maxpages):

	url = 'urlWithPages' + str(i)

	page = urllib.request.urlopen(url).read().decode("utf-8")

	soup = BS(page, "lxml")
	for imgtag in soup.find_all("img"):
		if imgtag["src"][1] == "r":
			links.append(imgtag["src"])

#print(links)

for item in links:
	temp = item.split("%2F")
	images.append("directoryoflargeimages" + str(temp[-1]))

for item in images:
	print(item)

#then download that photo and fit it ontu a button
