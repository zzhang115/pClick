import sys
import json

if __name__ == '__main__':
    #Device IP, Device id,Session id,Query,AdId,CampaignId,Ad_category_Query_category(0/1),clicked(0/1)
    #use following feature to generate click Log
    #IP, device_id, AdId,QueryCategry_AdsCategory,Query_CampaignId, Query_AdId
    adInputFileDir = sys.argv[1]
    queryAdInputDir = sys.argv[2]
    campWeightDir = sys.argv[3]
    adWeightDir = sys.argv[4]
    campCategoryDir = sys.argv[5]
    campIdAdIdDir = sys.argv[6]
    userInputDir = sys.argv[7]
    clickOutputDir = sys.argv[8]

    adList = []
    adIdQuery = {}
    queryCampAd = {}
    campWeight = {}
    adWeight = {}
    campCategory = {}
    campIdAdId = {}

    with open(adInputFileDir, "r") as ads:
        for ad in ads:
            # json.loads is for txt file, not for json file
            adEntry = json.loads(ad)
            adList.append(adEntry)
            adIdQuery[adEntry["adId"]] = adEntry["query"].lower()

    with open(queryAdInputDir, "r") as queryCampAds:
        queryCampAd = json.load(queryCampAds)
        print(queryCampAd)

    with open(campWeightDir, "r") as campWeights:
        campWeight = json.load(campWeights)
        print(campWeight)

    with open(adWeightDir, "r") as adWeights:
        adWeight = json.load(adWeights)
        print(adWeight)

    with open(campCategoryDir, "r") as campCategorys:
        campCategory = json.load(campCategorys)
        print(campCategory)

    with open(campIdAdIdDir, "r") as campIdAdIds:
        campIdAdId = json.load(campIdAdIds)
        print(campIdAdId)

    #split user to 4 level
    #level 0: 5% click for each query
    #level 1: 25% 1st 2 device id click for each query, rest 3 device_id click on 70% of query group, rest of 30% query  group no click
    #level 2: 30%  random  select 1 device_id click for 50% of query group
    #level 3: 40% never click



