from collections import deque

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited_states = set()
        self.all_solutions = []

    def solve(self):
        initial_state = (0, 0)
        self.bfs(initial_state)
        if self.all_solutions:
            return self.all_solutions
        else:
            return "No solution found."

    def bfs(self, initial_state):
        queue = deque([(initial_state, [])])
        while queue:
            state, path = queue.popleft()
            print("Exploring state:", state)
            print("Current path:", path)
            if state[0] == self.target or state[1] == self.target:
                self.all_solutions.append(path + [state])
                print("Found a solution!")
                print("Current solutions:", self.all_solutions)
            self.visited_states.add(state)

            next_states = self.generate_next_states(state)
            print("Next possible states:", next_states)
            for next_state in next_states:
                if next_state not in self.visited_states:
                    queue.append((next_state, path + [state]))

    def generate_next_states(self, state):
        next_states = []

        # Empty Jug 1
        next_states.append((0, state[1]))

        # Empty Jug 2
        next_states.append((state[0], 0))

        # Fill Jug 1
        next_states.append((self.jug1_capacity, state[1]))

        # Fill Jug 2
        next_states.append((state[0], self.jug2_capacity))

        # Pour from Jug 1 to Jug 2
        if state[0] > 0 and state[1] < self.jug2_capacity:
            amount_to_pour = min(state[0], self.jug2_capacity - state[1])
            next_states.append((state[0] - amount_to_pour, state[1] + amount_to_pour))

        # Pour from Jug 2 to Jug 1
        if state[1] > 0 and state[0] < self.jug1_capacity:
            amount_to_pour = min(state[1], self.jug1_capacity - state[0])
            next_states.append((state[0] + amount_to_pour, state[1] - amount_to_pour))

        return next_states

    def display_jugs(self, state):
        jug1 = state[0]
        jug2 = state[1]
        print("Jug 1:", "| " + "O" * jug1 + " " * (self.jug1_capacity - jug1) + "|")
        print("Jug 2:", "| " + "O" * jug2 + " " * (self.jug2_capacity - jug2) + "|")
        print("   ", " " * self.jug1_capacity + " ", " " * self.jug2_capacity)

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

problem = WaterJugProblem(jug1_capacity, jug2_capacity, target)
solutions = problem.solve()
if solutions != "No solution found.":
    print("Alternate solution paths:")
    for solution in solutions:
        for state in solution:
            problem.display_jugs(state)
            print()
        print("---------------")
else:
    print("No solution found.")
