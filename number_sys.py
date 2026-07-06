import random
import math
import heapq
from collections import defaultdict

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = {}

    def connect(self, other, weight):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Node({self.id})"


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, a, b, weight):
        self.add_node(a)
        self.add_node(b)

        self.nodes[a].connect(self.nodes[b], weight)
        self.nodes[b].connect(self.nodes[a], weight)

    def generate_random(self, size=100):
        for i in range(size):
            self.add_node(i)

        for _ in range(size * 6):
            a = random.randint(0, size - 1)
            b = random.randint(0, size - 1)

            if a != b:
                self.add_edge(a, b, random.randint(1, 30))

    def dijkstra(self, start):
        distances = {node: math.inf for node in self.nodes}
        previous = {node: None for node in self.nodes}

        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current = heapq.heappop(pq)

            if current_distance > distances[current]:
                continue

            for neighbor, weight in self.nodes[current].neighbors.items():
                distance = current_distance + weight

                if distance < distances[neighbor.id]:
                    distances[neighbor.id] = distance
                    previous[neighbor.id] = current
                    heapq.heappush(pq, (distance, neighbor.id))

        return distances, previous

    def shortest_path(self, start, end):
        distances, previous = self.dijkstra(start)

        path = []

        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, distances[end]


class NetworkAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def degree_distribution(self):
        distribution = defaultdict(int)

        for node in self.graph.nodes.values():
            distribution[len(node.neighbors)] += 1

        return dict(sorted(distribution.items()))

    def average_degree(self):
        total = 0

        for node in self.graph.nodes.values():
            total += len(node.neighbors)

        return total / len(self.graph.nodes)

    def density(self):
        n = len(self.graph.nodes)

        edges = sum(len(node.neighbors) for node in self.graph.nodes.values()) / 2

        return (2 * edges) / (n * (n - 1))

    def report(self):
        print("=" * 70)
        print("NETWORK ANALYSIS REPORT")
        print("=" * 70)

        print(f"Nodes             : {len(self.graph.nodes)}")
        print(f"Average Degree    : {self.average_degree():.2f}")
        print(f"Density           : {self.density():.4f}")

        print("\nDegree Distribution")
        print("-" * 70)

        for degree, count in self.degree_distribution().items():
            print(f"{degree:3d} -> {count:4d}")

        print("=" * 70)


class Simulation:

    def __init__(self):
        self.graph = Graph()

    def run(self):

        print("Generating network...")
        self.graph.generate_random(150)

        analyzer = NetworkAnalyzer(self.graph)
        analyzer.report()

        start = random.randint(0, 149)
        end = random.randint(0, 149)

        print("\nRunning shortest path search...")
        print(f"Source      : {start}")
        print(f"Destination : {end}")

        path, cost = self.graph.shortest_path(start, end)

        print("\nShortest Path")
        print(path)

        print(f"\nTotal Cost : {cost}")

        print("\nTop Connectivity Ranking")

        ranking = sorted(
            self.graph.nodes.values(),
            key=lambda n: len(n.neighbors),
            reverse=True
        )

        for node in ranking[:20]:
            print(
                f"Node {node.id:3d} | "
                f"Connections: {len(node.neighbors):3d}"
            )

        print("\nSimulation Complete.")


def benchmark():

    sim = Simulation()

    for run in range(3):
        print("\n")
        print("#" * 70)
        print(f"RUN {run + 1}")
        print("#" * 70)

        sim.run()


if __name__ == "__main__":
    random.seed(42)
    benchmark()