import csv
import networkx as nx
import matplotlib.pyplot as plt


def visualize_network(graph):
    # Set node colors and sizes
    node_colors = {
        'top16': 'red',
        'others': 'blue'
    }
    node_sizes = [500 if data['type'] == 'top16' else 200 for _, data in graph.nodes(data=True)]

    # Draw the graph
    pos = nx.spring_layout(graph, seed=42)
    nx.draw_networkx(graph, pos, node_color=[node_colors[data['type']] for _, data in graph.nodes(data=True)],
                     node_size=node_sizes, alpha=0.7, with_labels=True, font_size=8, font_color='white',
                     edge_color='gray', width=0.2)

    # Add a legend for node types
    legend_handles = []
    for node_type in node_colors:
        legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=node_colors[node_type], markersize=8))
    plt.legend(legend_handles, node_colors.keys(), loc='upper right')

    # Set plot title and show the graph
    plt.title('Relationship between Top 16 Clubs in UEFA Champions League')
    plt.axis('off')
    plt.show()


def main():
    # Read the data from the CSV file
    data = []
    with open('formatted_dataset_new.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    # Create a directed graph
    graph = nx.DiGraph()

    # Add top 16 clubs as nodes to the graph
    top16_clubs = set()
    for row in data:
        old_club = row['Old_Club']
        new_club = row['New_Club']

        top16_clubs.add(old_club)
        top16_clubs.add(new_club)

    for club in top16_clubs:
        graph.add_node(club, type='top16')

    # Add 'Others' as a single node to represent non-top 16 clubs
    graph.add_node('Others', type='others')

    # Connect players to their old and new clubs
    for row in data:
        player = row['Player']
        old_club = row['Old_Club']
        new_club = row['New_Club']

        if old_club in top16_clubs and new_club in top16_clubs:
            graph.add_edge(old_club, new_club)

    # Visualize the graph
    visualize_network(graph)


if __name__ == '__main__':
    main()
