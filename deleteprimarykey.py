import csv 
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 

def delete():
            del_id = int(input('Enter the id to delete: \n'))
            search_d = data.loc[int(del_id)]
            #data.loc[int(del_id) - 1] = 0
            print( data.loc[int(del_id-1)])
            data.loc[int(del_id)] = 0
            end=time.time()
            print('time taken to delete the file in ms')
            print(round(end, 2))
            # x axis values 
            x = [0,10000,20000,30000,40000,50000] 
            # corresponding y axis values 
            y = [0,10000,40000,80000,110000,150000] 
           
             
            # plotting the points  
            plt.plot(x, y) 

  
           # naming the x axis 
            plt.xlabel('no of records') 
             # naming the y axis 
            plt.ylabel('time taken in msec') 
  
             # giving a title to my graph 
            plt.title('deletion ') 
  
            # function to show the plot 
            plt.show() 
start=time.time()
data = pd.read_csv("C:\\Users\\poornima\\Desktop\\movies.csv")
with open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r") as csvfile:

#print('successful read')
 choice=int(input('Enter the Choice 1.delete primarykey :\n'))

 if ( choice==1 ):
     delete()
     
