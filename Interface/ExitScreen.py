from tkinter import *
from PIL import ImageTk, Image 
import time

class ExitScreen:
    def __init__(self):
        w=Tk()

        width_of_window = 630
        height_of_window = 250
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        w.overrideredirect(1)

        Frame(w, width=620, height=250, bg='#212325').place(x=0,y=0)
        label1=Label(w, text='Spark Stack\nBrandon Tejaxún - 202112030', fg='white', bg='#212325')
        label1.configure(font=('Roboto Medium',24,"bold"))
        label1.place(x=80,y=60)

        image_a=ImageTk.PhotoImage(Image.open('Image/c2.png'))
        image_b=ImageTk.PhotoImage(Image.open('Image/c1.png'))

        for i in range(6,-1,-1):
            label2=Label(w, text=f'{i}', fg='white', bg='#212325')
            label2.configure(font=('Roboto Medium',16))
            label2.place(x=10,y=215)

            w.update_idletasks()
            time.sleep(0.2)

            w.update_idletasks()
            time.sleep(0.2)

            w.update_idletasks()
            time.sleep(0.2)

            w.update_idletasks()
            time.sleep(0.2)

        w.destroy()