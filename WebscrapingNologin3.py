from bs4 import BeautifulSoup
import requests
from lxml import etree


def NigeriaSuya(keywordsearch):
    Recipelist = []
    # the url you want to extract from
    url = "https://www.epicurious.com/search/" + keywordsearch
    response = requests.get(url=url)
    if response.status_code == 200:
        try:
         #  to check the returned content and what type of coding chracters if there is need for decoding
            # print(response.content)
            # ------ use to decode content of the website
            # webpagecontent = response.content.decode("utf-8")
            #  to find content from a web page is rendered by Class Beautiful calling either  lxml or html5lib
            page_soup = BeautifulSoup(response.content, "lxml")
            Find_nigeriasuya_tag = page_soup.find_all(
                "article", {"class": "recipe-content-card"})
            for recipes in Find_nigeriasuya_tag:
                recipes_name = recipes.find("a").get_text()
                recipes_link = "http://www.epicurious.com" + \
                    recipes.find("a").get("href")
                try:
                    recipes_description = recipes.find(
                        "p", {"class": "dek"}).get_text()
                except:
                    recipes_description = " "
                Recipelist.append(
                    (recipes_name, recipes_link, recipes_description))

        except:
            return Recipelist
        return Recipelist


def recipescrapper(url2):
    delicacydict = {}
    responses = requests.get(url=url2)
    page_soup2 = BeautifulSoup(responses.content, "lxml")
    ingredientList = []
    prepstep = []
    findingredtags = page_soup2.find_all("li", {"class": "ingredient-group"})
    for ingredients in findingredtags:
        ingredient_name = ingredients.find("li").get_text()
        ingredientList.append(ingredient_name)

        findparatags = page_soup2.find_all(
            "li", {"class": "preparation-group"})
    for preps in findparatags:
        preps_name = preps.find("li").get_text().strip()
        prepstep.append(preps_name)

        delicacydict["Delingredients"] = ingredientList
        delicacydict["Preparation"] = prepstep
    return (delicacydict)


def all_receipes_details(keywordsearch):
    final_result_list = []
    advancekey = NigeriaSuya(keywordsearch)
    for recipes in advancekey:
        # Adjust based on the lis been returned
        myreturndic = recipescrapper(advancekey[0][1])
        myreturndic["name"] = recipes[0]
        myreturndic["description"] = recipes[2]
        final_result_list.append(myreturndic)
    return final_result_list


keywordsearch = input("Enter your search\n")
print(all_receipes_details(keywordsearch))
