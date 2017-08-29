#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket
import Tkinter as tk
import tkMessageBox

#win = tk.Tk()
#def hello():
#	tkMessageBox.showinfo("Say Hello", "Hello World")

#B1 = tk.Button(win, text = "Say Hello", command = hello)
#B1.pack()
#win.mainloop()

# 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8001))

s.listen(5)
connection,address = s.accept()
print 'Accept connection from %s:%d' % (address[0], address[1])

while True:
	buf = connection.recv(1024)
	if not buf:
		pass
	print buf[0]

	if buf[0] == "1":
		print "valid client ~~ "
		connection.send('welcome to server!')
	else:
		print "invalid client ~~~ "
		connection.send('please go out!')

connection.close()
