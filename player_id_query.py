import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}


player = "Modric"
data=requests.get("https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={}&x=0&y=0".format(player), headers=headers)

soup = BeautifulSoup(data.text, "lxml")
# print(soup)

table = soup.find("table", { "class" : "items" })
print(table)

for row in table.find_all("table", { "class" : "inline-table" }):

    hrefs = row.find("a", {"class" : "spielprofil_tooltip"})
    print(hrefs)    # hrefs is empty. there is no such title in the source page

    print("player : {}".format(hrefs['title']))
    print("url : {}".format(hrefs['href']))