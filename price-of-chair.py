import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.in/s?hidden-keywords=B07DJCYBVK%7CB078BN55WZ%7CB078BN2H3R%7CB077PWK5BY%7CB077Q42GDF&pf_rd_i=1320006031&pf_rd_i=1320006031&pf_rd_i=21439725031&pf_rd_m=A1K21FY43GMZF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=9cb16cb4-e1a1-410a-bec9-aa3581fe1ac8&pf_rd_p=previewPlacement_center-1&pf_rd_p=previewPlacement_center-1&pf_rd_r=10ZR0JP6JM2RWZ280ESD&pf_rd_r=APKGQJ6BNDWJPBT2WH11&pf_rd_r=ZNBDFC1V18RJQP55JJRV&pf_rd_s=center-1&pf_rd_s=center-1&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_t=101&pf_rd_t=101&ref=nb_sb_noss")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "a-price-whole"})
string_price = print(element.text.strip())

price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 200:
    print("You can buy the chair")
    print("price of chair is: {}".format(price))
else:
    print("Price is not affordable for you")
    print("Price of chair is: {}".format(price))
# <span class="a-price-whole">54,999</span>
print(request.content)
