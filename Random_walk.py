#%%
import random
#%%
def random_walk(n):
    x,y = 0,0
    for i in range(n):
        dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)
#%%
for i in range(25):
    walk = random_walk(10)
    print(walk, "distance from starting point = ", abs(walk[0]) + abs(walk[1]))
# %%
number_of_walks = 10000
for walk_length in range(1,31):
    no_of_transport = 0     # No. of walks with 4 or fewer blocks from the starting point
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_of_transport += 1
    no_of_transport_percentage = float (no_of_transport)/number_of_walks
    if 100*no_of_transport_percentage > 50:
        # a.append((walk_length,100*no_of_transport_percentage))
        print("Walk size = ", walk_length, " / % of no transport = ", 100*no_of_transport_percentage)

# %%
