def input_graph():
    n = int(input("Enter number of nodes: "))
    print("Enter the adjacency matrix row by row:")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph
def display_graph(graph):
    print("Graph (Adjacency Matrix):")
    for row in graph:
        print(" ".join(map(str, row)))
    print()
def delete_node(graph, node_index):
    graph.pop(node_index)
    for row in graph:
        row.pop(node_index)
    return graph
graph = input_graph()
print("\nBefore deletion:")
display_graph(graph)
graph = delete_node(graph, 1)
print("After deleting node 2:")
display_graph(graph)