import random
from tkinter import Button
from game import Game


class Controller:
    
    def __init__(self,view,model:Game):
        self.model=model
        self.view=view
        
    def on_click_button(self,row,column):
        
        self.check_winner(self.model.BOARD,row,column)
        
    def on_click_restart_button(self):
        
        self.model.game_state=self.model.GameState.X_TURN if random.choice([0,1])==0 else self.model.GameState.O_TURN
        for i in range(3):
            for j in range(3):
                self.model.BOARD[i][j]['text']=""
        self.view.game_state_label.config(text=self.model.game_state.value)
        
    
    def check_winner(self,board,row,column):
        
        if self.model.game_state.value=="X's Turn" and board[row][column]['text']=="":
         board[row][column]['text']='X'
         self.model.set_game_state(self.model.GameState.O_TURN)
         
        elif self.model.game_state.value=="O's Turn" and board[row][column]['text']=="":
         board[row][column]['text']='O'
         self.model.set_game_state(self.model.GameState.X_TURN)
        
        for i in range(3):
          if board[i][0]['text']==board[i][1]['text']==board[i][2]['text']!="":
            if self.model.game_state.value=="O's Turn":
                self.model.set_game_state(self.model.GameState.X_WIN)
            elif self.model.game_state.value=="X's Turn":
                self.model.set_game_state(self.model.GameState.O_WIN)
        
        for i in range(3):
          if board[0][i]['text']==board[1][i]['text']==board[2][i]['text']!="":
            if self.model.game_state.value=="O's Turn":
                self.model.set_game_state(self.model.GameState.X_WIN)
            elif self.model.game_state.value=="X's Turn":
                self.model.set_game_state(self.model.GameState.O_WIN)
        
        if board[0][0]['text']==board[1][1]['text']==board[2][2]['text']!="":
            if self.model.game_state.value=="O's Turn":
                self.model.set_game_state(self.model.GameState.X_WIN)
            elif self.model.game_state.value=="X's Turn":
                self.model.set_game_state(self.model.GameState.O_WIN)
                
        if board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
            if self.model.game_state.value=="O's Turn":
                self.model.set_game_state(self.model.GameState.X_WIN)
            elif self.model.game_state.value=="X's Turn":
                self.model.set_game_state(self.model.GameState.O_WIN)
        
        total_moves = 0
        for row in range(3):
            for column in range(3):
                text = board[row][column]['text']
                if text == "X" or text == "O":
                   total_moves += 1

        if total_moves == 9:
            self.model.set_game_state(self.model.GameState.TIE)
         
        self.view.game_state_label.config(text=self.model.game_state.value)
        
        
        
        
        