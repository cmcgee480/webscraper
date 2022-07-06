import requests
from bs4 import BeautifulSoup

URL = "https://www.airbnb.co.uk/rooms/20669368?source_impression_id=p3_1657058749_93v5O6w%2B22u0g%2F6u"
get_url = requests.get(URL)
get_text = get_url.text
soup = BeautifulSoup(get_text, "html.parser")
results = soup.find(id="site-content")
propertyTitle= soup.select('h1._fecoyn4')[0].text.strip()
space = "\n"
print(space)
print(propertyTitle)
propertyType = soup.select('h2._14i3z6h')[0].text.strip()
print(propertyType)
numOfBedBaths = soup.find('ol', class_='l7n4lsf dir dir-ltr').get_text()
print(numOfBedBaths)
amens= "Amenities include: "
print(amens)
amens = soup.find('div', class_='_1byskwn').get_text(separator="\n")
print(amens)
space = "\n\n"
print(space)

URL = "https://www.airbnb.co.uk/rooms/50633275?source_impression_id=p3_1657066759_WKuotiUXZywa9RQ4"
get_url = requests.get(URL)
get_text = get_url.text
soup = BeautifulSoup(get_text, "html.parser")
propertyTitle= soup.select('h1._fecoyn4')[0].text.strip()
space = "\n"
print(space)
print(propertyTitle)
propertyType = soup.select('h2._14i3z6h')[0].text.strip()
print(propertyType)
numOfBedBaths = soup.find('ol', class_='l7n4lsf dir dir-ltr').get_text()
print(numOfBedBaths)
amens= "Amenities include: "
print(amens)
amens = soup.find('div', class_='_1byskwn').get_text(separator="\n")
print(amens)
space = "\n\n"
print(space)














