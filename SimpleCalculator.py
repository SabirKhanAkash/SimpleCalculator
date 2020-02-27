# Code by Sabir Khan Akash 
# CSE 16, RUET

from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("E:/Desktop/Images/calc.ico")   #put the directory of the calc.ico here

e = Entry(root, width=36, borderwidth=6)
e.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_allclear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num 
	global math
	math = "addition"
	f_num = int (first_number)
	e.delete(0,END)

def button_equal():
	second_number = e.get()
	e.delete(0,END)

	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0,END)

buttonallclr = Button(root, text="AC", font=25, padx=13, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_allclear())

button0 = Button(root, text="0", font=25.5, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(0))
button1 = Button(root, text="1", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(1))
button2 = Button(root, text="2", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(2))
button3 = Button(root, text="3", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(3))
button4 = Button(root, text="4", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(4))
button5 = Button(root, text="5", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(5))
button6 = Button(root, text="6", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(6))
button7 = Button(root, text="7", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(7))
button8 = Button(root, text="8", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(8))
button9 = Button(root, text="9", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=lambda: button_click(9))

buttonAdd = Button(root, text="+", font=25, padx=20.6, pady=15, bg="#454547", fg="#ffffff", command=button_add)
buttonSub = Button(root, text="-", font=40, padx=23, pady=15, bg="#454547", fg="#ffffff", command= button_subtract)
buttonMult = Button(root, text="x", font=25, padx=22, pady=15, bg="#454547", fg="#ffffff", command=button_multiply)
buttonDiv = Button(root, text="/", font=25, padx=23.4, pady=15, bg="#454547", fg="#ffffff", command=button_divide)

buttonEql = Button(root, text="=", font=25, padx=20, pady=15, bg="#454547", fg="#ffffff", command=button_equal)

button0.grid(row=4, column=1)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

buttonallclr.grid(row=4, column=0)

buttonAdd.grid(row=1, column=3)
buttonSub.grid(row=2, column=3)
buttonMult.grid(row=3, column=3)
buttonDiv.grid(row=4, column=3)

buttonEql.grid(row=4, column=2)

root.mainloop()