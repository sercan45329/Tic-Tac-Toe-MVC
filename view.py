
from tkinter import *
from controller import Controller
from game import Game

class View:
    def __init__(self,window:Tk,model:Game):
        
        self.window=window
        
        WINDOW_WIDTH=400
        WINDOW_HEIGHT=500 
        
        self.window.title("Tic-Tac-Toe")
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        
        self.controller=None
        self.model=model
        
        self.game_state_label=Label(self.window,text=model.game_state.value,font="AkayaKanadaka 25 bold")
        self.game_state_label.pack()
        
        self.game_board_frame=Frame(self.window,bg="red")
        self.game_board_frame.pack()
        
        for row in range(3):
            for column in range(3):
                self.model.BOARD[row][column]=Button(self.game_board_frame,text="",command=lambda row=row,column=column: self.controller.on_click_button(row=row,column=column),width=8,height=8)
                self.model.BOARD[row][column].grid(row=row,column=column)
        
        self.restart_button=Button(self.window,text="Restart",command=lambda:self.controller.on_click_restart_button(),width=4,height=2)
        self.restart_button.pack()
                
    def set_controller(self,controller:Controller):
        self.controller=controller
        
    
    
        
        
        
        
        