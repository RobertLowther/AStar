class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, blocked=False):
        self.parent = parent
        self.position = position
        self.blocked = blocked

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        if not self or not other:
            return False
        return self.position == other.position

class Maze():
    """A maze class for A* Pathfinding"""

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.nodes = []

        for i in range(self.height):
            nodes.append([])
            for j in range(self.width):
                nodes[i].append(Node(position = (i, j)))

    def __init__(self, maze):
        self.width = len(maze[0])
        self.height = len(maze)
        self.nodes = []

        for i in range(self.height):
            self.nodes.append([])
            for j in range(self.width):
                self.nodes[i].append(Node(position = (i, j), blocked = maze[i][j] == 1))

    def GetNode(self, pos):
        if pos[0] >= 0 and pos[0] < len(self.nodes) and pos[1] >= 0 and pos[1] < len(self.nodes[0]):
            return self.nodes[pos[0]][pos[1]]

    def FindPath(self, start, end):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = self.GetNode(start)
        end_node = self.GetNode(end)

        if not start_node or not end_node:
            print("Start and end node cannot be Nonetye")
            return None

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Generate children
            for new_position in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

                # Get node position
                next_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Get next node based on next position
                next_node = self.GetNode(next_position)

                # Make sure within range
                if not next_node or next_node.blocked or next_node in closed_list:
                     continue

                newG = next_node.g + GetDeltaG(next_node.position, current_node.position)

                if next_node in open_list:
                    if next_node.g < newG:
                        continue
                else:
                    open_list.append(next_node)
                    print()

                # Set node parent and stats
                next_node.g = newG
                next_node.h = ((next_node.position[0] - end_node.position[0]) ** 2) + ((next_node.position[1] - end_node.position[1]) ** 2)
                next_node.f = next_node.h + next_node.g
                next_node.parent = current_node

                #self.PrintMap(open_list, closed_list)
                #print()

    def PrintMap(self, open_list, closed_list):
        print()
        for i in range(self.height):
            for j in range(self.width):
                if self.nodes[i][j].blocked:
                    print(" # ", end="")
                elif self.nodes[i][j] in open_list:
                    print(" 1 ", end="")
                elif self.nodes[i][j] in closed_list:
                    print(" 2 ", end="")
                else:
                    print(" 0 ", end="")
            print()


'''
return the distance between two adjascent positions
'''
def GetDeltaG(pos1, pos2):
    if pos1[0] != pos2[0] and pos1[1] != pos2[0]:
        return 1.41
    else:
        return 1

def main():

    mazeData = [[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]]

    maze = Maze(mazeData)

    start = (0, 0)
    end = (0, 9)

    path = maze.FindPath(start, end)
    print(path)

    if path:
        for i in range(maze.height):
            for j in range(maze.width):
                if (i, j) in  path:
                    print (" X ", end = "")
                elif maze.nodes[i][j].blocked == 1:
                    print(" # ", end = "")
                else:
                    print(" . ", end = "")
            print()


if __name__ == '__main__':
    main()