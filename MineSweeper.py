
# coding: utf-8

# In[101]:


import numpy as np


# In[102]:


def generate_mine(n):
    coord = []
    x_range = np.arange(5)
    y_range = np.arange(7)
    for _ in range(n):
        rand_y = np.random.randint(7)
        rand_x = np.random.randint(5)
        if not grid[rand_y,rand_x] == 9:
            coord.append((rand_y, rand_x))
            grid[rand_y,rand_x] = 9
            
    for y,x in coord:
        y_it = y-1
        x_it = x-1
        while y_it <= y+1:
            x_it = x-1
            while x_it <= x+1:
                if x_it in x_range and y_it in y_range:
                    if not grid[y_it,x_it] == 9:
                        grid[y_it,x_it]+=1
                x_it+=1
            y_it+=1
    print("mines placed")


# In[103]:


def show_grid(seen):
    show = ""
    for y in range(grid.shape[0]):
        show+="\n"
        for x in range(grid.shape[1]):
            if (y,x) in seen:
                show+=" " + str(seen[(y,x)]) + " "
            else:
                show+=" * "
    print(show)
            


# In[104]:


def sweep(coord,seen):
    revealed = [coord]
    x_range = np.arange(5)
    y_range = np.arange(7)
    if grid[coord[0],coord[1]] == 0:
        for y,x in revealed:

            #go up
            y_up = y-1
            if y_up in y_range:
                if grid[y_up,x] == 0 and (y_up,x) not in revealed:
                    revealed.append((y_up,x))

            #go down
            y_down = y+1
            if y_down in y_range:
                if grid[y_down,x] == 0 and (y_down,x) not in revealed:
                    revealed.append((y_down,x))

            #go left
            x_left = x-1
            if x_left in x_range:
                if grid[y,x_left] == 0 and (y,x_left) not in revealed:
                    revealed.append((y,x_left))

            #go right
            x_right = x+1
            if x_right in x_range:
                if grid[y,x_right] == 0 and (y,x_right) not in revealed:
                    revealed.append((y,x_right))
                    
                    
        for y,x in revealed:
            y_it = y-1
            x_it = x-1
            while y_it <= y+1:
                x_it = x-1
                while x_it <= x+1:
                    if x_it in x_range and y_it in y_range:
                        seen[y_it,x_it] = grid[y_it,x_it]
                    x_it+=1
                y_it+=1
            

    else:
        seen[coord] = grid[coord]
        


# In[122]:


def play():
    seen = {}
    generate_mine(2)
    while True:
        coord = input("y,x: ")
        if not (coord[0].isdigit() and coord[2].isdigit()):
            print("wrong input")
            continue
        y,x = int(coord[0]), int(coord[2])
        if not ((x < 5 and x > -1) and (y < 7 and y > -1)):
            print("out of range")
            continue
        
        sweep((y,x),seen)
        show_grid(seen)
        
        if grid[y,x] == 9:
            print("GAME OVER")
            break
        
            
        if (grid.shape[0]*grid.shape[1]) -len(seen) <= 2:
            print("WON")
            break


# In[123]:


grid = np.zeros((7,5),dtype=np.uint8)


# In[124]:


play()

