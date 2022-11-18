from tkinter import *
from settings import *
import keyboard as kb
from threading import Thread
from time import sleep
import tkintermapview
from math import sin, cos, sqrt, atan2

class GUI_app():
    def __init__(self, window_title, width, height):
        self.win = Tk()
        self.win.title("कता खाने प्रकाश सर ?")
        x, y = self.center(width, height)
        
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        #self.win.overrideredirect(True)
        self.win.wm_attributes("-topmost", 1)
        #self.win.wm_attributes("-alpha", 0.99)
        self.win.configure(background=BG)
        self.no = 2

        self.number_label = Label(self.win, text="enter no of people", font=('Helvetica',14), bg=BG, fg=FG)
        self.number_label.place(x=300, y =700)

        self.e1 = Entry(self.win)
        self.e1.place(x=500, y =700)

        self.title_label = Label(self.win, text="CHOOSE YOUR POSITION", font=('Helvetica',18), bg=BG, fg=FG_button)
        self.title_label.pack()

        self.submit_btn = Button(self.win, text="Submit", font=('Arial',14), bg=BG_button, fg=FG_button,command=self.result)
        self.submit_btn.place(x=850, y =700)

        self.map_widget = tkintermapview.TkinterMapView(width = 800, height = 600, corner_radius=0 )
        self.map_widget.set_position(27.618,85.538)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        self.new_marker = self.map_widget.set_marker(27.61845630485157, 85.53684128570558, text="your position") 
        
        def left_click_event(coordinates_tuple):
            print("Left click event with coordinates:", coordinates_tuple)
            try:
                self.new_marker.delete()
            except:
                pass
            self.new_marker = self.map_widget.set_marker(coordinates_tuple[0], coordinates_tuple[1], text="your position")
            

        self.map_widget.add_left_click_map_command(left_click_event)

        #self.map_widget.add_left_click_map_command(label ="Add marker",command = lambda current_position: coords ,pass_coords = True)
        self.map_widget.pack()
        
        self.exit_btn = Button(self.win, text="Exit", font=('Arial',14), bg=BG_button, fg=FG_button, command=self.win.destroy)
        self.exit_btn.place(x=70, y=700)
            
    

    def start_menu(self):
        self.title_label = Label(self.win, text="CHOOSE YOUR POSITION", font=('Helvetica',18), bg=BG, fg=FG)
        self.title_label.pack()

        self.submit_btn = Button(self.win, text="Submit", font=('Arial',14), bg=BG_button, fg=FG_button,command= self.destroy())
        self.submit_btn.place(x=850, y =700)

        self.map_widget = tkintermapview.TkinterMapView(width = 800, height = 600, corner_radius=0 )
        self.map_widget.set_position(27.618,85.538)

        def left_click_event(coordinates_tuple):
            print("Left click event with coordinates:", coordinates_tuple)
            new_marker = self.self.map_widget.set_marker(coordinates_tuple[0], coordinates_tuple[1], text="your position")
    
        self.map_widget.add_left_click_map_command(left_click_event)
        self.map_widget.pack()

        self.exit_btn = Button(self.win, text="Exit", font=('Arial',14), bg=BG_button, fg=FG_button, command=self.win.destroy)
        self.exit_btn.place(x=70, y=700)
        

    def clear_screen(self):
        self.no = int(self.e1.get())
        for widget in self.win.winfo_children():
            widget.destroy()
            print(948) 
        

        
    def result2(self):
        self.clear_screen()
        print("this was also run")

        self.title_label = Label(self.win, text="OUR SUGGESTIONS", font=('Helvetica',24), bg=BG, fg=FG)
        self.title_label.pack()

        self.title_label = Label(self.win, text="aru baki chha", font=('Helvetica',24), bg=BG, fg=FG)
        self.title_label.pack()



    def result(self):
        self.clear_screen()
        print("this was also run")

        
        self.title_label = Label(self.win, text="OUR SUGGESTIONS", font=('Helvetica',24), bg=BG, fg=FG)
        self.title_label.pack()

        self.title_label = Label(self.win, text="aru baki chha", font=('Helvetica',24), bg=BG, fg=FG)
        self.title_label.pack()

        

        

    def center(self, width, height):
        swidth = self.win.winfo_screenwidth()
        sheight = self.win.winfo_screenheight()
        x = (swidth/2) - (width/2)
        y = (sheight/2) - (height/2)
        return int(x), int(y)

    def submit(self):
        pass

    def distance(self,lat1,lon1,lat2,lon2):
                
        R = 6373.0
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return distance

    

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