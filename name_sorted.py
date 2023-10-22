import csv

def format_player_name(name):
    words = name.split('-')
    capitalized_words = [word.capitalize() for word in words]
    formatted_name = ' '.join(capitalized_words)
    return formatted_name

input_file = 'transfer_history_final_1.csv'
output_file = 'formatted_transfer_history.csv'

# Read the input CSV file
with open(input_file, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # Get the header row
    data = list(reader)  # Get the data rows

# Modify the player names and filter out rows with invalid seasons
formatted_data = []
for row in data:
    player_name = row[0]
    season = row[1]

    # Format player name
    formatted_name = format_player_name(player_name)
    row[0] = formatted_name

    # Check if season matches the desired format (two digits/two digits)
    if len(season) == 5 and season[2] == '/':
        formatted_data.append(row)

# Write the modified data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(formatted_data)

print("Player names formatted and rows with invalid seasons removed. Saved to 'formatted_transfer_history.csv'.")
