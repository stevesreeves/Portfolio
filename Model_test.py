# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:18:44 2017

@author: gy17sms
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:27:03 2017

@author: gy17sms
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:27:23 2017

@author: gy17sms
"""

'''Agent Based Model'''


#web scraping X Y data
#request library allows for fetching of HTTP
import requests
#"beautiful soup" library facilitates screen-scraping from webpage and converts into UTF-8
import bs4


#stating webpage to scrape for data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys) #displaying coordinates
print(td_xs)



#importing other libraries used for model

#libraries for building GUI 
#tkinter is a object-oriented package for construcing GUIs
import tkinter
import matplotlib.backends.backend_tkagg
#import this matplotlib before any other import of matplotlib
#matplotlib plots onto a 2D frame
import matplotlib 

#importing library responsible for production of random integers:
import random

import matplotlib.pyplot

#importing animating library for model:
import matplotlib.animation 

#importing module agentframework.py file containing agents information and behaviour:
import agentframework  

#library for using .csv and .txt files:
import csv 

#timing running of model:
import datetime
def getTimeMS():
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

start = getTimeMS()

#declaring variables for model:
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#declare agent and environment arrays for model:
agents = []
environment = []

#defining size of model plot:
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)


#read in .txt file, using imported csv library
f = open('in.txt', newline='')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

#reader reads file one line at a time, inputting it into "rowlist" array
for row in reader: 
        rowlist = []
        for item in row:
            rowlist.append (float(item))
        environment.append(rowlist)
f.close()


#pythagoras equation, establishing distance between given agents
def distance_between(agent0, agent1):
   return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5
# ** = square root of the sum of the difference between the agents
   

# Making the agents:
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
     
#plotting agent based model output on graph on  a 100x100 grid, using matplotlib  library
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#matplotlib.pyplot.show() #replace with canvas show


###################
#animating the plot

#defining movement of model:
carry_on = True

def update(frame_number):
    
    fig.clear()   
    global carry_on
    matplotlib.pyplot.imshow(environment)
    
#Shuffling list of agents before each iteration, meaning there is no chance of 
#picking an identical agent again
    random.shuffle(agents) 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
     
          
#Constructing stopping function for animation. 
#If the random number produced is less than 0.1, stopping function is fulfilled.
#No further iterations of agent based model occur after stopping function.
#This reduces error by catching exceptions
    
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(str(agents[i].x) + ',' + str(agents[i].y))  
        #additional string added in order to include comma in printed coordinates


def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed
    while (a < 10) & (carry_on) :
        yield a			#Returns control and awaits next call by model
        a = a + 1
        
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()


#building model GUI window with menu
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu) #menu with drop-down option to run the model
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()



#end of timing process
end = getTimeMS()
#displaying runtime of model
print("time = " + str(end - start))