import json

# data = open("original/ads.txt", "r")
# for line in data:
#     print(line)
with open("original/ads.txt") as jsonFile:
    data = json.load(jsonFile)
    # print(data["campaignId"])


