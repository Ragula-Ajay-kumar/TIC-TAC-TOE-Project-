import tkinter as tk
from tkinter import messagebox

class tictactoe:
    
    def __init__(self):
        self.curr_player="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttonsGrid=[]
        
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=20,height=10,command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttonsGrid.append(row)
            
    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.curr_player 
            self.buttonsGrid[row][col].config(text=self.curr_player)
            if self.check_winner(self.curr_player):
                messagebox.showinfo("Game over","The winner is" + self.curr_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game over","Its a Draw")
                self.window.quit()
            self.curr_player="O" if self.curr_player=="X" else "X"
            
    def check_winner(self,player):
        for i in range(3):
            if player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return True
            if player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return True
        if player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
                return True
        if player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
                return True
            
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
            return True
    
    def run(self):
        self.window.mainloop()
        
game=tictactoe()
game.run()
        