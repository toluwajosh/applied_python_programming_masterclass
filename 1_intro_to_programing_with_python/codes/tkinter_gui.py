# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:34:58 2019

@author: Joshua Owoyemi
see tutorial details here: https://www.tutorialspoint.com/python/python_gui_programming.htm
"""

import tkinter
import tkinter.messagebox as tkMessageBox


window = tkinter.Tk()
# add a label to the window
window.title("GUI")
window.geometry("640x420")

# %% buttons and message boxes
# https://www.tutorialspoint.com/python/tk_button.htm
# https://www.tutorialspoint.com/python/tk_pack.htm

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(window, text ="Hello", command = helloCallBack, fg="blue")
# hello_button = tkinter.Button(window, text ="Hello", command = helloCallBack, fg="blue")
# # hello_button.place(bordermode=tkinter.OUTSIDE, height=100, width=100)
# hello_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
D = tkinter.Button(window, text ="How are you doing?", command = helloCallBack)

# set background and foreground with keywords bg="orange" and fg="red"

# B.pack(side=tkinter.LEFT)
D.grid(column=100, row=100)
D.pack()
#window.mainloop()

# %% canvas
# https://www.tutorialspoint.com/python/tk_canvas.htm

C = tkinter.Canvas(window, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

#C.pack()


# %% message
# https://www.tutorialspoint.com/python/tk_message.htm
var = tkinter.StringVar() # you can change the content of the variable with time
label = tkinter.Message(window, text="Where are you now? \nI know where I am but do you?")
#label = tkinter.Message(window, textvariable=var)
#label = tkinter.Message( window, textvariable=var, relief=tkinter.RAISED )
# label.grid(column=0, row=0)

var.set("Hey!?\nHow are you doing?")
label.pack()

# %% grid: arrange widget in grids
#for r in range(3):
#   for c in range(4):
#      tkinter.Label(window, text='R%s/C%s'%(r,c),
#         borderwidth=1 ).grid(row=r,column=c)

# %%
B.place(bordermode=tkinter.OUTSIDE, height=100, width=100)

window.mainloop()


# %% for combobox
# combo = tkinter.ttk.Combobox(window)
# combo["values"] = (1,2,3,4,5, "Text")
# combo.current(3)
# combo.grid()

# %% Checkbutton
# chk_state = tkinter.BooleanVar()
# chk_state.set(True) # set the button to True by default
# chk = tkinter.ttk.Checkbutton(window, text="Select", var=chk_state)
# chk.grid()


# %%  Radio buttons
# rad1 = tkinter.ttk.Radiobutton(window, text="Python", value=1)
# rad2 = tkinter.ttk.Radiobutton(window, text="Java", value=2)
# rad3 = tkinter.ttk.Radiobutton(window, text="Scala", value=3)
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)

"""
Other widgets:
Scroll Text
Message Box
SpinBox
"""

# %% Using frames
# # creating two frames, top and bottom
# top_frame = tkinter.Frame(window).pack(fill="x") # you can also use "y" as the fill parameter
# bottom_frame = tkinter.Frame(window).pack()

# %% Use .bind to execute a command when an event takes place

# %% use PhotoImage method to add a photo

# %% Use Entry for displaying special texts as such: Entry(frame, font={"arial", 18, "bold"}, textvariable = input_text, width = 50, bg = "#eee", bd=0)