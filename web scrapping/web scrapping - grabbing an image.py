import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")

x = soup.select(".mw-file-element")

img_link = "https:" + x[1]["src"]

img = requests.get(img_link)

f = open("F:\\learning python\\sample_image.jpeg", "wb")
f.write(img.content)
f.close()

