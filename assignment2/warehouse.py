'''Warehouse routines.

    A) Class WarehouseState

    A specializion of the StateSpace Class that is tailored to the warehouse storage problem.

    B) class Direction

    An encoding of the directions of movement that are possible for robot operators.
    
'''

from search import *

class WarehouseState(StateSpace):

    def __init__(self, action, gval, parent, width, height, robots, boxes, storage, obstacles):
        '''
        Creates a new warehouse state.
        @param width: The room's X dimension (excluding walls).
        @param height: The room's Y dimension (excluding walls).
        @param robots: A tuple of all the robots' locations. Each robot is denoted by its index in the list.
        @param boxes: A frozenset of all the boxes.
        @param storage: A frozenset of all the storage points.
        @param obstacles: A frozenset of all the impassable obstacles.
        '''
        StateSpace.__init__(self, action, gval, parent)
        self.width = width
        self.height = height
        self.robots = robots
        self.boxes = boxes
        self.storage = storage
        self.obstacles = obstacles    

    def successors(self):
        '''
        Generates all the actions that can be performed from this state, and the states those actions will create.        
        '''
        successors = []
        transition_cost = 1
        moved_boxes = frozenset()

        for robot in range(0, len(self.robots)):
          for direction in (UP, RIGHT, DOWN, LEFT):
              new_location = direction.move(self.robots[robot])
              new_robots = list(self.robots);
              new_robots.remove(self.robots[robot])
              new_robots = tuple(new_robots)
              new_boxes = set(self.boxes)
              new_moved_boxes = set(moved_boxes)
              
              if new_location[0] < 0 or new_location[0] >= self.width:
                  continue
              if new_location[1] < 0 or new_location[1] >= self.height:
                  continue
              if new_location in self.obstacles:
                  continue
              if new_location in new_robots:
                  continue
              if new_location in moved_boxes:
                  continue
              
              if new_location in self.boxes:
                  new_box_location = direction.move(new_location)
                  
                  if new_box_location[0] < 0 or new_box_location[0] >= self.width:
                      continue
                  if new_box_location[1] < 0 or new_box_location[1] >= self.height:
                      continue
                  if new_box_location in self.obstacles:
                      continue
                  if new_box_location in new_robots:
                      continue
                  if new_box_location in new_boxes:
                      continue
                  
                  new_boxes.remove(new_location)
                  new_boxes.add(new_box_location)
                  new_moved_boxes.add(new_box_location)
              
              new_robots = list(self.robots)
              new_robots[robot] = new_location
              new_robots = tuple(new_robots)

              new_state = WarehouseState(str(robot) + " " + direction.name, self.gval + transition_cost, self, self.width, self.height, new_robots, frozenset(new_boxes), self.storage, self.obstacles)
              successors.append(new_state)

        return successors

    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent a state.'''
        return hash((self.robots, self.boxes))       

    def state_string(self):
        '''Returns a string representation fo a state that can be printed to stdout.'''        
        map = []
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row += [' ']
            map += [row]
        
        for storage_point in self.storage:
            map[storage_point[1]][storage_point[0]] = '.'
        for obstacle in self.obstacles:
            map[obstacle[1]][obstacle[0]] = '#'
        for i, robot in enumerate(self.robots):
            if robot in self.storage:
                map[robot[1]][robot[0]] = chr(ord('A') + i)
            else:
                map[robot[1]][robot[0]] = chr(ord('a') + i)
        for box in self.boxes:
            if box in self.storage:
                map[box[1]][box[0]] = '*'
            else:
                map[box[1]][box[0]] = '$'
        
        for y in range(0, self.height):
            map[y] = ['#'] + map[y]
            map[y] = map[y] + ['#']
        map = ['#' * (self.width + 2)] + map
        map = map + ['#' * (self.width + 2)]

        s = ''
        for row in map:
            for char in row:
                s += char
            s += '\n'

        return s        

    def print_state(self):
        '''
        Prints the string representation of the state. ASCII art FTW!
        '''        
        print("ACTION was " + self.action)      
        print(self.state_string())


def warehouse_goal_state(state):
  '''Returns True if we have reached a goal state'''
  '''INPUT: a warehouse state'''
  '''OUTPUT: True (if goal) or False (if not)'''  
  for box in state.boxes:
    if box not in state.storage:
      return False
  return True


'''
Warehouse Directions: encodes directions of movement that are possible for each robot.
'''
class Direction():
    '''
    A direction of movement.
    '''
    
    def __init__(self, name, delta):
        '''
        Creates a new direction.
        @param name: The direction's name.
        @param delta: The coordinate modification needed for moving in the specified direction.
        '''
        self.name = name
        self.delta = delta
    
    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets 
        and dictionaries.
        @return: The hash value of the action.
        '''
        return hash(self.name)
    
    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        return str(self.name)
    
    def __repr__(self):
        return self.__str__()
    
    def move(self, location):
        '''
        @return: Moving from the given location in this direction will result in the returned location.
        '''
        return (location[0] + self.delta[0], location[1] + self.delta[1])


#Global Directions
UP = Direction("up", (0, -1))
RIGHT = Direction("right", (1, 0))
DOWN = Direction("down", (0, 1))
LEFT = Direction("left", (-1, 0))



  
