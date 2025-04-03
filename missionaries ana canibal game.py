from collections import deque

# Define the initial state (Left side: 3 missionaries, 3 cannibals, Boat on left)
INITIAL_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)

# Possible boat movements (Missionaries, Cannibals)
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid_state(m, c):
    """Check if the missionaries are safe from being eaten."""
    return (m == 0 or m >= c) and ((3-m) == 0 or (3-m) >= (3-c))

def get_next_states(state):
    """Generate all possible next states."""
    m, c, b = state
    next_states = []
    direction = -1 if b == 1 else 1  # Boat moves opposite

    for m_move, c_move in MOVES:
        new_m, new_c, new_b = m + direction * m_move, c + direction * c_move, 1 - b
        if 0 <= new_m <= 3 and 0 <= new_c <= 3 and is_valid_state(new_m, new_c):
            next_states.append((new_m, new_c, new_b))
    
    return next_states

def bfs_solve():
    """Find the shortest path using BFS."""
    queue = deque([(INITIAL_STATE, [])])  # (current_state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        # If goal is reached, return the solution path
        if current_state == GOAL_STATE:
            return path + [current_state]

        # Explore all valid next states
        for next_state in get_next_states(current_state):
            queue.append((next_state, path + [current_state]))

    return None  # No solution found

# Run the solver
solution = bfs_solve()

# Display the solution
if solution:
    print("Solution found! Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")


    
"""🔹 Step 1: Understanding the Game State
Each state is represented as (M, C, B), where:

M = Number of Missionaries on the left side.

C = Number of Cannibals on the left side.

B = Boat position (1 for left, 0 for right).

Example States:

(3,3,1) → Initial state: All on the left.

(0,0,0) → Goal state: All on the right.

(2,2,0) → Valid intermediate state.

Rules for Valid Moves
Boat can carry 1 or 2 people at a time.

Cannibals must not outnumber missionaries on either side.

Boat must always be occupied when moving.

🔹 Step 3: Explanation
State Representation

INITIAL_STATE = (3,3,1) means 3 missionaries, 3 cannibals, and the boat on the left.

GOAL_STATE = (0,0,0) means all are safely on the right.

Checking Valid States

is_valid_state() ensures that cannibals never outnumber missionaries.

Generating Next States

get_next_states() finds valid moves (e.g., (1, 1) means 1 missionary & 1 cannibal cross).

Solving Using BFS

bfs_solve() explores all possible moves and finds the shortest solution.
How BFS Works (Step-by-Step)
Start from the Initial State

Add the initial state to a queue.

Keep track of visited states to avoid loops.

Explore Possible Moves (Level by Level)

Remove a state from the queue.

Check if it's the goal state.

If not, generate all valid next states.

Add these new states to the queue.

Repeat Until Goal is Found

The first time we reach the goal, it’s the shortest path (because BFS explores all shortest paths first)."""