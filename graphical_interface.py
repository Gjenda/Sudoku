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
        self.debut_grid()
        #self.checking_player_try(self.changing_positions_id, self.solved_grid)
        
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
        self.solved_grid = {(1, 1, 1): 8,
        (1,2,1): 2,
        (1,3,1): 7,
        (1,1,2): 3,
        (1,2,2): 1,
        (1,3,2): 6,
        (1,1,3): 5,
        (1,2,3): 4,
        (1,3,3): 9,
        (2,1,1): 6,
        (2,2,1): 4,
        (2,3,1): 9,
        (2,1,2): 7,
        (2,2,2): 5,
        (2,3,2): 2,
        (2,1,3): 8,
        (2,2,3): 3,
        (2,3,3): 1,
        (3,1,1): 5,
        (3,2,1): 3,
        (3,3,1): 1,
        (3,1,2): 4,
        (3,2,2): 8,
        (3,3,2): 9,
        (3,1,3): 6,
        (3,2,3): 7,
        (3,3,3): 2,
        (1,1,4): 2,
        (1,2,4): 1,
        (1,3,4): 8,
        (1,1,5): 5,
        (1,2,5): 4,
        (1,3,5): 7,
        (1,1,6): 3,
        (1,2,6): 9,
        (1,3,6): 6,
        (2,1,4): 4,
        (2,2,4): 9,
        (2,3,4): 6,
        (2,1,5): 2,
        (2,2,5): 3,
        (2,3,5): 8,
        (2,1,6): 1,
        (2,2,6): 5,
        (2,3,6): 7,
        (3,1,4): 7,
        (3,2,4): 5,
        (3,3,4): 3,
        (3,1,5): 6,
        (3,2,5): 9,
        (3,3,5): 1,
        (3,1,6): 2,
        (3,2,6): 8,
        (3,3,6): 4,
        (1,1,7): 1,
        (1,2,7): 8,
        (1,3,7): 5,
        (1,1,8): 9,
        (1,2,8): 2,
        (1,3,8): 4,
        (1,1,9): 7,
        (1,2,9): 6,
        (1,3,9): 3,
        (2,1,7): 9,
        (2,2,7): 6,
        (2,3,7): 2,
        (2,1,8): 8,
        (2,2,8): 7,
        (2,3,8): 3,
        (2,1,9): 4,
        (2,2,9): 1,
        (2,3,9): 5,
        (3,1,7): 3,
        (3,2,7): 7,
        (3,3,7): 4,
        (3,1,8): 1,
        (3,2,8): 6,
        (3,3,8): 5,
        (3,1,9): 9,
        (3,2,9): 2,
        (3,3,9): 8}
        self.positions = [(1,1,1),
        (2,1,1),
        (3,1,1),
        (1,2,1),
        (2,2,1),
        (3,2,1),
        (1,3,1),
        (2,3,1),
        (3,3,1),
        (1,1,2),
        (2,1,2),
        (3,1,2),
        (1,2,2),
        (2,2,2),
        (3,2,2),
        (1,3,2),
        (2,3,2),
        (3,3,2),
        (1,1,3),
        (2,1,3),
        (3,1,3),
        (1,2,3),
        (2,2,3),
        (3,2,3),
        (1,3,3),
        (2,3,3),
        (3,3,3),
        (1,1,4),
        (2,1,4),
        (3,1,4),
        (1,2,4),
        (2,2,4),
        (3,2,4),
        (1,3,4),
        (2,3,4),
        (3,3,4),
        (1,1,5),
        (2,1,5),
        (3,1,5),
        (1,2,5),
        (2,2,5),
        (3,2,5),
        (1,3,5),
        (2,3,5),
        (3,3,5),
        (1,1,6),
        (2,1,6),
        (3,1,6),
        (1,2,6),
        (2,2,6),
        (3,2,6),
        (1,3,6),
        (2,3,6),
        (3,3,6),
        (1,1,7),
        (2,1,7),
        (3,1,7),
        (1,2,7),
        (2,2,7),
        (3,2,7),
        (1,3,7),
        (2,3,7),
        (3,3,7),
        (1,1,8),
        (2,1,8),
        (3,1,8),
        (1,2,8),
        (2,2,8),
        (3,2,8),
        (1,3,8),
        (2,3,8),
        (3,3,8),
        (1,1,9),
        (2,1,9),
        (3,1,9),
        (1,2,9),
        (2,2,9),
        (3,2,9),
        (1,3,9),
        (2,3,9),
        (3,3,9)]
        
        
        self.positions_v2 = [(1,1,1),
        (1,2,1),
        (1,3,1),
        (1,1,2),
        (1,2,2),
        (1,3,2),
        (1,1,3),
        (1,2,3),
        (1,3,3),
        (2,1,1),
        (2,2,1),
        (2,3,1),
        (2,1,2),
        (2,2,2),
        (2,3,2),
        (2,1,3),
        (2,2,3),
        (2,3,3),
        (3,1,1),
        (3,2,1),
        (3,3,1),
        (3,1,2),
        (3,2,2),
        (3,3,2),
        (3,1,3),
        (3,2,3),
        (3,3,3),
        (1,1,4),
        (1,2,4),
        (1,3,4),
        (1,1,5),
        (1,2,5),
        (1,3,5),
        (1,1,6),
        (1,2,6),
        (1,3,6),
        (2,1,4),
        (2,2,4),
        (2,3,4),
        (2,1,5),
        (2,2,5),
        (2,3,5),
        (2,1,6),
        (2,2,6),
        (2,3,6),
        (3,1,4),
        (3,2,4),
        (3,3,4),
        (3,1,5),
        (3,2,5),
        (3,3,5),
        (3,1,6),
        (3,2,6),
        (3,3,6),
        (1,1,7),
        (1,2,7),
        (1,3,7),
        (1,1,8),
        (1,2,8),
        (1,3,8),
        (1,1,9),
        (1,2,9),
        (1,3,9),
        (2,1,7),
        (2,2,7),
        (2,3,7),
        (2,1,8),
        (2,2,8),
        (2,3,8),
        (2,1,9),
        (2,2,9),
        (2,3,9),
        (3,1,7),
        (3,2,7),
        (3,3,7),
        (3,1,8),
        (3,2,8),
        (3,3,8),
        (3,1,9),
        (3,2,9),
        (3,3,9)]
        self.dictionnary_1 = {}
        self.dictionnary_2 = {}
        self.entries = []
        self.entries_ids = []
        
        def update_player_grid(event):
            resultat = False
            widget = event.widget
            
            for key2, value2 in self.dictionnary_2.items():
                if widget.winfo_id() == key2:
                    self.dictionnary_2[key2] = int(widget.get())
            self.changing_id_value = (widget.winfo_id(), int(widget.get()))
            for key1 , value1 in self.dictionnary_1.items():
                if widget.winfo_id() == value1:
                    self.changing_positions_id = (key1, value1)
            self.changing_positions_value = (self.changing_positions_id[0], self.changing_id_value[1])
            
            #print(self.changing_positions_id)
            #print(self.changing_id_value)
            print(self.changing_positions_value)
            print("")
            #for key, value in self.solved_grid.items():
                #print((key, value))
            
            i = 0                
            while not resultat or i <= len(self.solved_grid.values()):
                for key, value in self.solved_grid.items():
                    if (key, int(value)) == self.changing_positions_value:
                        resultat = True
                    else:
                        i += 1
            '''
            for key, value in self.solved_grid.items():
                    if (key, int(value)) == (self.changing_positions_value[0], self.changing_positions_value[1]):
                        print('correct')
                    else:
                        print('faux')
            '''            
            if not resultat:
                widget.config(bg='red')
            else:
                widget.config(bg='green')
            
                    
        def show_id(event):
            widget = event.widget
            for key, value in self.dictionnary_1.items():
                if widget.winfo_id() == value:
                    print((key, value))
            #print(widget.winfo_id())
                
            
        def storage_positions_and_id(a,b):
            self.dictionnary_1 = {k: v for k, v in zip(a, b)}
            #for key, value in self.dictionnary_1.items():
                #print(f"{key}: {value}")
                
        #def checking_player_try(changing_element):
            
            
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
                e.bind('<Return>', update_player_grid)
                #e.bind('<Button-1>', show_id)
                #checking_player_try(e.bind('<Return>', update_player_grid))
                #print(e.winfo_id())
                self.entries_ids.append(e.winfo_id())
                
                     
                
                
        self.dictionnary_2 = {key: 0 for key in self.entries_ids}
        #print(self.dictionnary_2)
        storage_positions_and_id(self.positions_v2, self.entries_ids)
        #for k, v in self.dictionnary_2.items():
            #print(f"{k}: {v}")
            
    def debut_grid(self):
        #num_items = random.randint(1, len(self.solved_grid))
        list_revealing_id = []
        selected_items = random.sample(self.solved_grid.items(), 38)
        self.selected_dict = dict(selected_items)
        print(self.selected_dict)
        for key1, value1 in self.dictionnary_1.items():
            for key2 in self.selected_dict.keys():
                if key1 == key2:
                    list_revealing_id.append(value1)
        print(list_revealing_id)
        '''
        for widget_id in list_revealing_id:
            widget = self.sudoku_window.nametowidget(f".{widget_id}")  # Get the widget by ID
            if isinstance(widget, tk.Entry):
                content = widget.get()  # Retrieve the content of the entry box
                print(f"Widget ID: {widget_id}, Content: {content}")
                '''
    def checking_player_try(self):
        """
        """
        
        
            
                 
            
            
            
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
