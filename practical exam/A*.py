import heapq

def heuristic(state):
    left_missionaries, left_cannibals, _, _, _ = state
    return left_missionaries + left_cannibals 

def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    transitions = [
        (1, 0), 
        (2, 0), 
        (0, 1), 
        (0, 2), 
        (1, 1), 
    ]

    for transition in transitions:
        m, c = transition 
        if boat_position == 'left':
            new_left_m = left_missionaries - m
            new_left_c = left_cannibals - c
            new_right_m = right_missionaries + m
            new_right_c = right_cannibals + c
            new_boat_position = 'right'
        else:
            new_left_m = left_missionaries + m
            new_left_c = left_cannibals + c
            new_right_m = right_missionaries - m
            new_right_c = right_cannibals - c
            new_boat_position = 'left'

        if (
            new_left_m >= 0
            and new_left_c >= 0
            and new_right_m >= 0
            and new_right_c >= 0
            and (new_left_m == 0 or new_left_m >= new_left_c)
            and (new_right_m == 0 or new_right_m >= new_right_c)
        ):
            possible_moves.append(
                (
                    new_left_m,
                    new_left_c,
                    new_right_m,
                    new_right_c,
                    new_boat_position,
                )
            )

    return possible_moves

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (0, 0, start, [start])) 

    visited = set() 
    while queue:
        total_cost, path_cost, current_state, path = heapq.heappop(queue)

        if current_state == goal:
            return path 

        if current_state not in visited:
            visited.add(current_state)

            for new_state in get_possible_moves(current_state):
                if new_state not in visited:
                    new_path_cost = path_cost + 1 
                    total_cost = new_path_cost + heuristic(new_state) 
                    new_path = path + [new_state]
                    heapq.heappush(queue, (total_cost, new_path_cost, new_state, new_path))

    return None 

if __name__ == "__main__":
    start_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')

    solution = astar(start_state, goal_state)

    if solution:
        print("A* Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")

