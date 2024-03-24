import random
import math

class TravellingSalesman:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)

    def distance(self, city1, city2):
        # Assuming cities are represented as tuples (x, y) coordinates
        x1, y1 = city1
        x2, y2 = city2
        # Calculate Euclidean distance
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distance

    def calculate_fitness(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            from_city = self.cities[route[i]]
            to_city = self.cities[route[i + 1]]
            total_distance += self.distance(from_city, to_city)
        return total_distance

    def generate_random_route(self):
        route = list(range(self.num_cities))
        random.shuffle(route)
        return route

    def crossover(self, parent1, parent2):
        # Ordered crossover
        start = random.randint(0, self.num_cities - 2)
        end = random.randint(start + 1, self.num_cities - 1)
        subset = parent1[start:end]
        offspring = [city for city in parent2 if city not in subset]
        return offspring[:start] + subset + offspring[start:]

    def mutate(self, route, mutation_rate):
        for i in range(self.num_cities):
            if random.random() < mutation_rate:
                j = random.randint(0, self.num_cities - 1)
                route[i], route[j] = route[j], route[i]
        return route

    def solve(self, population_size=100, num_iterations=1000, mutation_rate=0.01):
        population = [self.generate_random_route() for _ in range(population_size)]
        for _ in range(num_iterations):
            new_population = []
            for _ in range(population_size // 2):
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                offspring = self.crossover(parent1, parent2)
                offspring = self.mutate(offspring, mutation_rate)
                new_population.append(offspring)
            population.extend(new_population)
            population = sorted(population, key=self.calculate_fitness)[:population_size]
        best_route = min(population, key=self.calculate_fitness)
        return best_route

# Example usage
cities = [(0, 0), (1, 2), (3, 1), (2, 3), (4, 0)]
tsp = TravellingSalesman(cities)
best_route = tsp.solve()
print("Best route:", best_route)
