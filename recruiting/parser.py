# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup

url = "https://www.trainee.de/traineestellen/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

jobs = soup.find_all("div", {"id": "jobs"})

for job in jobs:
    print(jobs.content[0].find_all("h4", {"class": "tr-text-trans-none line-camp"})[0].text)

# for link in links:
#         print("<div href='%s'>%s</a>" % (link.get("href"), link.text))
