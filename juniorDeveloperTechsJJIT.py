# juniorDeveloperTechsJJIT.py - takes the junior job offers count for the following technologies: AI, Python, Ruby, Java, JS, PHP and DevOps and makes a bar chart from them

import requests, bs4, re
import matplotlib.pyplot as plt

addresses = []

techAndNumRegex = re.compile(r'^(\w+\W?\w+)  - (\d{1,3})? offers$')

techDict = {}

# Python
addressPy = 'https://justjoin.it/all-locations/python/experience-level_junior'
addresses.append(addressPy)
# Java
addressJava = 'https://justjoin.it/all-locations/java/experience-level_junior'
addresses.append(addressJava)
# PHP
addressPHP = 'https://justjoin.it/all-locations/php/experience-level_junior'
addresses.append(addressPHP)
# JS
addressJS = 'https://justjoin.it/all-locations/javascript/experience-level_junior'
addresses.append(addressJS)
# Ruby
addressRuby = 'https://justjoin.it/all-locations/ruby/experience-level_junior'
addresses.append(addressRuby)
# AI/ML
addressAI = 'https://justjoin.it/all-locations/ai/experience-level_junior'
addresses.append(addressAI)
# DevOps
addressDevOps = 'https://justjoin.it/all-locations/devops/experience-level_junior'
addresses.append(addressDevOps)
# Testing
addressTesting = 'https://justjoin.it/all-locations/testing/experience-level_junior'
addresses.append(addressTesting)
# Mobile
addressTesting = 'https://justjoin.it/all-locations/mobile/experience-level_junior'
addresses.append(addressTesting)


for address in addresses:
    try:
        res = requests.get(address)
    except ConnectionError:
        print('Connection error!')
        exit()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    numOfJuniorJobsElem = soup.select('h1.MuiTypography-root')[0]

    # this doesn't exist in HTML thus is not saved into the list - it is dynamically generated:
    # numOfJuniorJobs = pythonSoup.select('.MuiTab-iconWrapper.css-1604j7q')


    textNumOfJuniorJobs = numOfJuniorJobsElem.getText()


    # '[12:]' trims the 'Job offers: ' with trimming the first 12 characters
    techTextAndNum = textNumOfJuniorJobs[12:]

    mo = techAndNumRegex.search(techTextAndNum)

    techDict.setdefault(mo.group(1), int(mo.group(2)))


colorsDict = {'Python': (0.16, 0.52, 0.8), 'Java': 'orange', 'PHP': 'purple', 'JS': (0.8, 0.67, 0), 'Ruby': 'red', 'AI/ML': 'gray', 'DevOps': 'cyan', 'Testing': (0.306, 0.561, 0.016), 'Mobile': '#2fff00'}

# Create a techs reverse-sorted dictionary so that the one with most offers count is at the top:
techDictSorted = dict(sorted(techDict.items(), key = lambda item: item[1], reverse=True))

# Create a bar colors list with the proper technology assigned to it:
colors = []

for inLabel in techDictSorted.keys():
    for techName, color in colorsDict.items():
        if inLabel == techName:
            colors.append(color)


print("Job offers count:")

for k, v in techDict.items():
    print(k + ':  ' + str(v))

plt.bar(range(len(techDictSorted)), list(techDictSorted.values()), width = 0.7, color = colors)

plt.xticks(range(len(techDictSorted)), list(techDictSorted.keys()))

plt.title('justjoin.it - offers for Junior Developer')

plt.xlabel('Technology')

plt.ylabel('Offers count')

plt.show()
