#Look for ### IMPLEMENT BELOW ### tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.

#   You may add only standard python imports---i.e., ones that are automatically
#   available on TEACH.CS
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

import os
import math
# Search engines
from search import * 
# Warehouse specific classes
from warehouse import WarehouseState, Direction, warehouse_goal_state

def heur_displaced(state):
  '''A trivial example heuristic that is admissible'''
  '''INPUT: a warehouse state'''
  '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''
  '''In this case, simply the number of displaced boxes.'''   
  count = 0
  for box in state.boxes:
    if box not in state.storage:
      count += 1
    return count

def heur_manhattan_distance(state):

    '''admissible heuristic: manhattan distance'''
    '''INPUT: a warehouse state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''
    
    #We want an admissible heuristic, which is an optimistic heuristic. 
    #It must always underestimate the cost to get from the current state to the goal.
    #The sum Manhattan distance of the boxes to their closest storage spaces is such a heuristic.  
    #When calculating distances, assume there are no obstacles on the grid and that several boxes can fit in one storage bin.
    #You should implement this heuristic function exactly, even if it is tempting to improve it.
    #Your function should return a numeric value; this is the estimate of the distance to the goal.
    
    ### IMPLEMENT BELOW ###
    distance = 0
    distance_b2s = []

    # the goal of this function is 1. To find the smallest distance from on box to
    # one storage unit 2. To sum them up
    for i in state.boxes:
        for j in state.storage:
            cur = abs(j[1] - i[1]) + abs(j[0] - i[0]) # y - x, or height -width
            distance_b2s.append(cur)
        # summing up the distances
        distance = distance + min(distance_b2s)
        distance_b2s.clear() # clearing the stored values for the next cycle of i
    return distance

def evaluation(weight, sNode):
    # Evaluation function based on the assignment handout
    f_value = sNode.gval + (weight * sNode.hval)
    return f_value


def weighted_astar(initial_state, heuristic, weight, timebound = 10):

    '''Provides an implementation of weighted a-star, as described in the PA2 handout'''
    '''INPUT: a warehouse state that represents the start state, the heursitic to be used,'''
    '''       weight for the A* search (w >= 1), and a timebound (number of seconds)'''
    '''OUTPUT: A WarehouseState (if a goal is found), else False'''
    
    ### IMPLEMENT BELOW ###
    # Some of my own comments
    # 1. w is omega in this function
    # 2. the heuristic argument is the result from manhattan distance function
    # 3. f = c + wh
    # 4. The evaluation function --> what does it do?

    # cur_state = initial_state

    strat = SearchEngine("custom", "full")
    # performing the search initialization, and using the wrapped function mentioned in the handout
    status_1 = strat.init_search(initial_state, warehouse_goal_state, heuristic,
                               fval_function = (lambda sN: evaluation(weight, sN)))
    # Checking for timebound constraint
    # Status 3 is just a placeholder for the double return
    status_2,status_3 = strat.search(timebound, None)
    return status_2

def iterative_astar(initial_state, heuristic, weight, timebound = 10):

    '''Provides an implementation of iterative a-star, as described in the PA2 handout'''
    '''INPUT: a warehouse state that represents the start state, the heursitic to be used,'''
    '''       weight for the A* search (w >= 1), and a timebound (number of seconds)'''
    '''OUTPUT: A WarehouseState (if a goal is found), else False'''
    
    # HINT: Use os.times()[0] to obtain the clock time. Your code should finish within the timebound.'''
    
    ### IMPLEMENT BELOW ###
    # some of my own comments part 2
    # 1. w is omega in this function
    # 2. Timebound needs to considered with more care
    # 3. os.times()[0] to obtain the clock time (Should I make a real time variable to track rt clk time?)
    # 4. w needs to adjusted --> decrement
    # 5. The heuristic argument is still going to be result from manhattan heuristic

    # rt_time = os.times()[0]

    cycle = 0
    begin = os.times()[0]
    # begin_2 = os.times()[0]
    strat = SearchEngine("custom", "full")

    while os.times()[0] - begin < timebound:

        cycle = cycle + 1

        status_1 = strat.init_search(initial_state, warehouse_goal_state, heuristic,
                          fval_function=(lambda sN: evaluation(weight, sN)))
        status, placeholder = strat.search(timebound - os.times()[0] + begin, None)
        # testing conditions
        # begin_2 is used to track if there are sufficient time to search for another iteration
        if status == False and cycle == 1:
            return False
        elif cycle != 1:
            if status != False:
                status_prev = status
            elif status == False:
                return status_prev
        weight = weight - 2.5
        if(weight < 0):
            weight = abs(weight)

    return status


def heur_alternate(state):

    '''a better warehouse heuristic'''
    '''INPUT: a warehouse state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''        
  
    #Write a heuristic function that improves upon heur_manhattan_distance to estimate distance between the current state and the goal.
    #Your function should return a numeric value for the estimate of the distance to the goal.
    
    ### IMPLEMENT BELOW ###
    # Some of my own comments part 3
    # 1. Same as return for the manhattan heuristic, needs to return minimum estimate value of from the distance to the goal state
    # 2. Needs a better heuristic than the manhattan

    distance = 0
    obs = set()
    for i in state.obstacles:
        obs.add(i)

    distance_b2c_m = []
    # attempt with chebyshev distance: not sure if it is going to work
    # maybe try to add some distance calculations together.
    # chebyshev distance: d = max(delta_x, delta_y)'
    # temp = heur_manhattan_distance(state)


    for i in state.boxes:
        for j in state.storage:
            dx = abs(j[0] - i[0])
            dy = abs(j[1] - i[1])

            if ((j[0], j[1]-1)) in obs or ((j[0] + 1, j[1])) in obs:
                if ((j[0], j[1] + 1)) in obs or ((j[0] - 1, j[1])) in obs:
                    cur_1 = max(dx, dy) + dx + dy
                    distance_b2c_m.append(cur_1)
            else:
                cur = math.sqrt(dx**2 + dy**2) + min(dx, dy)
                distance_b2c_m.append(cur)
        distance = distance + max(distance_b2c_m)
        distance_b2c_m.clear()
    return distance
    ### END OF IMPLEMENTATION ###


