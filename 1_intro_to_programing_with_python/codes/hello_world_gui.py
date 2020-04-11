# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:34:58 2019

@author: Joshua Owoyemi
see tutorial details here: https://www.tutorialspoint.com/python/python_gui_programming.htm
"""

# import packages
import tkinter
import tkinter.messagebox as tkMessageBox

# Set up the window
window = tkinter.Tk()
window.title("GUI")
window.geometry("640x420")

# display message
hello_message = tkinter.Message(window, text="Hello World GUI")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# run the GUI
window.mainloop()
