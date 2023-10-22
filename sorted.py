# this is for cleaning the transferred clubs
import csv


input_file = 'dataset.csv'
output_file = 'formatted_dataset_new.csv'

# Read the input CSV file
with open(input_file, 'r', encoding='utf-8') as csv_file_1:
    reader = csv.reader(csv_file_1)
    header = next(reader)  # Get the header row
    data = list(reader)  # Get the data rows


# Get all values from the first column
first_column_values = [row[0] for row in data]


def clean_team_name(team, first_column_values):
    if "liverpool" in team:
        return "Liverpool"
    elif "chelsea" in team:
        return "Chelsea"
    elif "frankfurt" in team:
        return "E. Frankfurt"
    elif "benfica" in team:
        return "Benfica"
    elif "tottenham" in team:
        return "Tottenham"
    elif "rb leipzig" in team:
        return "RB Leipzig"
    elif "milan" in team:
        return "AC Milan"
    elif "inter" in team:
        return "Inter"
    elif "bruges" in team or "brügge" in team:
        return "Club Brugge"
    elif "porto" in team:
        return "FC Porto"
    elif "dortmund" in team:
        return "Bor. Dortmund"
    elif "bayern" in team:
        return "Bayern Munich"
    elif "napoli" in team:
        return "SSC Napoli"
    elif "paris" in team:
        return "Paris SG"
    elif "real madrid" in team:
        return "Real Madrid"
    elif "man city" in team:
        return "Man City"
    elif team not in first_column_values:
        return "Others"
    else:
        return team


# Clean team names in the third and fourth columns
for row in data:
    row[2] = clean_team_name(row[2], first_column_values)
    row[3] = clean_team_name(row[3], first_column_values)

# Remove rows with the same value in the third and fourth columns
cleaned_data = []
for row in data:
    if row[2] == row[3]:
        print("skip")
    else:
        cleaned_data.append(row)

# Write the modified data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(cleaned_data)

print("Player names formatted, invalid season rows removed, team names cleaned, and rows with the same value in the third and fourth columns deleted.")
print("Formatted data saved to 'formatted_transfer_history.csv'.")
