import requests
import re
from bs4 import BeautifulSoup
import csv
import pandas as pd

# List of player URLs
player_urls = [
    'https://www.transfermarkt.com/erling-haaland/profil/spieler/418560',
    'https://www.transfermarkt.com/manuel-akanji/profil/spieler/284730',
    # Add more player URLs here...
]

# Open a CSV file to write the data
with open('transfer_history.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Player', 'Season', 'Date', 'Old_Club', 'New_Club', 'Market_Value', 'Fee'])  # Write the header row

    # Iterate over each player URL
    for url in player_urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        player_name = re.search(r'/([^/]+)/profil', url).group(1)

        # Find all the transfer history grids
        transfer_history_grids = soup.find_all('div', {'class': 'box', 'data-viewport': 'Transferhistorie'})

        transfer_history = []

        # Find all the transfer history entries
        transfer_entries = soup.find_all("div", class_="grid tm-player-transfer-history-grid")
        # Iterate over each transfer entry
        for entry in transfer_entries:
            season = entry.find(class_="tm-player-transfer-history-grid__season").text.strip()
            date = entry.find(class_="tm-player-transfer-history-grid__date").text.strip()
            old_club = entry.find(class_="tm-player-transfer-history-grid__old-club").text.strip()
            new_club = entry.find(class_="tm-player-transfer-history-grid__new-club").text.strip()
            market_value = entry.find(class_="tm-player-transfer-history-grid__market-value").text.strip()
            fee = entry.find(class_="tm-player-transfer-history-grid__fee").text.strip()

            # Append the transfer details to the transfer history list
            transfer_history.append({
                "Player": player_name,
                "Season": season,
                "Date": date,
                "Old_Club": old_club,
                "New_Club": new_club,
                "Market_Value": market_value,
                "Fee": fee
            })

        # Convert the data to a DataFrame
        df = pd.DataFrame(transfer_history)

        # Export DataFrame to CSV
        df.to_csv(csv_file, index=False, header=False, mode='a')

print("Data has been scraped and saved to 'transfer_history.csv'.")
