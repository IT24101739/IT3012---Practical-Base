# agent.py

import random

class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

class SimpleReflexAgent:

    def sense_and_act(self, percept: dict) -> str:
        
        if percept.get('food_here'):
            return 'Up'       
        if percept.get('wall_ahead'):
            return 'Left'    
        if percept.get('toxin_here'):
            return 'Down'
        if percept.get('opponent_nearby'):
            return 'Right'
        if percept.get('food_remaining'):
            return 'Up'
        if percept.get('collision'):
            return 'Down'
        return 'Up'       

class ModelBasedAgent:

    def __init__(self):

        self.visited_cells = set()
        self.x, self.y = 0, 0
        self.path=[]

    def sense_and_act(self, percept):

        here = (self.x, self.y)
        self.visited_cells.add((self.x, self.y))

        moves ={

            'Up': (self.x, self.y + 1),
            'Down': (self.x, self.y - 1),
            'Left': (self.x - 1, self.y),
            'Right': (self.x + 1, self.y),
        }

        action_to ={cell:action for  action, cell in moves.items()}

        candidates = ['Up', 'Down', 'Left', 'Right']

        if percept.get('wall_up') or percept.get('toxin_up')  or percept.get('opponent_up'):
            candidates.remove('Up')
        if percept.get('wall_down') or percept.get('toxin_down') or percept.get('opponent_down'):
            candidates.remove('Down')
        if percept.get('wall_left') or percept.get('toxin_left') or percept.get('opponent_left'):
            candidates.remove('Left')
        if percept.get('wall_right') or percept.get('toxin_right') or percept.get('opponent_right'):
            candidates.remove('Right')
        

        ## find a new cell to visit
        for action in candidates:
            next_cell = moves[action]
            if next_cell not in self.visited_cells:
                self.path.append(here)
                self.apply_move(action)
                return action

        ## if no new cell to visit, backtrack
        if self.path:
            prev = self.path.pop()
            action = action_to[prev]
            if action is not None:
                self.apply_move(action)
                return action

        ## nowhere to go

        action = candidates[0] if candidates else 'Up'
        self.apply_move(action)
        return action
       
    def apply_move(self, action):

        if action == 'Up':
            self.y += 1
        elif action == 'Down':
            self.y -= 1
        elif action == 'Left':
            self.x -= 1
        elif action == 'Right':
            self.x += 1
        self.visited_cells.add((self.x, self.y))