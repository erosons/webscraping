from bs4 import BeautifulSoup
import requests
from lxml import etree


def NigeriaSuya(keywordsearch):
    Niglist = []
    # the url you want to extract from
    url = "https://www.epicurious.com/search/" + keywordsearch
    response = requests.get(url=url)
    if response.status_code == 200:
     #  to check the returned content and what type of coding chracters if there is need for decoding
        # print(response.content)
        # ------ use to decode content of the website
        # webpagecontent = response.content.decode("utf-8")
        #  to find content from a web page is rendered by Class Beautiful calling either  lxml or html5lib
        page_soup = BeautifulSoup(response.content, "lxml")
        Find_nigeriasuya_tag = page_soup.find(
            "article", {"class": "recipe-content-card"})
        Find_nig_suya_anch = Find_nigeriasuya_tag.find("a")
        To_get_link = "http://www.epicurious.com" + \
            Find_nig_suya_anch.get("href")
        nigUrl = To_get_link
        if nigUrl not in Niglist:
            Niglist.append(nigUrl)
            url2 = nigUrl
            responses = requests.get(url=url2)
            page_soup = BeautifulSoup(responses.content, "lxml")
            Find_nigeriasuya_tag_ingridents = page_soup.find(
                "div", {"class": "recipe-and-additional-content"})
            ingredientlist = Find_nigeriasuya_tag_ingridents .find(
                "li").get_text()
            if ingredientlist not in Niglist:
                Niglist.append(ingredientlist)
            else:
                print("check your anchors")
            return Niglist
    else:
        print("check your url")


keywordsearch = input("Enter your search term\n")
print(NigeriaSuya(keywordsearch))
