# web-scraper-exercise/scraper.py

import requests
from bs4 import BeautifulSoup
import csv

print("-----------------------")
print("WEB SCRAPER EXERCISE...")
print("-----------------------")

request_url = "https://www.gutenberg.org/ebooks/author/65"
print("REQUEST URL:", request_url)

# issue an HTTP "GET" request to the specified URL:
response = requests.get(request_url)
print("RESPONSE:", response)
#print(response.status_code)
#print(response.text) # the page contents!

print("-----------------------")
print("PARSING THE RESPONSE:")
print("-----------------------")

# initialize a new BeautifulSoup() object to parse the specified page contents
# see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup
soup = BeautifulSoup(response.text, features="html.parser")
#print(soup.prettify())

# use the .find_all() method to find all elements with a specific class
# see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
elements = soup.find_all("span", "title")

with open("books.csv", "w") as csv_file:
    # see: https://docs.python.org/3/library/csv.html#csv.DictWriter
    writer = csv.DictWriter(csv_file, fieldnames=["author", "title"])
    # writes header row with fieldnames set above:
    writer.writeheader()

    for element in elements:
        print(element) #> <span class="title">Macbeth</span>
        print(element.text) #> Macbeth
        print("---")
        # write each book title to its own row:
        writer.writerow({"author": "Shakespeare", "title": element.text})
