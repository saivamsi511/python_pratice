import tkinter as tk
class TicTacToe:
    def __init__(self):
        self.current_player="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttons=[]
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=20,height=10,command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append
                (button)
            self.buttons.append(row)
    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.current_player="O" if self.current_player=="X" else "X"
    def run(self):
        self.window.mainloop()
game=TicTacToe()
game.run()