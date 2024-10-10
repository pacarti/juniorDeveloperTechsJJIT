# juniorDeveloperTechsJJIT.py - takes the junior job offers count for the following technologies: AI, Python, Ruby, Java, JS, PHP and DevOps and makes a bar chart from them

# Step1: Return the proper value of the offers for each technology - print the text of that
# Step2: Save the result in a dictionary, with a format: {Technology: number of jobs}

import requests, bs4, re

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

print("Job offers count:")

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
    print(techTextAndNum)

    mo = techAndNumRegex.search(techTextAndNum)

    techDict.setdefault(mo.group(1), mo.group(2))

print(techDict)