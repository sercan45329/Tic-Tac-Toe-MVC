from enum import Enum
import random

class Game:
    
    class GameState(Enum):
        
     X_WIN="X wins"
     O_WIN="O wins"
     TIE="Tie"
     X_TURN="X's Turn"
     O_TURN="O's Turn"

    def __init__(self):
        
     self.BOARD=[[0,0,0],[0,0,0],[0,0,0]]
     self.game_state=self.GameState.X_TURN if random.choice([0,1])==0 else self.GameState.O_TURN
    
    def set_game_state(self,game_state):
         self.game_state=game_state
         
   
         
     
    
    
    
    
    


    