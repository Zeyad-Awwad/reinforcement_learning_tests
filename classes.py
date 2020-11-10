
class Bandit:
    
    def __init__(self, env, policy, update, initializer, kwargs):
        self.N_arms = env.action_space.n
        self.env = env
        self.policy = policy
        self.update = update
        initializer(self, kwargs)
        
    
    def action(self, verbose = False):
        arm = self.policy(self)
        observation, reward, done, info = self.env.step(arm)
        if verbose:
            print( arm, "\t", reward, "\t", observation, "\t" ) #[ int(100*o) for o in observation ], "\t", 
        self.update(self, arm, reward, observation)
        return done, reward


class ActionSpace:
    
    def __init__(self, N_actions):
        self.n = N_actions

        

class Environment:
    
    def __init__(self, N_actions, step_function, initializer, reset_function, kwargs):
        self.action_space = ActionSpace(N_actions)
        self.step = lambda x: step_function(self, x)
        initializer(self, kwargs)
        self.reset = lambda: reset_function(self)
    
    def reset(self):
        return self.state
    
    def close(self):
        return