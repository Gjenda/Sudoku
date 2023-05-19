# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:58:14 2023

@author: vduon
"""

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

class GUI():
    
    #MAIN FUNCTIONS
    
    def __init__(self, solved_grid):    # The class GUI will takes as entry: 1) the solved_grid and some answers to guide the player, 2) the  
            
        self.solved_sudoku = solved_grid # We define self.solved_sudoku as the dictionnary that is given in entry in the Main class
        
        self.racine = tk.Tk()       
        self.racine.configure(bg='gray85')
        self.creation_grid()        # Creation of the grid (entry boxes)
        self.creation_widgets_game()    # Creation of the other functionnalities of our game (solution, hint, timer, exit)
        self.debut_grid()       # Display the first answers to guide the player
       
        
    def creation_widgets_game(self):   # Creation of the other functionalities of the game
        """doc
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
        
    def creation_grid(self):        # Creation of the entry boxes in a loop + the callback functions linked to them
        self.cells = {}
        self.storage_entries = {}
        # We created a list to store the positions of every boxes in a the format (COLUMN, ROW, #SQUARE)
        self.box_positions_list = [(1,1,1),
        (2,1,1),
        (3,1,1),
        (1,1,2),
        (2,1,2),
        (3,1,2),
        (1,1,3),
        (2,1,3),
        (3,1,3),
        (1,2,1),
        (2,2,1),
        (3,2,1),
        (1,2,2),
        (2,2,2),
        (3,2,2),
        (1,2,3),
        (2,2,3),
        (3,2,3),
        (1,3,1),
        (2,3,1),
        (3,3,1),
        (1,3,2),
        (2,3,2),
        (3,3,2),
        (1,3,3),
        (2,3,3),
        (3,3,3),
        (1,1,4),
        (2,1,4),
        (3,1,4),
        (1,1,5),
        (2,1,5),
        (3,1,5),
        (1,1,6),
        (2,1,6),
        (3,1,6),
        (1,2,4),
        (2,2,4),
        (3,2,4),
        (1,2,5),
        (2,2,5),
        (3,2,5),
        (1,2,6),
        (2,2,6),
        (3,2,6),
        (1,3,4),
        (2,3,4),
        (3,3,4),
        (1,3,5),
        (2,3,5),
        (3,3,5),
        (1,3,6),
        (2,3,6),
        (3,3,6),
        (1,1,7),
        (2,1,7),
        (3,1,7),
        (1,1,8),
        (2,1,8),
        (3,1,8),
        (1,1,9),
        (2,1,9),
        (3,1,9),
        (1,2,7),
        (2,2,7),
        (3,2,7),
        (1,2,8),
        (2,2,8),
        (3,2,8),
        (1,2,9),
        (2,2,9),
        (3,2,9),
        (1,3,7),
        (2,3,7),
        (3,3,7),
        (1,3,8),
        (2,3,8),
        (3,3,8),
        (1,3,9),
        (2,3,9),
        (3,3,9)]
        
        self.dictionary_positions_id = {}       #Dictionary that stores : KEY => box_position, VALUE => box_id
        self.dictionary_id_values = {}          #Dictionary that stores : KEY => box_id, VALUE => box_value
        self.entries_ids = []       # List to store all the id number of the entry boxes that are created          
            
        for row in range(1, 10):
            for column in range(1, 10):
                if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                    color='skyblue1'
                else:
                    color='royalblue1'
                # To get a better visual, we change the color of the background for different #square number
                cell = tk.Frame(self.sudoku_window, highlightbackground=color, highlightcolor=color, highlightthickness=1, width=50, height=50, padx=3,  pady=3, background='black')
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell
                
                # We create the entry boxes
                e = tk.Entry(self.cells[row, column], justify='center')
                e.place(height=40, width=40) #Entry box a little bit smaller than background to see the colors
                e.bind('<Return>', self.update_player_grid)
                #e.bind('<Button-1>', show_id)      Command just to check that the program returns us the id of the box we just cliked on
                self.entries_ids.append(e.winfo_id())  # Add the id of the box into a list storing all the id of the 81 boxes   
                
        self.dictionary_id_values = {key: 0 for key in self.entries_ids}
        self.storage_positions_and_id(self.box_positions_list, self.entries_ids) # Merge the list of the box positions and the list of the ids into one single dictionary
    
    #SECONDARY FUNCTIONS
        
        
    def start_timer(self):
        """doc
        """
        self.time += 1
        self.timer_label.config(text=str(self.time))
        self.sudoku_window.after(1000, self.start_timer)
        
    def close_windows(self, event):     # Close all the actual Sudoku window if the button EXIT is pressed
        self.sudoku_window.destroy()
        self.racine.destroy()
        
    def update_player_grid(self,event):     # Take into account the try that player did and check with the solved_grid if it is correct or not
        resultat = False
        widget = event.widget
        
        for box_id, box_value in self.dictionary_id_values.items():
            if widget.winfo_id() == box_id:
                self.dictionary_id_values[box_id] = int(widget.get())
                
        self.changing_id_value = (widget.winfo_id(), int(widget.get()))
        
        for box_position , box_id in self.dictionary_positions_id.items():
            if widget.winfo_id() == box_id:
                self.changing_positions_id = (box_position, box_id)
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
            
    def show_id(self,event):        # OPTIONAL : Display the id of the box that has just been clicked on
        widget = event.widget
        for box_position, box_id in self.dictionary_positions_id.items():
            if widget.winfo_id() == box_id:
                print((box_position, box_id))

    def storage_positions_and_id(self,box_position_list,box_id_list): # Merge the list of the box positions and the list of the ids into one single dictionary
            self.dictionary_positions_id = {k: v for k, v in zip(box_position_list, box_id_list)}  
    
    def debut_grid(self):   # Display the value of certain box positions at the beginning of the game to guide the player
    
    
        #num_items = random.randint(1, len(self.solved_grid))
        list_revealing_id = []
        selected_items = random.sample(self.solved_grid.items(), 38)
        self.selected_dict = dict(selected_items)
        print(self.selected_dict)
        for box_position, box_id in self.dictionary_positions_id.items():
            for position_to_reveal in self.selected_dict.keys():
                if box_position == position_to_reveal:
                    list_revealing_id.append(box_id)
        print(list_revealing_id)
 
