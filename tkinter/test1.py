#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tkinter as tk

win = tk.Tk()
# window name
win.title('tkinter window')
# size of window
win.geometry('200x100')

# label
label = tk.Label(	win, 
					text = 'Hello !',
					bg = 'green',
					font = ('Arial', 12),
					width = 15, height = 2
				)

# put the label
label.pack()

win.mainloop()
