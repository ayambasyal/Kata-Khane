from tkinter import *
from settings import *
import keyboard as kb
from threading import Thread
from time import sleep
import tkintermapview
from math import sin, cos, sqrt, atan2
import pandas as pd
import numpy as np
from queue import Queue
import random

class GUI_app():
    def __init__(self, window_title, width, height):
        self.win = Tk()
        self.win.title("कता खाने?")
        x, y = self.center(width, height)
        
        self.storeeh = pd.read_csv("distance.txt")
      
        #print(self.storeeh.to_string())\
        #for index, row in self.storeeh.iterrows():
        #    print(row['Latitude'], row['Longitude'],row['Name'])
            
            
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        #self.win.overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        #self.win.wm_attributes("-alpha", 0.99)
        self.win.configure(background=BG)
        self.no = 2
        self.objs=[]

        self.no_of_seats = int

        self.number_label = Label(self.win, text="Enter no of people: ", font=('ubuntu',14), bg=BG, fg=FG)
        self.number_label.place(x=300, y =696)

        self.e1 = Entry(self.win, font=('ubuntu',14))
        self.e1.place(x=500, y =700)

        self.title_label = Label(self.win, text="CHOOSE YOUR POSITION", font=('ubuntu',18), bg=BG, fg=FG_button)
        self.title_label.pack()

        self.submit_btn = Button(self.win, text="Submit", font=('Arial',14), bg=BG_button, fg=FG_button,command =lambda:[bubbleSort(objs),self.result()])
        self.submit_btn.place(x=850, y =700)

        self.map_widget = tkintermapview.TkinterMapView(width = 800, height = 600, corner_radius=0 )
        self.map_widget.set_position(27.618,85.538)
        #self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        self.new_marker = self.map_widget.set_marker(27.61845630485157, 85.53684128570558, text="your position") 
        
        self.b1 = Button
        self.b2 = Button
        self.b3 = Button
        self.b4 = Button
        self.b5 = Button
        self.b6 = Button
        self.b7 = Button
        self.b8 = Button
        self.b9 = Button
        self.b10 = Button
        self.b11 = Button
        self.b12 = Button


        self.c1 = Label(self.win)
        self.what_your_position_x = 27.62233076617784
        self.what_your_position_y =85.53681951827144
        def left_click_event(coordinates_tuple):
            print("Left click event with coordinates:", coordinates_tuple)
            try:
                self.new_marker.delete()
            except:
                pass
            #store = open("distance.txt","a")
            #store.write(str(coordinates_tuple)+"\n")
            #store.close()

            print(str(coordinates_tuple))
            self.what_your_position_x = coordinates_tuple[0]
            self.what_your_position_y = coordinates_tuple[1]
            self.new_marker = self.map_widget.set_marker(coordinates_tuple[0], coordinates_tuple[1], text="your position")


        self.map_widget.add_left_click_map_command(left_click_event)

        #self.map_widget.add_left_click_map_command(label ="Add marker",command = lambda current_position: coords ,pass_coords = True)
        self.map_widget.pack()
        
        self.exit_btn = Button(self.win, text="Exit", font=('Arial',14), bg=BG_button, fg=FG_button, command=self.win.destroy)
        self.exit_btn.place(x=70, y=700)
        
        class aarrey():
            def __init__(self, name, distance):
                self.size= 20
                self.name = name
                self.distance = distance
                self.seat = Queue(maxsize=20)
            
                for i in range(random.randrange(5,17)):
                    bad_num = random.randrange(1000,9999)
                    print(bad_num)
                    self.seat.put(bad_num)
                
                self.disp_queue()
                
            def disp_queue(self):
                print(self.seat.qsize())
                return self.seat.qsize()

        
        def bubbleSort(objs):
            objs = []

            for index, row in self.storeeh.iterrows():
                print(len(objs))
                objs.append(aarrey(row['Name'],self.distance(float(row['Latitude']),float(row['Longitude']),self.what_your_position_x,self.what_your_position_y))) 
            n = len(objs)
            print(n)
            print(n)
            # optimize code, so if the array is already sorted, it doesn't need
            # to go through the entire process
            swapped = False
            # Traverse through all array elements
            for i in range(n):
                # range(n) also work but outer loop will
                # repeat one time more than needed.
                # Last i elements are already in place
                for j in range(0, n-i-1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if objs[j].distance > objs[j+1].distance:
                        swapped = True
                        objs[j], objs[j+1] = objs[j+1], objs[j]
                
                if not swapped:
                    # if we haven't needed to make a single swap, we
                    # can just exit the main loop.
                    return
            self.objs= []
            self.objs.extend(objs)
            for i in range(len(objs)):
                print(objs[i].name,objs[i].distance)
                pass
        
        #dummy = aarrey(15,"dummy",70)
        objs = []
       

        bubbleSort(objs)

    def book_func(self,name2):
        self.c1.destroy()
        self.c1 = Label(self.win,text = "You have booked "+str(self.no_of_seats)+" seats at "+name2, font=('ubuntu',18), bg=highlight, fg=FG_button )
        self.c1.place(x = 260,y = 600)

    def clear_screen(self):
        self.no = int(self.e1.get())
        for widget in self.win.winfo_children():
            widget.destroy()
            

    def result(self):
        self.no_of_seats = self.e1.get()
        self.clear_screen()
        self.title_label = Label(self.win, text="OUR SUGGESTIONS", font=('ubuntu',24), bg=BG, fg=FG)
        self.title_label.grid(columnspan=5)

      


        lst = [("Serial number","Place to eat","Occupied seats","Vacant seats","BOOK?")]
        
        for i in range(0,12):
            lst.append((i+1,self.objs[i].name,self.objs[i].disp_queue(),20-int(self.objs[i].disp_queue()),"book"))

        total_rows = len(lst)
        total_columns = len(lst[0])
        button_list = []

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if (j==4) and (i!=0):
                    print(i)
                    '''
                    l2 = Button(self.win,text =lst[i][j] , width=18, fg='blue',font=('Arial',13,'bold'),command=lambda:[self.book_func(self.objs[i-6].name)])
                    self.b1.grid(row=i+3, column=j,sticky= S)
                    button_list.append(l2)
                    '''
                    if (i == 1):
                        self.b1 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[0].name)])
                        self.b1.grid(row=i+3, column=j,sticky= S)
                    if (i == 2):
                        self.b2 = Button(self.win,text =lst[i][j] , width=18,font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[1].name)])
                        self.b2.grid(row=i+3, column=j,sticky= S)
                    if (i == 3):
                        self.b3 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[2].name)])
                        self.b3.grid(row=i+3, column=j,sticky= S)
                    if (i == 4):
                        self.b4 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[3].name)])
                        self.b4.grid(row=i+3, column=j,sticky= S)
                    if (i == 5):
                        self.b5 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[4].name)])
                        self.b5.grid(row=i+3, column=j,sticky= S)
                    if (i == 6):
                        self.b6 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[5].name)])
                        self.b6.grid(row=i+3, column=j,sticky= S)
                    if (i == 7):
                        self.b7 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[6].name)])
                        self.b7.grid(row=i+3, column=j,sticky= S)
                    if (i == 8):
                        self.b8 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[7].name)])
                        self.b8.grid(row=i+3, column=j,sticky= S)
                    if (i == 9):
                        self.b9 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[8].name)])
                        self.b9.grid(row=i+3, column=j,sticky= S)
                    if (i == 10):
                        self.b10 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[9].name)])
                        self.b10.grid(row=i+3, column=j,sticky= S)
                    if (i == 11):
                        self.b11 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[10].name)])
                        self.b11.grid(row=i+3, column=j,sticky= S)
                    if (i == 12):
                        self.b12 = Button(self.win,text =lst[i][j] , width=18, font=('ubuntu',11,'bold'),command=lambda:[self.book_func(self.objs[11].name)])
                        self.b12.grid(row=i+3, column=j,sticky= S)
                  


                else:
                    l1 = Label(self.win,text =lst[i][j] , width=18 ,font=('ubuntu',11,'bold'))
                    l1.grid(row=i+3, column=j,sticky= S)
                
                
        '''
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                l1 = Label(self.win,text =lst[i][j] , width=18, fg='blue',font=('Arial',11,'bold'))
                l1.grid(row=i+3, column=j,sticky= S)
        
        '''
        def refresh():

                
            
            print("*********************************************")
            print(self.objs)
            


    def center(self, width, height):
        swidth = self.win.winfo_screenwidth()
        sheight = self.win.winfo_screenheight()
        x = (swidth/2) - (width/2)
        y = (sheight/2) - (height/2)
        return int(x), int(y)



    def distance(self,lat1,lon1,lat2,lon2):
                
        R = 6373.0
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return distance

    def write(self):
        pass


    

class Node:
	# Function to initialise the node object
	def __init__(self, data, max_size,position,filled):
		self.data = data # Assign data
		self.max_size = max_size
		self.filled = filled 
		self.position = position
		self.next = None # Initialize next as null
        
# Linked List class contains a Node object
class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None


GUI_app = GUI_app("kata khane", 1000, 800)


GUI_app.win.mainloop()