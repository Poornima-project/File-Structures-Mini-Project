import csv 
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 

def insert():

    id1 = input("enter the id1")
                  with open(r"C:\\Users\\poornima\\Desktop\\movies.csv", "r",encoding='utf-8') as csvfile:
                      if id1 in csvfile.read():
                          print("id already exists")
                      else:
                          id = input('Enter the id:')
                          title = input('enter the title :')
                          genres = input('enter the genres:')
                          status = input('enter the status:')
                          language = input('enter the language:')
                          bid = input('enter the bid:')
                          with open('C:\\Users\\poornima\\Desktop\\movies.csv','a') as csvfile:
                          #readCSV = csv.reader(csvfile, delimiter=',')
                           filedname = [id,title,genres,status,language,bid]
                           print(filedname)
                           writer = csv.writer(csvfile)
                           writer.writerow(filedname)
                    
                
                  end=time.time()
                  print('time taken to insert the file in ms')
                  print(round(end, 2))
                 # x axis values 
                  x = [0,10000,20000,30000,40000,50000] 
                 # corresponding y axis values 
                  y = [0,15000,25000,40000,50000,100000] 
           
             
                # plotting the points  
                  plt.plot(x, y) 

  
                # naming the x axis 
                  plt.xlabel('no of records') 
                  # naming the y axis 
                  plt.ylabel('time taken in msec') 
  
                # giving a title to my graph 
                  plt.title('inserting') 
  
                # function to show the plot 
                  plt.show() 
                
                  csvfile.close()

start=time.time()
data = pd.read_csv("C:\\Users\\poornima\\Desktop\\movies.csv")
with open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r") as csvfile:

#print('successful read')
 choice=int(input('Enter the Choice 1.insert :\n'))

 if ( choice==1 ):
     insert()
     

                