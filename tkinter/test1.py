#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tkinter as tk

win = tk.Tk()
# window name
win.title('tkinter window')
# size of window
win.geometry('200x100')

var = tk.StringVar()

# label
label = tk.Label(   win, 
                    #text = 'Hello !',
                    textvariable = var,
                    bg = 'green',
                    font = ('Arial', 12),
                    width = 15, height = 2
                )
# put the label
label.pack()


clicked = False
def click_button():
	global clicked
	if clicked == False:
		clicked = True
		var.set('confirmed')
	else:
		clicked = False
		var.set('')

button = tk.Button( win,
                    text = 'ok',
                    width = 15, height = 2,
                    command = click_button
                    )
# put the button
button.pack()



win.mainloop()
