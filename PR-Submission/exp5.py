import numpy as np
import matplotlib.pyplot as plt
import heapq

class State:
    def __init__(self, tiles, blank_position, parent=None, g=0, h=0):
        self.tiles = tiles
        self.blank_position = blank_position
        self.parent = parent
        self.g = g  # cost from start to current state
        self.h = h  # heuristic cost from current state to goal state

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def is_goal(self, goal_state):
        return np.array_equal(self.tiles, goal_state.tiles)

    def get_neighbors(self):
        neighbors = []
        i, j = self.blank_position
        m, n = self.tiles.shape
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                neighbor = np.copy(self.tiles)
                neighbor[i, j], neighbor[ni, nj] = neighbor[ni, nj], neighbor[i, j]
                neighbors.append(State(neighbor, (ni, nj), self, self.g + 1, 0))  # Assuming uniform cost
        return neighbors

def manhattan_distance(state, goal_state):
    return np.sum(np.abs(state.tiles - goal_state.tiles))

def a_star_search(initial_state, goal_test):
    frontier = []
    heapq.heappush(frontier, initial_state)
    explored = set()

    while frontier:
        current_state = heapq.heappop(frontier)
        if goal_test(current_state):
            return current_state
        explored.add(tuple(map(tuple, current_state.tiles)))
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.tiles)) not in explored:
                heapq.heappush(frontier, neighbor)
                explored.add(tuple(map(tuple, neighbor.tiles)))
    return None

def plot_state(state):
    plt.imshow(state.tiles, cmap='viridis', origin='upper')
    plt.colorbar()
    plt.title('8 Puzzle State')
    plt.show()

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    path.reverse()
    for state in path:
        plot_state(state)

def main():
    initial_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    initial_blank_position = np.where(initial_state == 0)
    initial_blank_position = (initial_blank_position[0][0], initial_blank_position[1][0])
    initial_state = State(initial_state, initial_blank_position)

    goal_blank_position = np.where(goal_state == 0)
    goal_blank_position = (goal_blank_position[0][0], goal_blank_position[1][0])
    goal_state = State(goal_state, goal_blank_position)

    solution = a_star_search(initial_state, lambda state: state.is_goal(goal_state))

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()
