import json
import re
from ast import literal_eval

data = open("original/ads.txt", "r")
i = 0
for line in data:
    # print(line)
    jsondata = json.loads(line)
    print(jsondata)
    newAdId = jsondata["adId"] + 2000 + i
    print(newAdId)
    newTitle = jsondata["title"].replace(",", "")
    newTitle = newTitle.replace("-", "")
    newTitle = newTitle.replace(".", "")
    newTitle = re.sub("\s+", " ", newTitle)
    print(newTitle)

    i = i + 1
    break;


