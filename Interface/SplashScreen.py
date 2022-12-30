from tkinter import *
from PIL import ImageTk, Image 
import time

class SplashScreen:
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

        self.count = 5
        for i in range(5):
            l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=275, y=160)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=160)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=325, y=160)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=350, y=160)

            label2=Label(w, text=f'{self.count}', fg='white', bg='#212325')
            label2.configure(font=('Roboto Medium',16))
            label2.place(x=10,y=215)

            w.update_idletasks()
            time.sleep(0.2)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=275, y=160)
            l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=300, y=160)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=325, y=160)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=350, y=160)
            w.update_idletasks()
            time.sleep(0.2)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=275, y=160)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=160)
            l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=325, y=160)
            l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=350, y=160)
            w.update_idletasks()
            time.sleep(0.2)

            l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=275, y=160)
            l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=160)
            l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=325, y=160)
            l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=350, y=160)
            w.update_idletasks()
            time.sleep(0.2)

            self.count -= 1

        w.destroy()