import matplotlib.pyplot as plt
import networkx as nx

# Define a set of input reads
reads = [
    "ATGGCATGTGTAGTCA",
    "AGTCATGTCAGTGCCAT",
    "AGTGCCATTATATTAGTCTT",
    "TTAGTCTTAGCTAGCTTACTGAT",
    "CTGATCTTCTTCTAGAGGATC",
    "TCTTCTAGAGGATCTGATCTT",
    "GATCTTAGCTATATATT",
    "TATATATTCGATCTC",
    "ATCTCTATCCCGATCGATTAGCTTCTCAAACGGGGCCC"
]

# Define a function to find the longest common substring (LCS) between two reads
def find_lcs(read1, read2):
    lcs = ""
    for i in range(len(read1)):
        for j in range(len(read2)):
            k = 0
            while i + k < len(read1) and j + k < len(read2) and read1[i + k] == read2[j + k]:
                k += 1
            if k > len(lcs):
                lcs = read1[i:i + k]
    return lcs

# Construct an overlap graph by finding the LCS between all pairs of reads
overlap_graph = nx.DiGraph()
for i in range(len(reads)):
    for j in range(len(reads)):
        if i != j:
            lcs = find_lcs(reads[i], reads[j])
            if len(lcs) > 0:
                overlap_graph.add_edge(i, j, label=lcs)

# Plot the overlap graph
pos = nx.circular_layout(overlap_graph)
labels = nx.get_edge_attributes(overlap_graph, 'label')
nx.draw(overlap_graph, pos, with_labels=True)
nx.draw_networkx_edge_labels(overlap_graph, pos, edge_labels=labels)
plt.title("Overlap Graph")
plt.show()

# Define a function to find the read with the highest degree (i.e., the most overlaps)
def find_max_degree_node(graph, visited):
    max_degree = -1
    max_node = -1
    for node in graph:
        if node not in visited:
            degree = len(graph[node])
            if degree > max_degree:
                max_degree = degree
                max_node = node
    return max_node

# Find a Hamiltonian path through the overlap graph using a Greedy Algorithm
path = [find_max_degree_node(overlap_graph, set())]
while len(path) < len(reads):
    last_node = path[-1]
    next_node = find_max_degree_node(overlap_graph, set(path))
    path.append(next_node)

# Plot the Hamiltonian path
path_edges = [(path[i-1], path[i]) for i in range(1, len(path))]
path_graph = nx.DiGraph()
path_graph.add_edges_from(path_edges)
pos = nx.circular_layout(path_graph)
nx.draw(path_graph, pos, with_labels=True)
plt.title("Hamiltonian Path")
plt.show()

# Assemble the genome sequence from the Hamiltonian path
genome = reads[path[0]]
for i in range(1, len(path)):
    lcs = find_lcs(reads[path[i - 1]], reads[path[i]])
    genome += reads[path[i]][len(lcs):]

# Assemble the genome sequence from the Hamiltonian path
genome = reads[path[0]]
for i in range(1, len(path)):
    lcs = find_lcs(reads[path[i - 1]], reads[path[i]])
    genome += reads[path[i]][len(lcs):]

# Print the final assembled genome sequence
print("Assembled Genome Sequence:")
print()
print(">genome")
print(genome)
