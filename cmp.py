class Graph:
    def __init__(self, n):
        self.al = [[] for i in range(n)]

    def add(self, i, j):
        self.al[i].append(j)

def solve(board, s, t):
    """
    board is an array of adjacency lists, i.e., board[u] is the list of
    neighbours of u.

    s is the desired starting point.

    t is the desired ending point.

    Compute the minimum number of steps that Chromorpher can start from s with
    colour 0 and ends at t with colour 0.  Or None if it can't be done.
    """
    num_steps = 0
    passed = {}
    start = s
    finish = (t, 0)
    # add all possible position and colur combinations to a dictionary
    for vertex in range(len(board)):
        for colour in range(4):
            passed[(vertex, colour)] = []
            for incident in board[vertex]:
                passed[(vertex, colour)].append((incident, (colour + 1) % 4))
    
    # need one queue to store current node being worked on, one queue 
    # for BFS algorithm
    q1 = []
    q1.append((start, 0))
    q2 = []
    
    # BFS algorithm
    # if queue is not empty
    while len(q1) != 0:
        # go through all the possible states in the graph
        for state in q1:
            # if a solution has been found, return number of steps needed
            if state == finish:
                return num_steps
            # go through incident nodes and add to the queue
            for i in passed[state]:
                q2.append(i)

            passed[state] = []
        # increment steps, update queue
        num_steps += 1
        q1 = q2
        q2 = []

    # if loop finishes, then there is no solution so None is returned
    return None
        
if __name__ == "__main__":

    g = Graph(8)
    g.add(3,1); g.add(1,4); g.add(4,2); g.add(2,5);
    g.add(5,6); g.add(6,0); g.add(0,7); g.add(7,3);
    g.add(1,0);

    print(solve(g.al, 0, 1))
    
    g = Graph(8)
    g.add(3,6); g.add(6,0); g.add(0,7); g.add(7,3);
    g.add(1,5); g.add(5,4); g.add(4,2); g.add(2,3); g.add(3,1);
    print(solve(g.al, 3, 6))
    
    