from struct import pack
from tkinter import *

def estonia_flag():
   
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 300, 67, fill="#007DFF")
    canvas.create_rectangle(0, 67, 300, 133, fill="#000000")
    canvas.create_rectangle(0, 133, 300, 200,fill="#FFFFFF")

def finland_flag():

    canvas.delete("all")
    canvas.create_rectangle(0, 0, 300, 200, fill="white") 
    canvas.create_rectangle(130, 0, 100, 200, fill="#122FAA")  # Узкая вертикальная полоса
    canvas.create_rectangle(0, 109, 300, 80, fill="#122FAA")  

def chess_board():
    canvas.delete("all")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "#FFFFFF"
            else:
                color = "#000000" 
            canvas.create_rectangle(j*25, i*25, (j+1)*25, (i+1)*25, fill=color)

def gradient_circle():
    canvas.delete("all")
    radius = 150
    c_x, c_y = 200, 200
    colors = ["#FF0000", "#FF8000", "#FFFF00", "#80FF00", "#00FF80", "#00FFFF", "#0080FF", "#0000FF", "#8000FF", "#FF00FF", "#FF0080"]
    step = 360 / len(colors)
    for i, color in enumerate(colors):
        start_angle = i * step
        end_angle = (i + 1) * step
        canvas.create_arc(c_x - radius, c_y - radius, c_x + radius, c_y + radius, start=start_angle, extent=step, fill=color)

def ring():
    canvas.delete("all")
    colors = ["#FF0000", "#FF8000", "#FFFF00", "#80FF00", "#00FF80", "#00FFFF", "#0080FF", "#0000FF", "#8000FF", "#FF00FF"]
    c_x, c_y = 200, 200
    outer_radius = 150
    num_ring = 10
    step_radius = outer_radius / num_ring
    for i in range(num_ring):
        color = colors[i % len(colors)]
        radius = outer_radius - step_radius * i
        canvas.create_oval(c_x - radius, c_y - radius, c_x + radius, c_y + radius, fill=color, outline="")


def CGKDM():
    canvas.delete("all")
    x, y, size = 100, 100, 200

    spacing = size / 4
    base_width = size /5

    canvas.create_rectangle(x - base_width / 2, y, x + base_width / 2, y + size * 1.5, fill="black")

    red_radius = size / 10
    canvas.create_oval(x - red_radius, y - red_radius, x + red_radius, y + red_radius, fill="red")

    yellow_radius = size / 10
    canvas.create_oval(x - yellow_radius, y + spacing - yellow_radius, x + yellow_radius, y + spacing + yellow_radius, fill="yellow")

    green_radius = size / 10
    canvas.create_oval(x - green_radius, y + 2 * spacing - green_radius, x + green_radius, y + 2 * spacing + green_radius, fill="green")      

    canvas.create_text(x, y - size / 5 - 1, text="Valgusfoor", font=("Arial", 20), fill="black")
    
def ffsfd():
    canvas.delete("all")
    x0=0 
    y0=0
    x1=600
    y1=600
    p=0
    x_=600
    y_=600
    for i in range(20):
        x0+=p  
        y0+=p 
        x1-=p 
        y1-=p 
        canvas.create_rectangle(x0,y0,x1,y1, fill="#be2344")
        canvas.create_oval(x0,y0,x1,y1, fill="#ffdbe3")
        x_-=2*p 
        y_-=2*p 
        p=int(((x_**2+y_**2)**(1/2)-x_)/2) 
        p=int(((p**2)/2)**(1/2))


def Bahamas_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 120, 300, 160, fill="#0d646d", outline="")
    canvas.create_rectangle(0, 160, 300, 200, fill="Yellow", outline="")
    canvas.create_rectangle(0, 200, 300, 240, fill="#0d646d", outline="")
    canvas.create_polygon([0,120],[0,240],[100,180],fill="black", outline="") 



   

root = Tk()


canvas = Canvas(root, width=600, height=600)
canvas.pack()




btn_estonia = Button(root, text="Estonia", command=estonia_flag)
btn_estonia.pack(side=LEFT)
btn_finland = Button(root, text="Soome", command=finland_flag)
btn_finland.pack(side=LEFT)

btn_chess_board = Button(root, text="Malelaud", command=chess_board)
btn_chess_board.pack(side=LEFT)

radiobutton = Button(root, text="gradiendi ring", command=gradient_circle)
radiobutton.pack(side=LEFT)

radiobutton2 =Button(root, text="Ring", command=ring)
radiobutton2.pack(side=LEFT)

radiobutton3 = Button(root, text="Valgusfoor", command=CGKDM)
radiobutton3.pack(side=LEFT)

radiobutton4 = Button(root, text="Värviline ruut", command=ffsfd)
radiobutton4.pack(side=LEFT)

radiobutton5 = Button(root, text="Bahama", command= Bahamas_flag)
radiobutton5.pack(side=LEFT)


root.mainloop()