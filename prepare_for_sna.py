import csv
import networkx as nx


# Read the modified CSV file
with open('pre_sna.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # Get the header row
    data = list(reader)  # Get the data rows

# Create a directed graph
graph = nx.DiGraph()

# Iterate through the data and add edges to the graph
for row in data:
    teams = row[0]
    club1 = row[1]
    club2 = row[2]

    # Add edges between player and clubs
    graph.add_edge(teams, club1)
    graph.add_edge(teams, club2)

# Perform analysis on the graph using networkx
# Example: Calculate degree centrality
degree_centrality = nx.degree_centrality(graph)
print(degree_centrality)
