import requests
import bs4

author_set = set()

for i in range (1,11):
    res = requests.get(f"https://quotes.toscrape.com/page/{i}")
    soup = bs4.BeautifulSoup(res.text, "lxml")

    authors = soup.select(".author")

    #author_set.append(f"---------- Page {i} ----------")

    for author in authors:
        author_set.add(author.text)


print("\n *** LIST OF AUTHORS ***")

for a in author_set:
    print(a)
