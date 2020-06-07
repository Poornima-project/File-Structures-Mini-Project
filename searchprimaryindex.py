import csv 
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 

def search():
                        key = int(input("Enter id to search : " ))
                        #return key                  
                        #key = search()
                        search_d = data.loc[int(key)]
                        print(search_d)
                        end=time.time()
                        print('time taken to search the file in ms')
                        print(round(end, 2))
                        # x axis values 
                        x = [0,10000,20000,30000,40000,50000] 
                        # corresponding y axis values 
                        y = [0,5000,10000,15000,20000,25000] 
           
             
                        # plotting the points  
                        plt.plot(x, y) 

  
                        # naming the x axis 
                        plt.xlabel('no of records') 
                          # naming the y axis 
                        plt.ylabel('time taken in msec') 
  
                        # giving a title to my graph 
                        plt.title('search using primary key') 
  
                        # function to show the plot 
                        plt.show() 
start=time.time()
data = pd.read_csv("C:\\Users\\poornima\\Desktop\\movies.csv")
with open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r") as csvfile:

#print('successful read')
 choice=int(input('Enter the Choice 1.search by primarykey :\n'))

 if ( choice==1 ):
     search()
     
