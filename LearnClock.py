from tkinter import Tk, Canvas, Text, END
import math
import random

master = Tk()
master.title ("What's the time now?")
w = Canvas (master, width = 600, height = 600)
w.pack ()
text = Text(master, height= 1, width=6)

hours = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12' ]
minutes = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55' ]

def draw_indications(hour, minute):
    for i in range (0,360,30):
        dx = 300; dy = 300; r = 200
        rad_fi = i * 3.14 / 180
        x = int (r * math.sin (rad_fi)) + dx
        y = int (r * math.cos (rad_fi)) + dy
        w.create_line (x, y, x + 10, y, fill = 'green', width = 4)
    # dx = 150; dy = 150
    hint_hour = 140
    pin_minute_length = 160
    cat_hour = 0.5 * 3.14 / 180 * (60 * hour + minute)
    cat_minute = minute * 3.14 * 6/180
    x_hour = int (hint_hour * math.sin (3.14-cat_hour)) + dx
    y_hour = int (hint_hour * math.cos (3.14-cat_hour)) + dy
    x_minute = int (pin_minute_length * math.sin (3.14-cat_minute)) + dx
    y_minute = int (pin_minute_length * math.cos (3.14-cat_minute)) + dy
    w.create_line (300,300, x_hour, y_hour, fill = 'red', width = 10)
    w.create_line (300,300, x_minute, y_minute, fill = 'blue', width = 4)    
    w.after(4000, lambda: showAns())
    #generate()

def showAns():
    text.tag_configure("center", justify = 'center')
    text.insert("1.0", "{}:{}".format(hour, minute), "center")
    text.config(font=("courier", 88))
    text.pack()
    w.after(2000, lambda: delAns())

def delAns():
    text.delete(1.0, END)
    #text.destroy()
    w.delete('all')
    generate()
    

def generate():
    global hour, minute
    hour = random.choice(hours)
    minute = random.choice(minutes)
    draw_indications(int (hour), int (minute))


generate()
