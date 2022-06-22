from datetime import time

import bs4
import html5lib as html5lib
from bs4 import BeautifulSoup
import requests
import pprint

# url from networks in web inspector
url = 'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&pageNo=1&experience=0&k=python&l=bangalore&experience=0&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong='
# url='https://www.naukri.com/python-jobs-in-bangalore?k=python&l=bangalore&experience=0'
headers = {"appid": "109", "systemid": "109"}
html_code = requests.get(url, headers=headers)
# This website doesn't want us to scrape this
data = html_code.json()

# print(data['jobDetails'])

# for i in data['jobDetails']:
#    print(i['title'], i['companyName'])
#    print(i['tagsAndSkills'])
#    print(i['jobDescription'])
#    print('\n')
# line 17 to 21 is fine but job desc as html in it. we can clean that using beautiful soup
jobid = 1
for i in data['jobDetails']:
    print(i['title'], i['companyName'])
    print(i['tagsAndSkills'])
    soup = bs4.BeautifulSoup(i['jobDescription'])
    print(soup.text)
    # apart for printing we can store this in file as well
    f = open(str(jobid) + ".txt", "w")
    f.write(i['title'])
    f.write(i['companyName'])
    f.write(i['tagsAndSkills'])
    f.write(soup.text)
    f.close()
    jobid += 1
    print('\n')

# JSON stands for JavaScript Object Notation

# JSON is a lightweight format for storing and transporting data

# JSON is often used when data is sent from a server to a web page

# JSON is "self-describing" and easy to understand
# pprint.pprint(data)
# The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be
# used as input to the interpreter
#
# print(html_code.content) what is xhr? there are the javascript running on the modern website requesting it to
# refresh the specific parts what is json? Now suppose you have a dictionary and want to write it into a file. You
# can't write dictionary directly into a file. so u can convert it into string format using json.dumps() and write
# into the file. now while reading that object, u can use json.load(file name) and get the string in dictionary
# format. json calls with serialization (python objects to string) and deserialization (strings to python objects)
# json stands from javascript object notation
