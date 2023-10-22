import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://www.uefa.com/uefachampionsleague/clubs/1652--tottenham//squad/'

# Make a GET request to the URL
response = requests.get(url)
print(response)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <span> tags with 'slot="primary"' and 'itemprop="name"' attributes
names = soup.find_all('span', {'slot': 'primary', 'itemprop': 'name'})

# Extract the text of each <span> tag and store it in a list
name_list = [name.get_text() for name in names]

# Write the list of names to a CSV file
with open('tottenham.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name'])
    for name in name_list:
        writer.writerow([name])
