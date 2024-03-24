class BlockWorld:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def evaluate_state(self, state):
        score = 0
        for block, resting_place in state.items():
            if block == resting_place:
                score += 1
            else:
                score -= 1
        return score

    def generate_next_states(self, current_state):
        next_states = []
        for block, resting_place in current_state.items():
            if resting_place != "table":
                # Move block to the table
                next_state = current_state.copy()
                next_state[block] = "table"
                next_states.append(next_state)
            for other_block in current_state.keys():
                if other_block != block:
                    # Move block on top of other_block
                    next_state = current_state.copy()
                    next_state[block] = other_block
                    next_states.append(next_state)
        return next_states

    def hill_climbing(self):
        current_state = self.initial_state
        current_score = self.evaluate_state(current_state)

        while True:
            print("Current state:", current_state)
            print("Current score:", current_score)

            if current_state == self.goal_state:
                print("Goal state reached!")
                break

            next_states = self.generate_next_states(current_state)
            best_next_state = None
            best_next_score = current_score

            for next_state in next_states:
                next_score = self.evaluate_state(next_state)
                if next_score > best_next_score:
                    best_next_state = next_state
                    best_next_score = next_score

            if best_next_state is None or best_next_score <= current_score:
                print("Local maximum reached. Stopping.")
                break

            current_state = best_next_state
            current_score = best_next_score

        print("Final state:", current_state)
        print("Final score:", current_score)


def main():
    initial_state = {'A': 'table', 'B': 'table', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H'}
    goal_state = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H'}
    block_world = BlockWorld(initial_state, goal_state)
    block_world.hill_climbing()


if __name__ == "__main__":
    main()
