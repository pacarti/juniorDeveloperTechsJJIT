# juniorDeveloperTechsJJIT.py - takes the junior job offers count for the following technologies: AI, Python, Ruby, Java, JS, PHP and DevOps and makes a bar chart from them

# Step1: Return the proper value of the offers for each technology

import requests, bs4

# Python
addressPy = 'https://justjoin.it/all-locations/python/experience-level_junior'
# Java
# addressJava = 'https://justjoin.it/all-locations/java/experience-level_junior'


try:
    resPy = requests.get(addressPy)
except ConnectionError:
    print('Connection error!')
    exit()

pythonSoup = bs4.BeautifulSoup(resPy.text, 'html.parser')

numOfJuniorJobsElem = pythonSoup.select('h1.MuiTypography-root')[0]

# this doesn't exist in HTML thus is not saved into the list - it is dynamically generated:
# numOfJuniorJobs = pythonSoup.select('.MuiTab-iconWrapper.css-1604j7q')

# print(numOfJuniorJobs)

textNumOfJuniorJobs = numOfJuniorJobsElem.getText()

print("Job offers count:")

print(textNumOfJuniorJobs.strip('Job offers: '))