import tkinter
from game import Game
from controller import Controller
from view import View

window=tkinter.Tk()
model=Game()
view=View(window,model)
controller=Controller(view,model)
view.set_controller(controller=controller)

def run():
 window.mainloop()

run()
