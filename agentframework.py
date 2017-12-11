#a module - contains classes as well as its own variables
# needs to be imported and referred to by "import agentframework"
#usually single files to do a set of jobs
#modules are imported whilst scripts generally run directly
#packages are collections of modules, with a namespace (a unique way of referring to them)


#agentframework.py is imported into the model



import random

#class Agent ():
   #def __init__ (self):
    #    self._x = None
     #   self._y = None
   #     self.randomize()
  #      
    #def getx(self):
       # return self._x
        
    #def gety(self):
   #     return self._y
    
    #def setx(self, value):
   #     self._x = value
        
    #def sety(self, value):
 #       self._y = value
        
    #def delx(self):
 #       del self._x
    
   # def dely(self):
 #       del self._y
        
        
 #   x = property(getx, setx, delx, "I'm the 'x' property.")   
  #  y = property(gety, sety, dely, "I'm the 'y' property.")  
        
 #   def randomize (self):
 #       self._x = random.randint(0,99)
 #       self._y = random.randint(0,99)
        
        
        
 #   def move (self):
        
    #    if random.random() < 0.5:
  #          self._x = (self._x + 1) % 100
#        else:
  #         self._x = (self._x - 1) % 100

 #       if random.random() < 0.5:
  #          self._y = (self._y + 1) % 100
  #      else:
            #self._y = (self._y - 1) % 100
  


    

#define Agent class and class behaviour
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
   # "== None!" etc allows for X and Y value to be absent, substitutes in a random integer
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
            
    #adding sharing function to set up agent communication   
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
    
    




       