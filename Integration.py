# this is the final version of integration
import os
import csv

# Set the directory where the CSV files are stored
directory = "/Users/berwyn/Documents/XJTLU/Semester_2/CAN404 Social Network Analysis/Final Project/My Project/players"

# Create a list to store the rows of the integrated CSV file
integrated_rows = []

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        team_name = filename[:-4]  # Get the team name from the filename
        with open(os.path.join(directory, filename), "r") as f:
            reader = csv.reader(f)
            for player_name in reader:
                integrated_rows.append([team_name, player_name[0]])

# Write the integrated CSV file
with open("integrated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Team", "Players"])  # Write the header row
    for row in integrated_rows:
        writer.writerow(row)
