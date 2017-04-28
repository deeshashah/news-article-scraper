from scraping.scraper import Scraper
import requests
import json
import pprint
# Fetch the json data from the newsapi.
r = requests.get('https://newsapi.org/v1/articles?source=mirror&apiKey=6df0769e0d6244aaa00768c02f123fb2')

#Create a empty dictionary
response_dictionary = {}

# response_dictionary["status"] = r

# Here the source of the news article is "Mirror"
response_dictionary["source"] = "mirror"

#The json data fetched from API is to be stored in a variable.
#It is in the following format :
apiFetchedData = json.loads(r.text)

pprint.pprint(apiFetchedData) 
# print data["articles"]
list_of_urls = []
article_data = []
main_dict = {}
i = 0;
#We go through information of each article provided by the API and using the url we scrape the data and store it in new JSON format. 

for item in apiFetchedData["articles"]:
    #Creation of a sub dictionary to store information about each article.
    mid_dictionary = {}
    
    #The title maybe present in encoded format so cleaning it. 
    if(type(item["title"])=="unicode"):
        title = unicodedata.normalize('NFKD', item["title"]).encode('ascii','ignore')
    else : 
        title = item["title"]
    
    print title
    
    mid_dictionary["title"] = title

    #In order to fetch the data from the article url, Scraper code has been written. sc is the object of the Scraper class.
    sc = Scraper()
    #Using the url, article is scraped and added in new dictionary.
    mid_dictionary["data"] = sc.scrape_mirror(item["url"])
    article_data.append(mid_dictionary)
    mid_dictionary["image"] = (item["urlToImage"])
    print mid_dictionary["image"]
        
    print mid_dictionary
    main_dict["article_"+str(i)] = mid_dictionary
    i = i+1
    

response_dictionary["articles"] = article_data
print response_dictionary