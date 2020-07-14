"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage (http://www.nytimes.com/).
"""

from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.nytimes.com/')
soup = BeautifulSoup(page.content, 'lxml')
headlines = [x.text for x in soup.find_all('h2')]

[print(h) for h in headlines]
