import time
import os
from collections import deque

def move(state, action):
    # Unpack the current state
    left_bank_missionaries, left_bank_cannibals, boat_position = state
    
    # Apply the action based on the boat position
    if boat_position == 'left':
        left_bank_missionaries -= action[0]
        left_bank_cannibals -= action[1]
        boat_position = 'right'
    else:
        left_bank_missionaries += action[0]
        left_bank_cannibals += action[1]
        boat_position = 'left'
    
    return (left_bank_missionaries, left_bank_cannibals, boat_position)

def is_valid(state):
    left_bank_missionaries, left_bank_cannibals, boat_position = state
    right_bank_missionaries = 3 - left_bank_missionaries
    right_bank_cannibals = 3 - left_bank_cannibals
    
    # Check constraints
    if left_bank_missionaries < 0 or left_bank_cannibals < 0 or \
        right_bank_missionaries < 0 or right_bank_cannibals < 0:
        return False
    if left_bank_missionaries > 0 and left_bank_missionaries < left_bank_cannibals:
        return False
    if right_bank_missionaries > 0 and right_bank_missionaries < right_bank_cannibals:
        return False
    return True

def print_state(state):
    os.system('cls' if os.name == 'nt' else 'clear')
    left_bank_missionaries, left_bank_cannibals, boat_position = state
    right_bank_missionaries = 3 - left_bank_missionaries
    right_bank_cannibals = 3 - left_bank_cannibals
    
    boat_side = 'Left' if boat_position == 'left' else 'Right'
    print('Missionaries and Cannibals Problem')
    print(f'Boat Position: {boat_side} Bank\n')

    print('Bank:          Left           |           Right')
    print('               M  C           |            M  C')
    print(f'Missionaries:   {left_bank_missionaries}  {left_bank_cannibals}           |            {right_bank_missionaries}  {right_bank_cannibals}')
    print('\n\n')

def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited_states = set()

    while queue:
        state, path = queue.popleft()
        visited_states.add(state)

        if state == (0, 0, 'right'):
            return path + [state]

        for action in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]:
            new_state = move(state, action)
            if is_valid(new_state) and new_state not in visited_states:
                new_path = path + [state]
                queue.append((new_state, new_path))
                visited_states.add(new_state)

def solve_missionaries_cannibals():
    initial_state = (3, 3, 'left')
    solution_path = bfs(initial_state)
    return [initial_state] + solution_path if solution_path else None

def main():
    solution_path = solve_missionaries_cannibals()
    if solution_path:
        print("Solution found!")
        for i, state in enumerate(solution_path):
            print(f'Step {i + 1}:')
            print_state(state)
            time.sleep(1)  # Add a delay between steps
        print("No more steps")
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()
