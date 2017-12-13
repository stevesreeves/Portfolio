'''agentframework module'''

#agent framework.py is a module containing the classes and variables defining
# how the agents of the model behave.
#agentframework.py is imported into, and referred to by, the agent based model


#import random, library to generate random number
import random

#Defining Agent class and class behaviour.
#Generating random integers between 0 and 99,
# to represent coordinates on a 100x100 grid.
class Agent():
    def __init__ (self, environment, agents, x = None, y = None):
        if (x == None):
            self.x=random.randint(0,99)
        else:
            self.x=x
            
        if (y == None):
            self.y=random.randint(0,99)
        else:
            self.y=y
# "== None" etc allows for X and Y value to be absent, 
#substitutes in a random integer, eliminating error
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def move (self):
    
        if random.random() >0.5:
            self.x = (self.x+1) % 100
        else:
            self.x = (self.x-1) %100
    
        if random.random() <0.5:
            self.y = (self.y - 1) % 100
        else:
            self.y = (self.y - 1) %100
    
    def eat(self):
        if self.environment[self.y] [self.x]>10:
            self.environment [self.y][self.x]-=10
            self.store+=10
            
#adding sharing function to set up inter-agent communication within environment
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
                print("sharing" + str (dist) + " " + str (ave))
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y)**2))**0.5
    
    




       