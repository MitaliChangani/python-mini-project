# Maze Solver using DFS or BFS

class Node():
    
    """Represents a node in the search tree.

        state: Position in the maze (row, col).

        parent: Previous node (used to trace the solution path).

        action: Direction taken to reach this node ("up", "down", etc.).
    """
    def __init__(self, state, parent, action):
        self.state = state 
        self.parent = parent
        self.action= action
        
class StackFrontier():   # Initializes an empty list to store nodes yet to be explored (DFS uses a stack).
    def __init__(self):
        self.frontier = []
        
    def add(self, node):  # Adds a new node to the frontier (top of the stack).
        self.frontier.append(node)
        
    def contain_state(self, state):  # Checks if a state is already in the frontier (to prevent loops).
        return any(node.state == state for node in self.frontier)
    
    def empty(self):  # Returns True if the frontier is empty (no more nodes to explore).
        return len(self.frontier)==0
    
    def remove(self):  # Removes the last node added (LIFO behavior of DFS stack).
        if self.empty():
            raise Exception("Empty frontier.")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):  # Inherits StackFrontier but overrides remove() to remove the first node (FIFO behavior of a queue → BFS).
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier.")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class Maze():  # Loads a maze from a text file like maze1.txt
    def __init__(self, filename):
        
        #  read file and set hight and width of maze 
        with open("maze1.txt", "r") as f:
            contents = f.read()
            
        #  validate start and goal
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point (A).")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal point (B).")
        
        # determine hight and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        
        #  keep trac of walls
        
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(True)
            self.walls.append(row)
        self.solution = None
        
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            
    def neighbors(self, state):    # Calculates possible movement directions.
        row, col = state
        
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        
        # ensure actions are valid
        results = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    results.append((action, (r, c)))
            except IndexError:
                continue
        return results
    
    def solve(self):   #Initializes the DFS or BFS search with the start node and explored set.
        
        """finds a solution to maze, if one exists."""
        
        # Keep tracks of numbe of states explored
        self.num_explored = 0
        
        # Iitializing frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()  # DFS - Depth-First Search , OR
        # frontier = QueueFrontier()  # BFS - Breadth-First Search
        frontier.add(start)
        
        # Initialize an empty explored set
        self.explored = set()
        
        #  keep ooping until solution is found or frontier is empty
        while True:
            # If there are no more states to explore, then there is no solution
            if frontier.empty():
                raise Exception("No solution found.")
            
            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1
            
            # If the node is the goal, then we have found a solution
            if node.state == self.goal:
                actions = []
                cells = []
                
                # follow the parent nodes to find the solution
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            # Mark the state as explored
            self.explored.add(node.state)
            
            # Add neighbors to the frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contain_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
                    
if __name__ == "__main__":
    maze = Maze("maze1.txt")
    print("Maze before solving:")
    maze.print()
    maze.solve()
    print("\nMaze after solving:")
    maze.print()

    print("\nActions to reach the goal:")
    print(maze.solution[0])

    print("\nPath (coordinates):")
    print(maze.solution[1])