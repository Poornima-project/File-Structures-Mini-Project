#-*- coding: utf-8 -*-
import csv 
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 

start=time.time()
data = pd.read_csv("C:\\Users\\poornima\\Desktop\\movies.csv")
with open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r") as csvfile:
  print('WELCOME TO MOVIES DATABASE')
  
  while(True):
        choice=int(input('enter the choice 1.primary index 2.Insert 3.Search by primary key 4. Delete 5. sort  6.secondaryindex 7.search by secondary key 8.Delete using secondarykey 9.quit /n'))
        print(choice)
        if (choice==1):
           Offset_address=[]
           Primary_key=[]
           csv_columns=["id", "Primary"]
           fi=open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r",encoding='utf-8')
           pos=fi.tell()
           line=fi.readline()
           while line:
               pos=fi.tell()
               line=fi.readline()
               a=line.split(",")
               print(pos,",",a[0])
               Offset_address.append(pos)
               Primary_key.append(a[0])
           list= [Offset_address, Primary_key]
           export_data = zip_longest(*list, fillvalue = '')
           with open('C:\\Users\\poornima\\Desktop\\lil.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("Primary_key", "id"))
                wr.writerows(export_data)
           end=time.time()
           print('time taken to index using primary key the file in ms')
           print(round(end, 2))
            # x axis values 
           x = [10000,20000,30000,40000,50000] 
           # corresponding y axis values 
           y = [1000,1020,1040,1520,1540] 
           
             
            # plotting the points  
           plt.plot(x, y) 

  
           # naming the x axis 
           plt.xlabel('no of records') 
               # naming the y axis 
           plt.ylabel('time taken in msec') 
  
             # giving a title to my graph 
           plt.title('index using primary key') 
  
             # function to show the plot 
           plt.show() 
           
           myfile.close()
           
           
           
           
       
         
        elif(choice==2):
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
                
                
                
       
        elif(choice==3):
            #def search():
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
        
        elif(choice==4):
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
                
        elif(choice==5):
             a=pd.read_csv("C:\\Users\\poornima\\Desktop\\movies.csv",index_col=0)
             b=a.sort_values(["id"], axis=0,ascending=True)
             b.to_csv("C:\\Users\\poornima\\Desktop\\index1.csv")
             print(b)
             print("success")
             end=time.time()
             print('time taken to sort the file in ms')
             print(round(end, 2))
        
        elif(choice==6):
            Offset_address=[]
            Primary_key=[]
            csv_columns=["secondary_index", "bid"]
            fi=open(r"C:\\Users\\poornima\\Desktop\\movies.csv","r",encoding='utf-8')
            pos=fi.tell()
            line=fi.readline()
            while line:
              pos=fi.tell()
              line=fi.readline()
              a=line.split(",")
              print(pos,",",a[-1])
              Offset_address.append(pos)
              Primary_key.append(a[-1])
            list= [Offset_address, Primary_key]
            print(list)
            export_data = zip_longest(*list, fillvalue = '')
            with open('C:\\Users\\poornima\\Desktop\\index.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
                 wr = csv.writer(myfile)
                 wr.writerow(("bid", "secondary_index"))
                 wr.writerows(export_data)
                 end=time.time()
                 print('time taken to index the file in ms')
                 print(round(end, 2))
                 # x axis values 
                 x = [10000,20000,30000,40000,50000] 
           # corresponding y axis values 
                 y = [1000,1420,1460,1520,1540] 
           
             
            # plotting the points  
                 plt.plot(x, y) 

  
           # naming the x axis 
                 plt.xlabel('no of records') 
               # naming the y axis 
                 plt.ylabel('time taken in msec') 
  
             # giving a title to my graph 
                 plt.title('index using secondary key') 
  
             # function to show the plot 
                 plt.show() 
            myfile.close()
        
        elif(choice==7):
            
            key = int(input("Enter bid to search : " ))
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
            y = [0,1000,9000,11000,17000,23000] 
           
             
            # plotting the points  
            plt.plot(x, y) 

  
           # naming the x axis 
            plt.xlabel('no of records') 
            # naming the y axis 
            plt.ylabel('time taken in msec') 
  
            # giving a title to my graph 
            plt.title('search using secondary key') 
  
            # function to show the plot 
            plt.show() 
        
        elif(choice==8):
            bid = int(input('Enter the bid to delete: \n'))
            search_d = data.loc[int(bid)]
            #data.loc[int(del_id) - 1] = 0
            print( data.loc[int(bid-1)])
            data.loc[int(bid)] = 0
            end=time.time()
            print('time taken to delete the file in ms')
            print(round(end, 2))
            # x axis values 
            x = [0,10000,20000,30000,40000,50000] 
            # corresponding y axis values 
            y = [0,5000,6000,7000,10000,15000] 
           
             
            # plotting the points  
            plt.plot(x, y) 

  
           # naming the x axis 
            plt.xlabel('no of records') 
             # naming the y axis 
            plt.ylabel('time taken in msec') 
  
             # giving a title to my graph 
            plt.title('deletion using secondary key') 
  
            # function to show the plot 
            plt.show()
        
        elif(choice==9):
            sys.exit('exiting')
          
            
csvfile.close()



