import sys
import json

if __name__ == '__main__':
    #Device IP, Device id,Session id,Query,AdId,CampaignId,Ad_category_Query_category(0/1),clicked(0/1)
    #use following feature to generate click Log
    #IP, device_id, AdId,QueryCategry_AdsCategory,Query_CampaignId, Query_AdId
    adInputFileDir = sys.argv[1]

    adList = []
    adIdQuery = {}
    with open(adInputFileDir, "r") as ads:
        for ad in ads:
            adEntry = json.loads(ad)
            adList.append(adEntry)
            adIdQuery[adEntry["adId"]] = adEntry["query"].lower()
    print(adIdQuery)

