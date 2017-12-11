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
#web scraping X Y data
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



#import all libraries for model
import tkinter
import matplotlib.backends.backend_tkagg
import matplotlib #import this matlibplot before any other improt of matplotlib
#matplotlib.use('tkagg')


import random
#import operator
import matplotlib.pyplot
import matplotlib.animation #animating library
import agentframework
import csv

#timing running of model
import datetime
def getTimeMS():
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

start = getTimeMS()

#declaring variables for model
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#declare arrays:
agents = []
environment = []


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)



#read in .txt file, using csv library
f = open('in.txt', newline='')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)



for row in reader: #reader reads file one line at a time, inputting it into rowlist array
        rowlist = []
        for item in row:
            rowlist.append (float(item))
        environment.append(rowlist)
f.close()


#pythagoras
def distance_between(agent0, agent1):
   return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5
# ** = square root of the sum of the difference between the agents
   

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
     
#plotting model output on graph on  a 100x100 grid, using matplotlib  library
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#matplotlib.pyplot.show() #replace with canvas show


###################
#animating the plot

#define movement
carry_on = True

def update(frame_number):
    
    fig.clear()   
    global carry_on


    matplotlib.pyplot.imshow(environment)

    random.shuffle(agents) # shuffles list of agents befre each iteration - no chance of picking same agent again
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
     
          
    #constructing stopping fucntion for animation    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(str(agents[i].x) + ',' + str(agents[i].y))  #add string to include comma in coords


def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
tkinter.mainloop()



#end of timing process
end = getTimeMS()

print("time = " + str(end - start))