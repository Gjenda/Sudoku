#display_table() is not needed, it's just to visualize the game a little for the mini code test at the bottom

example_sudoku = {(1,1,1):0 ,
        (2,1,1):0 ,
        (3,1,1):0 ,
        (1,2,1):6 ,
        (2,2,1):4 ,
        (3,2,1):9 ,
        (1,3,1):5 ,
        (2,3,1):3 ,
        (3,3,1):1 ,
        (1,1,2):3 ,
        (2,1,2):1 ,
        (3,1,2):0 ,
        (1,2,2):0 ,
        (2,2,2):0 ,
        (3,2,2):0 ,
        (1,3,2):0 ,
        (2,3,2):8 ,
        (3,3,2):0 ,
        (1,1,3):5 ,
        (2,1,3):0 ,
        (3,1,3):9 ,
        (1,2,3):8 ,
        (2,2,3):0 ,
        (3,2,3):1 ,
        (1,3,3):6 ,
        (2,3,3):7 ,
        (3,3,3):0 ,
        (1,1,4):2 ,
        (2,1,4):1 ,
        (3,1,4):0 ,
        (1,2,4):0 ,
        (2,2,4):9 ,
        (3,2,4):6 ,
        (1,3,4):7 ,
        (2,3,4):0 ,
        (3,3,4):0 ,
        (1,1,5):0 ,
        (2,1,5):4 ,
        (3,1,5):0 ,
        (1,2,5):2 ,
        (2,2,5):0 ,
        (3,2,5):8 ,
        (1,3,5):6 ,
        (2,3,5):0 ,
        (3,3,5):1 ,
        (1,1,6):3 ,
        (2,1,6):0 ,
        (3,1,6):6 ,
        (1,2,6):0 ,
        (2,2,6):0 ,
        (3,2,6):0 ,
        (1,3,6):0 ,
        (2,3,6):8 ,
        (3,3,6):0 ,
        (1,1,7):1 ,
        (2,1,7):0 ,
        (3,1,7):5 ,
        (1,2,7):9 ,
        (2,2,7):0 ,
        (3,2,7):0 ,
        (1,3,7):3 ,
        (2,3,7):0 ,
        (3,3,7):0 ,
        (1,1,8):9 ,
        (2,1,8):0 ,
        (3,1,8):0 ,
        (1,2,8):0 ,
        (2,2,8):0 ,
        (3,2,8):3 ,
        (1,3,8):1 ,
        (2,3,8):6 ,
        (3,3,8):0 ,
        (1,1,9):7 ,
        (2,1,9):0 ,
        (3,1,9):0 ,
        (1,2,9):0 ,
        (2,2,9):0 ,
        (3,2,9):0 ,
        (1,3,9):0 ,
        (2,3,9):0 ,
        (3,3,9):8 }


copied_dicto = example_sudoku.copy()

def display_table(dicto):
        for y in range (1,10):    # Y axis rows
                if y == 4 or y == 7:
                        print("|-----------|")
                row = "|"
                for z in range (1,4):    # Z boxes (advancing horizontally)
                        for x in range (1,4):    # X axis columns
                                if y <= 3:
                                        row += str([dicto[(x,y,z)]][0])
                                elif y <= 6:
                                        row += str([dicto[(x,y-3,z+3)]][0])  #because Y is defined until 3
                                else:
                                        row += str([dicto[(x,y-6,z+6)]][0])
                        row += "|"
                print(row.strip(",").strip("'"))

sudoku_list=display_table(example_sudoku)

print("________________________________________________________________")

def control_cases():
        box_for_x = 0     #initiate final result
        if z == 1 or  z == 4 or  z == 7:     #if box is on the left give 1
                box_for_x = 1
        elif z == 2 or  z == 5 or  z == 8:     #middle box
                box_for_x = 2
        else:  #if z == 3 or  z == 6 or  z == 9:     #right box
                box_for_x = 3
        
        box_for_y = 0
        if z == 1 or  z == 2 or  z == 3:     #if box is on the top
                box_for_y = 1
        elif z == 4 or  z == 5 or  z == 6:     #middle box
                box_for_y = 2
        else:     #bottom box
                box_for_y = 3
        return (box_for_x, box_for_y) 


def control_loop_x(k,l):
        for a in range(1,4):
                for c in range(z+k,z+l):
                        if copied_dicto[(a,y,c)] == copied_dicto[(x,y,z)] and (a,y,c) != (x,y,z):   #not to compare with itself
                                return False
        return True

def control_loop_y(k,l):
        for b in range(1,4):
                for c in range(z+k,z+l, 3):   #step = 3
                        if copied_dicto[(x,b,c)] == copied_dicto[(x,y,z)] and (x,b,c) != (x,y,z):
                                return False
        return True

def control_loop_z():
        for b in range(1,4):
                for a in range(1,4):
                        if copied_dicto[(a,b,z)] == copied_dicto[(x,y,z)] and (a,b,z) != (x,y,z):
                                return False
        return True


def control():     #returns True if position is safe to play, False if numberb is unplacable
        result = True     #initiated with no same values found yet
        (x_verify, y_verify) = control_cases()     #check which box you're in, to know which other ones to compare to
        if x_verify == 1:     #have to check the other two boxes on the right
                result = control_loop_x(0,3)
        elif x_verify == 2:
                result = control_loop_x(1,2)
        else:   #x_verify == 3
                result = control_loop_x(-2, 1)
        if result == True:
                if y_verify == 1:
                        result = control_loop_y(0,7)
                elif y_verify == 2:
                        result = control_loop_y(-3,4)
                else:
                        result = control_loop_y(-6, 1)
        if result == True:
                result = control_loop_z()
        
        return result



#Test program
x = int(input("Please give the X coordinate you want to place: "))
y = int(input("Please give the Y coordinate you want to place: "))
z = int(input("Please give the Z coordinate you want to place: "))
val = int(input("please input your value: "))
copied_dicto[(x,y,z)] = val
b = control()
if b == True:
        print("Yay! This number is placable here!")
else:
        print("Sorry! This value can't be placed here.")
