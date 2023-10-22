import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.transfermarkt.us/yann-sommer/profil/spieler/42205'  # Replace with the URL of the website you want to scrape
print("[ url ] is ready")

proxies = {
    "http": "http://Jeagier:bc170efe-6b83-48f1-b21c-85f139014a1c@tkus03.aakvlog.xyz:39737",
    "https": "https://Jeagier:bc170efe-6b83-48f1-b21c-85f139014a1c@tkus03.aakvlog.xyz:39737",
}
print("[ proxies ] is ready")

# make a request using the proxy
response = requests.get('https://www.transfermarkt.us/yann-sommer/profil/spieler/42205', proxies=proxies)
print(response)

# check the response
if response.status_code == 200:
    print('Success!')
else:
    print('Error:', response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
print("[ soup ] is ready")

# Find all the transfer history grids
transfer_history_grids = soup.find_all('div', {'class': 'box viewport-tracking', 'data-viewport': 'Transferhistorie'})
print(transfer_history_grids)

# Open a CSV file to write the data
with open('transfer_history.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Season', 'Left', 'Joined'])  # Write the header row

    # Loop through each transfer history grid
    for transfer_history_grid in transfer_history_grids:
        # Get the season
        season = transfer_history_grid.find('div', class_='grid__cell grid__cell--center tm-player-transfer-history-grid__season').text.strip()

        # Get the left club and joined club
        clubs = transfer_history_grid.find_all('a', class_='tm-player-transfer-history-grid__club-link')
        left = clubs[0].text.strip()
        joined = clubs[1].text.strip()

        # Write the row to the CSV file
        writer.writerow([season, left, joined])
