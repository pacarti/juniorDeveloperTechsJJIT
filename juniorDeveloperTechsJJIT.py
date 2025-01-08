# juniorDeveloperTechsJJIT.py - takes the junior job offers count for the following technologies: AI, Python, Ruby, Java, JS, PHP and DevOps and makes a bar chart from them

def fetchJobData(address):
    try:
        res = requests.get(address)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        numOfJuniorJobsElem = soup.select('h1.MuiTypography-root')[0]

        return numOfJuniorJobsElem

    except IndexError:
        return None

import requests, bs4, re, time, datetime
import matplotlib.pyplot as plt

addresses = []

techAndNumRegex = re.compile(r'^(\w+\W?\w+)  - (\d{1,3})? offers$')

techDict = {}

# Python
addressPy = 'https://justjoin.it/job-offers/all-locations/python?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressPy)
# Java
addressJava = 'https://justjoin.it/job-offers/all-locations/java?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressJava)
# PHP
addressPHP = 'https://justjoin.it/job-offers/all-locations/php?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressPHP)
# JS
addressJS = 'https://justjoin.it/job-offers/all-locations/javascript?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressJS)
# Ruby
addressRuby = 'https://justjoin.it/job-offers/all-locations/ruby?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressRuby)
# AI/ML
addressAI = 'https://justjoin.it/job-offers/all-locations/ai?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressAI)
# DevOps
addressDevOps = 'https://justjoin.it/job-offers/all-locations/devops?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressDevOps)
# Testing
addressTesting = 'https://justjoin.it/job-offers/all-locations/testing?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressTesting)
# Mobile
addressTesting = 'https://justjoin.it/job-offers/all-locations/mobile?experience-level=junior&orderBy=DESC&sortBy=published'
addresses.append(addressTesting)


for address in addresses:
    # while True:
        

    # this doesn't exist in HTML thus is not saved into the list - it is dynamically generated:
    # numOfJuniorJobs = pythonSoup.select('.MuiTab-iconWrapper.css-1604j7q')


    numOfJuniorJobsElem = fetchJobData(address)

    # Since the h1 element containing the job offers count is not always loaded, then numOfJuniorJobsElem will be None. Then loop the function until it will be loaded properly:
    while numOfJuniorJobsElem == None:
        numOfJuniorJobsElem = fetchJobData(address)


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

for k, v in techDictSorted.items():
    print(k + ':  ' + str(v))

plt.bar(range(len(techDictSorted)), list(techDictSorted.values()), width = 0.7, color = colors)

plt.xticks(range(len(techDictSorted)), list(techDictSorted.keys()))

dt = datetime.datetime.now()

plt.title('justjoin.it - offers for Junior Developer - ' + dt.strftime('%d/%m/%Y'))

plt.xlabel('Technology')

plt.ylabel('Offers count')

plt.show()
