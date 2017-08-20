import json
import re
import random
from ast import literal_eval

with open("original/ads.txt", "r") as data:
    i = 0
    newData = ""
    for line in data:
        # print(line)
        newAd = {}
        jsondata = json.loads(line)
        newAdId = jsondata["adId"] + 2000 + i
        newTitle = jsondata["title"].replace(",", "")
        newTitle = newTitle.replace("-", "")
        newTitle = newTitle.replace(".", "")
        newTitle = re.sub("\s+", " ", newTitle).lower()
        newKeyWords = jsondata["keyWords"]
        for title in newTitle.split(" "):
            newKeyWords.append(title)
        newPrice = random.randint(1, 100000)
        newQuery = jsondata["query"].lower()

        newAd["category"] = jsondata["category"]
        newAd["query"] = newQuery
        newAd["campaignId"] = jsondata["campaignId"]
        newAd["title"] = newTitle
        newAd["price"] = newPrice
        newAd["relevanceScore"] = jsondata["relevanceScore"]
        newAd["brand"] = jsondata["brand"]
        newAd["pClick"] = jsondata["pClick"]
        newAd["thumbnail"] = jsondata["thumbnail"]
        newAd["costPerClick"] = jsondata["costPerClick"]
        newAd["bidPrice"] = jsondata["bidPrice"]
        newAd["query_group_id"] = jsondata["query_group_id"]
        newAd["position"] = jsondata["position"]
        newAd["keyWords"] = newKeyWords
        newAd["adId"] = newAdId
        newAd["detail_url"] = jsondata["detail_url"]
        newAd["rankScore"] = jsondata["rankScore"]
        newAd["qualityScore"] = jsondata["qualityScore"]

        newData = newData + str(newAd) + "\n"
        i = i + 1
print(newData)

with open("cleaned/cleanedAds.txt", "w") as newDataFile:
    newDataFile.write(newData)
    newDataFile.close()


