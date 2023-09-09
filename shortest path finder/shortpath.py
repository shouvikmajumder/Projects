import curses
from curses import wrapper 
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", " ", "#",],
    ["#", "O", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#",]
] 




def findpath(maze,stdscr):
    start = 'O'
    end = "X"
    startpos = findcoordinates(maze,start)

    q = queue.Queue()
    q.put((startpos,[startpos]))
    visited = set()    

    while not q.empty():     
        currentpos, path = q.get()
        row, col = currentpos

        stdscr.clear()
        viewmaze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()
        

        if maze[row][col] == end: 
            return path

        neighbors = findneighbors(maze,row,col)

        for neigh in neighbors:
            if neigh in visited:
                continue
            r, c = neigh
            if maze[r][c] == "#":
                continue
            newpath = path + [neigh]
            q.put((neigh, newpath))
            visited.add(neigh)
    

def findneighbors(maze, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # this goes up

    if row + 1 < len(maze): 
        neighbors.append((row + 1, col))  # this goes down

    if col > 0:  # Left
        neighbors.append((row, col - 1))

    if col + 1 < len(maze[0]): 
        neighbors.append((row, col + 1))

    return neighbors  # Fix: Return the 'neighbors' list






def findcoordinates(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i , j
    return None



def viewmaze(maze,stdscr,path=[]):
    bloo = curses.color_pair(1)
    red = curses.color_pair(2) #path

    for i, row in enumerate(maze): # in enumerate i is the value of the list that the iteration is on 
        for j, val in enumerate(row):
            if (i,j) in path: 
                stdscr.addstr(i,j*2, "X", red)  
            else:
                stdscr.addstr(i,j*2, val, bloo)  
         

             


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    findpath(maze, stdscr)
    stdscr.getch()


curses.wrapper(main)


