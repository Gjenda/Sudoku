# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:50:10 2023

@author: vduon
"""

import tkinter as tk
from tkinter import scrolledtext
import csv
import random
import winsound
import pygame.mixer

class Fenetre_avec_graphique():
    
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.geometry("500x400")
        self.racine.title("Sudoku Game")
        self.racine.configure(bg='lightblue')
        
        self.button_height = 2
        self.button_width = 15
        self.create_widgets(self.racine)
        
    def create_widgets(self, root):
        
        self.blankspace1 = tk.Label(root, text="")
        self.blankspace1.configure(bg='lightblue')
        self.blankspace1.pack()
        
        self.label1 = tk.Label(root,text="Welcome to the SUDOKU Game !", font = "Helvetica 16 bold" )
        self.label1.configure(bg='lightblue')
        self.label1.pack(side = tk.TOP)
        
        self.blankspace2 = tk.Label(root, text="")
        self.blankspace2.configure(bg='lightblue')
        self.blankspace2.pack()     
        
        self.blankspace3 = tk.Label(root, text="")
        self.blankspace3.configure(bg='lightblue')
        self.blankspace3.pack()   
        
        self.label2 = tk.Label(root, text="Choose a level : ", font = "Helevetica 13 bold")
        self.label2.configure(bg='lightblue')
        self.label2.pack(side = tk.TOP)     
        
        self.blankspace4 = tk.Label(root, text="")
        self.blankspace4.configure(bg='lightblue')
        self.blankspace4.pack()             
        
        self.easy_button = tk.Button(root, text = "EASY", height = self.button_height, width = self.button_width, font = "Calibri 11 bold")
        self.easy_button.pack()
        self.easy_button.bind('<Button-1>', self.easy_game)
        
        self.blankspace5 = tk.Label(root, text="")
        self.blankspace5.configure(bg='lightblue')
        self.blankspace5.pack()
        
        self.medium_button = tk.Button(root, text = "MEDIUM", height = self.button_height, width = self.button_width, font = "Calibri 11 bold")
        self.medium_button.pack()
        self.medium_button.bind('<Button-1>', self.medium_game)
        
        self.blankspace6 = tk.Label(root, text="")
        self.blankspace6.configure(bg='lightblue')
        self.blankspace6.pack()
        
        self.hard_button = tk.Button(root, text = "HARD", height = self.button_height, width = self.button_width, font = "Calibri 11 bold")
        self.hard_button.pack()
        self.hard_button.bind('<Button-1>', self.hard_game)
        
        
    def easy_game(self,event):
        """

        """
        self.sudoku_graph()
        winsound.Beep(640, 500)
    def medium_game(self, event):
        """

        """
        self.sudoku_graph()
        winsound.Beep(840, 500)
    def hard_game(self, event):
        """
        
        """
        self.sudoku_graph()
        winsound.Beep(1040, 500)
        
        
    def sudoku_graph(self):
        
        self.sudoku_window = tk.Toplevel(self.racine)
        #self.sudoku_window.geometry("600x600")
        self.sudoku_window.configure(bg='gray85')
        self.creation_grid()
        self.creation_widgets_game()
        #print(self.entries)
        #self.trying_numbers()        
        
    def creation_widgets_game(self):
        """
        """
        self.exit_button = tk.Button(self.sudoku_window, text="EXIT", font="Calibri 12 bold")
        self.exit_button.grid(row=10, column = 9)
        self.exit_button.bind('<Button-1>', self.close_windows)
        
        self.solution_button = tk.Button(self.sudoku_window, text="SOLUTION", font="Calibri 12 bold")
        self.solution_button.grid(row=10, column = 1, columnspan = 2)
        
        self.start_hint_button = tk.Button(self.sudoku_window, text="START HINT", font="Calibri 12 bold")
        self.start_hint_button.grid(row=10, column=3, columnspan=3)
        
        
        self.stop_hint_button = tk.Button(self.sudoku_window, text="STOP HINT", font="Calibri 12 bold")
        self.stop_hint_button.grid(row=10, column=5, columnspan=3)
        
        
        
        self.time = 0
        self.time_text = tk.Label(self.sudoku_window, text = "TIME : ", font = 'Calibri 12 bold')
        self.time_text.grid(row = 0, column = 2)
        self.timer_label = tk.Label(self.sudoku_window, text="",font = 'Calibri 12 bold', fg = 'red')
        self.timer_label.grid(row=0, column = 3)
        self.start_timer()
        
        
    def start_timer(self):
        self.time += 1
        self.timer_label.config(text=str(self.time))
        self.sudoku_window.after(1000, self.start_timer)
        
    def close_windows(self, event):
        self.sudoku_window.destroy()
        self.racine.destroy()
        
    def retrieve_box(self, a, b):
        """
        

        Parameters
        ----------
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        print(a)
        print(b)
        
        
        
        
   
    def creation_grid(self):
        self.cells = {}
        self.storage_entries = {}
        self.dico_store ={}
        self.entries = []
        self.box_positions = []
        
        def callback(event):
            widget = event.widget
            if widget.winfo_id() not in self.entries:
                self.entries.append(widget.winfo_id())
                print(self.entries)         
            
        for row in range(1, 10):
            for column in range(1, 10):
                if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                    color='skyblue1'
                else:
                    color='royalblue1'
                cell = tk.Frame(self.sudoku_window, highlightbackground=color, highlightcolor=color, highlightthickness=1, width=50, height=50, padx=3,  pady=3, background='black')
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell
                
                
                e = tk.Entry(self.cells[row, column], justify='center')
                e.place(height=40, width=40) #Entry box a little bit smaller than background to see the colors
                e.bind('<Button-1>', callback)
                 
            
            
            
    def text_changed(self):
        print(self.entry_text.get())
                
    def trying_numbers(self):
        self.sudoku_window.bind('<Button-1>', self.verification)
    
    def verification(self, event):
        box = event.num
        print("Box", box, "clicked")
        
        
        
    
                
    def solve_grid(self, event):
       """
       """


if __name__ == "__main__":
    app = Fenetre_avec_graphique()
    app.racine.mainloop()
