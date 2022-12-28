# ------------------------------------------------------------------------------------------------------------------
# NOTE: This only works under the assumption that the accessed web page does not change its layout and class naming
# ------------------------------------------------------------------------------------------------------------------


# Need to be installed with pip
from bs4 import BeautifulSoup
import requests
from progress.bar import IncrementalBar
import time
import json
import sys

# ------------------------------------------------------------------------------------------------------------------

# Go to Billboard top 100 page
url = "https://www.billboard.com/charts/hot-100"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


# ===========================================================
# look fot only the 'li' tags with the class of 'chart-list__element'
tags = soup.findAll("li", class_="chart-list__element")

bar = IncrementalBar('Collecting...', max = len(tags))


outList = []


# package up needed the needed data in each lst item into a dictionary
def extract(li):
    return {
        "rank": int(li.find_all('span', class_="chart-element__rank__number")[0].text),
        "title": li.find_all('span', class_="chart-element__information__song")[0].text,
        "artist": li.find_all('span', class_="chart-element__information__artist")[0].text
    }


# loop through the li tags to get a list of a tags and get the text within them
for i in tags:

    # Add each dictionary to a list
    outList.append(extract(i))

    # Increment the bar and pause a little
    bar.next()
    time.sleep(0.01)

bar.finish()


# write the outList to a .json file
with open("Billboard-Hot-100.json", 'w') as fileObject:
    json.dump(outList, fileObject)


sys.stdout.write("Output to Billboard-Hot-100.json")