import numpy as np

def init_cliffworld(env, kwargs):
    env.grid = np.zeros(kwargs['shape']) - 1
    idx = np.asarray(kwargs['cliff'])
    I, J = idx[:,0], idx[:,1]
    env.grid[J,I] = -100
    env.start = kwargs['start']
    env.end = kwargs['end']
    env.loc = kwargs['start']
    env.shape = kwargs['shape']

def cliffworld_edges(loc, arm):
    if arm == 0 and loc[0] == 0:
        return True
    if arm == 1 and loc[0] == env.shape[0]-1:
        return True
    if arm == 2 and loc[1] == 0:
        return True
    if arm == 3 and loc[1] == env.shape[1]-1:
        return True
    return False
    
def step_cliffworld(env, x):
    i, j = env.loc
    if cliffworld_edges(env.loc, x):
        return (i,j), env.grid[i,j], False, None
    if x < 2:
        i += 2*x - 1
    elif 2 <= x < 4:
        j += 2*(x-2) - 1
    else:
        print( "ERROR: Invalid arm", x)
        return None
    if (i,j) == env.end:
        env.loc = env.start
        return env.start, 0, True, None
    elif env.grid[i,j] < -1:
        return env.start, -100, True, None
    else:
        env.loc = (i,j)
        return (i,j), -1, False, None

def reset_cliffworld(env):
    env.loc = env.start
    return env.start