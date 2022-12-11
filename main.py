import numpy as np

x1 = [0,1,2]
x2 = [3,4,5]
x3 = [6,7,8]

y1 = [0,1,2]
y2 = [3,4,5]
y3 = [6,7,8]

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def possible(x,y,n) :
    global grid
    for i in range(9):
        if grid[x][i] == n :
            return False
        
    for i in range(9):
        if grid[i][y] == n :
            return False
    
    if x in x1 :
        if y in y1 :
            for l in x1:
                for m in y1:
                    if grid[l][m] == n :
                        return False
        if y in y2 :
            for l in x1:
                for m in y2:
                    if grid[l][m] == n :
                        return False  
        if y in y3 :
            for l in x1:
                for m in y3:
                    if grid[l][m] == n :
                        return False

    if x in x2 :
        if y in y1 :
            for l in x2:
                for m in y1:
                    if grid[l][m] == n :
                        return False
        if y in y2 :
            for l in x2:
                for m in y2:
                    if grid[l][m] == n :
                        return False                        
        if y in y3 :
            for l in x2:
                for m in y3:
                    if grid[l][m] == n :
                        return False
    
    if x in x3 :
        if y in y1 :
            for l in x3:
                for m in y1:
                    if grid[l][m] == n :
                        return False
        if y in y2 :
            for l in x3:
                for m in y2:
                    if grid[l][m] == n :
                        return False                       
        if y in y3 :
            for l in x3:
                for m in y3:
                    if grid[l][m] == n :
                        return False
    return True

def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0 :
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return grid
    print(np.matrix(grid))
            
if __name__ == "__main__" :
    solve()