# this is the final version of extracting the players name
import re
import csv

# Open the input CSV file
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    names = [row[1] for row in reader]  # Get the names from the first column

# Modify the names with regular expressions
modified_names = []
for name in names:
    modified_name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name)
    modified_names.append(modified_name)

# Open the output CSV file for writing
with open('output.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Name'])  # Write the header row

    # Write the modified names to the output CSV file
    for name in modified_names:
        writer.writerow([name])
