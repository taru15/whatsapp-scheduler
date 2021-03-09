import pywhatkit as kit
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
top = Tk()

top.title("WhatsApp Scheduler")
top.geometry("1350x700+0+0")
canvas=Canvas(top, width=1350, height=700)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\sacha\\OneDrive\\Desktop\\fone.png"))
canvas.create_image(0,0,anchor=NW, image=image)
canvas.pack()
img=ImageTk.PhotoImage(Image.open("C:\\Users\\sacha\\OneDrive\\Desktop\\1.jpg"))
canvas.create_image(570,40,anchor=NW, image=img)
var_no=StringVar()
var_mess=StringVar()
var_hr=IntVar()
var_min=IntVar()
phone_no=Label(top, text="Phone no.", font=("times of roman", 20, "bold")).place(x=510, y=240)
e1 = Entry(top, textvariable=var_no).place(x = 680, y = 250, width=150)
message=Label(top,text="Message", font=("times of roman", 20, "bold")).place(x=510, y=280)
e2 = Entry(top, textvariable=var_mess, font=("times of roman", 13, "bold")).place(x = 680, y = 290, height=70, width=150)  
hr=Label(top, text="Hour", font=("times of roman", 20, "bold")).place(x=510, y=360)
e3  =ttk.Combobox(top, textvariable=var_hr)
e3['values']=("00", "01", "02", "03","04","05", "06", "07","08","09", "10", "11","12","13","14","15","16","17","18","19","20","22","23")
e3.place(x = 680, y = 370)
m=Label(top, text="Minutes", font=("times of roman", 20, "bold")).place(x=510, y=400)
e4 = ttk.Combobox(top, textvariable=var_min)
e4['values']=("00", "01", "02", "03","04","05", "06", "07","08","09", "10", "11","12","13","14","15","16","17","18","19","20","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
e4.place(x = 680, y = 410)
def register_data():
    try:
        var="+91"+str(var_no.get())
        kit.sendwhatmsg(var,var_mess.get(), var_hr.get(), var_min.get())
        print('message send')
    except:
        print('fail')
b_image=ImageTk.PhotoImage(Image.open("C:\\Users\\sacha\\OneDrive\\Desktop\\images.png"))    
b=Button(top, image=b_image, bd=0 , cursor="hand2", command=register_data).place(x=570, y=440, width=150, height =80)
top.mainloop()
