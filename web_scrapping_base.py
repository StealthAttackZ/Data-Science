from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = ''

#opening up a connection, grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Brand, Product\n"
f.write(headers)



for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    f.write(brand + "," + product_name.replace(",", "|") + "\n")

f.close()


