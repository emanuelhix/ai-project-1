# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Implements DFS using a stack for the frontier.
    """
    fringe = util.Stack()
    closed = set()
    
    start_state = problem.getStartState()
    fringe.push((start_state, []))
    
    while not fringe.isEmpty():
        state, path = fringe.pop()
        
        if state in closed:
            continue
        
        closed.add(state)
        
        if problem.isGoalState(state):
            return path
        
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]))
                
    return []
        
def breadthFirstSearch(problem: SearchProblem):
    """
    Implements BFS using a queue for the frontier.
    """
    fringe = util.Queue()
    closed = set()
    
    start_state = problem.getStartState()
    fringe.push((start_state, []))
    
    while not fringe.isEmpty():
        state, path = fringe.pop()
        
        if state in closed:
            continue
        
        closed.add(state)
        
        if problem.isGoalState(state):
            return path
        
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]))
                
    return []

def uniformCostSearch(problem: SearchProblem):
    """
    Implements UCS using a priority queue for the frontier.
    """
    fringe = util.PriorityQueue()  
    closed = {}  
    
    start_state = problem.getStartState()
    fringe.push((start_state, [], 0), 0)  
    
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()  
        
        if state in closed and closed[state] <= cost:
            continue  
        
        closed[state] = cost
         
        if problem.isGoalState(state):
            return path
        
        for successor, action, _ in problem.getSuccessors(state):
            new_path = path + [action]
            cost = problem.getCostOfActions(new_path)
            fringe.push((successor, new_path, cost), cost)  
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Implements A* using a priority queue for the frontier.
    """
    open = util.PriorityQueue()  
    closed = {}  
    
    start_state = problem.getStartState()
    open.push((start_state, [], 0), heuristic(start_state, problem))  
    
    while not open.isEmpty():
        curr_state, path, g_cost = open.pop()  
        
        if curr_state in closed and closed[curr_state] <= g_cost:
            continue  
        
        closed[curr_state] = g_cost  

        if problem.isGoalState(curr_state):
            return path  

        for successor, action, step_cost in problem.getSuccessors(curr_state):
            new_path = path + [action]
            new_g_cost = g_cost + step_cost
            # if the new g cost is less than a g-cost we already calculated for this successor, push it onto open. 
            # if the successor hasn't been seen before, the default value is inf, which will always cause the successor to be pushed onto open.
            if new_g_cost < closed.get(successor, float("inf")):
                new_f_cost = new_g_cost + heuristic(successor, problem)
                open.push((successor, new_path, new_g_cost), new_f_cost)  
    
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
