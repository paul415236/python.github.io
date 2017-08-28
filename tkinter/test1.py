#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tkinter as tk

win = tk.Tk()
# window name
win.title('tkinter window')
# size of window
win.geometry('200x200')


# entry
entry = tk.Entry(   win,
                    #show='*', # all the input words will be shown as *
                    show = None
                )
entry.pack()

def insert_point():
    var = entry.get()
    text.insert('insert', var)

def insert_end():
    var = entry.get()
    text.insert('end', var)

def clean_text():
    #text.delete(1.0, 'end')    # clear all
    text.delete(1.0)            # clear a word

button_1 = tk.Button(   win,
                        text = 'insert point',
                        width = 15, height = 2,
                        command = insert_point
                    )

button_2 = tk.Button(   win,
                        text = 'insert point',
                        width = 15, height = 2,
                        command = insert_end
                    )

button_3 = tk.Button(   win,
                        text = 'clear',
                        width = 15, height = 2,
                        command = clean_text
                    )
# put the button
button_1.pack()
button_2.pack()
button_3.pack()

text = tk.Text( win,
                height = 2
                )
text.pack()

win.mainloop()
