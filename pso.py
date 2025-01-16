#code for particle swarm optimization (PSO)
#import libraries
import random
import numpy as np
import matplotlib.pyplot as plt
from swarmfun import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Particle
class Particle:

    #initialization
    def __init__(self,POP,option,XMIN,YMIN,XMAX,YMAX):


        self.pos=[None]*POP                    # particle position
        self.vel=[np.array([0,0])]*POP         # particle velocity
        self.pos_best=[None]*POP               # best position individual
        self.pos_cost=[None]*POP               # cost
        self.pos_best_cost=[None]*POP          #cost for the best position

        self.xvalues=[]                        #xvalues
        self.yvalues=[]                        #yvalues
        self.colours = []

        
        for i in range(POP):
        
            randX = random.randint(XMIN,XMAX)
            randY = random.randint(YMIN,YMAX)       
            self.pos[i]=np.array([randX,randY],dtype=float)            # particle position
            self.pos_best[i]=self.pos[i]                              # best position individual
            self.evaluate(option,i)
            self.pos_best_cost[i]=self.pos_cost[i]

            self.xvalues.append(self.pos[i][0])
            self.yvalues.append(self.pos[i][1])

            self.colours.append(random.randint(0,2))

    #velocity updating    
    def update_velocity(self,i,global_best_pos):

        w=1
        c1=1.2
        c2=1.2

        r1=np.random.rand()
        r2=np.random.rand()
        self.vel[i]=self.vel[i]+w*(c1*r1*(self.pos_best[i]-self.pos[i]) + c2*r2*(global_best_pos-self.pos[i]))

    #position updating
    def update_position(self,i):

        self.pos[i]+=self.vel[i]

    #evaluating a particles
    def evaluate(self,option,i):
        if option==0:          
           self.pos_cost[i]=Ackley(self.pos[i])
           
        if option==1:          
           self.pos_cost[i]=Booth(self.pos[i])
           
        if option==2:          
           self.pos_cost[i]=Matyas(self.pos[i])

        if option==3:          
           self.pos_cost[i]=Himmelblau(self.pos[i])
           
        if option==4:          
           self.pos_cost[i]=Beale(self.pos[i])
           
    #runinig simulation       
    def run_simulation(self,maxiter,POP,option,XMIN,YMIN,XMAX,YMAX,root):

        it=0
        global_best_pos=np.array([0,0])
        global_best_cost=np.inf

        ax=root.figure.add_subplot(111)

        ax.scatter(self.xvalues,self.yvalues,c=self.colours)
        ax.set_xlim([XMIN-10,XMAX+10])  
        ax.set_ylim([YMIN-10,YMAX+10])

        
        root.fig1.draw()
        
        
        
        while it<maxiter:

            
            for i in range(POP):

                self.update_velocity(i,global_best_pos)
                self.update_position(i)           

                self.evaluate(option,i)
                
                if self.pos_cost[i] < self.pos_best_cost[i]:
                     self.pos_best_cost[i]=self.pos_cost[i]

                if self.pos_best_cost[i] < global_best_cost:
                         
                     global_best_cost=self.pos_best_cost[i]

                if  self.pos[i][0] < XMIN:
                     self.pos[i][0]=XMIN
                 
                if  self.pos[i][1] < YMIN:
                     self.pos[i][1]=YMIN

                if  self.pos[i][0] > XMAX:
                     self.pos[i][0]= XMAX  
                 
                if   self.pos[i][1] > YMAX:
                     self.pos[i][1]= YMAX
                 
                self.xvalues[i]=self.pos[i][0]
                self.yvalues[i]=self.pos[i][1]

                bha=ax.scatter(self.xvalues,self.yvalues, c=self.colours)
                root.fig1.draw()
                plt.pause(.05)

                bha.remove()
                
                ax.set_xlim([XMIN-10,XMAX+10])  
                ax.set_ylim([YMIN-10,YMAX+10])
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
            print('Best Cost at Iteration:',it+1,'=',global_best_cost)

            it+=1
          
        plt.show()

