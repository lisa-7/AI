import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))

    def a_star_search(self, start):
        # Initialize f' value for each vertex
        f_values = [float('inf')] * self.vertices
        f_values[start] = 0

        # Initialize heap for open list
        open_list = [(0, start)]

        # Iterate until open list is empty
        while open_list:
            # Pop node with minimum f' value
            f_prime, current = heapq.heappop(open_list)

            # Mark node as SOLVED if f' value is 0
            if f_prime == 0:
                print(f"Node {current} is SOLVED.")
                continue

            # Explore each neighbor of current node
            for neighbor, edge_weight in self.adj_list[current]:
                # Calculate f' value for the neighbor
                f_prime_neighbor = max(f_values[current], edge_weight)

                # Update f' value if it's improved
                if f_prime_neighbor < f_values[neighbor]:
                    f_values[neighbor] = f_prime_neighbor
                    heapq.heappush(open_list, (f_prime_neighbor, neighbor))

        print("Algorithm execution complete.")

    def draw_graph(self):
        # Code to visualize the graph
        pass

def main():
    # Example usage
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 4, 4)
    graph.a_star_search(0)

if __name__ == "__main__":
    main()
