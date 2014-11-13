'''
This python script simulate John Corway's Game of Life

This script is served as a guideline for your to finish your game of life program.
Feel free to change or edit on this program.

Task1: In your Game of Life configuraiton, you should have a gun, a glider and a few oscillators
Task2: Try your best to find a way to animate your results. 

@ytang, Nov 2014
'''

import numpy as np
import scipy.ndimage
import time

class Life(object):
    '''
    a class contains all varialbes and methods that you need to simulate the Game of life
    '''    
    #initialization of the class
    def __init__(self, nx, ny):
        #n: number of row and columns on our working grid
        #grid: the nx x ny grid we are working on
        self.nx = nx
        self.ny = ny
        self.grid = np.zeros((nx,ny), int)
        self.neighbor = np.array([[1,1,1],[1,10,1],[1,1,1]])
        
    def Add_pattern(self, x=0, y=0):      
        """TASK1: Add a Gun and Oscillators to your configuration as well"""
        
        '''provides initial patterns of living cells on the grid. 
        By default, the pattern starts from (0,0) position'''
        #pattern of a glider
        glider = [(0,1), (1,2), (2,0), (2,1), (2,2)]  #list of tuples 
        for i, j in glider:
            self.grid[x+i, y+j] = 1
        self.newarr=self.grid
            
    def Update(self, array):
        #with "Wrap", it considers the peoriodic condition
        arr = scipy.ndimage.filters.convolve(array, self.neighbor,mode="wrap")
        #alive if three are living neighbors for the dead cell or 2 or 3 living neighbors for the living cell
        boolarr = ((arr==3) | (arr==12) | (arr==13))  
        self.newarr = 1*boolarr #convert boolean matrix to the integer matrix
        return self.newarr
    
def animate():
    for i in range(10):
        print  ''
        global arr
        print arr
        arr=game.Update(arr)
        time.sleep(1) 
        
nx, ny = raw_input("please input the size of the grids (nx, ny)").split(',')
nx = int(nx)
ny = int(ny)
game=Life(nx, ny) # create an instance of Life
game.Add_pattern()
arr = game.newarr

animate() 
'''Task 2, Find a way to use matplotlib (or other packages) to animate results '''