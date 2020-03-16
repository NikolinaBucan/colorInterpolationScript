from tkinter import * 
from tkinter.colorchooser import *
import tkinter
root = Tk()
root.title('Color interpolation') 
root.geometry("340x350")
label=Label(text="Select 2 colors to interpolate between them", padx=50, pady=20).grid(row=0,column=2)
#canvas= tkinter.Canvas(width=30, height=30)
#canvas.grid(row=1, column=3, )
#canvas["bg"]="green"

def chooseColor():
	color = askcolor()
	#print(color)
	label=Label(text="First color is:").grid(row=2, column=2)
	canvas= tkinter.Canvas(width=30, height=30)
	canvas.grid(row=3, column=2)
	#canvas.print(color)	
	#canvas["bg"]="red"
	canvas.configure(background=color[1])

def chooseColor2():
	color2 = askcolor()
		#print(color)
	label2=Label(text="Second color is:").grid(row=6, column=2)
	canvas2= tkinter.Canvas(width=30, height=30)
	canvas2.grid(row=7, column=2)
		#canvas.print(color)	
		#canvas["bg"]="red"
	canvas2.configure(background=color2[1])



button_1= Button(text="Choose first color", command= chooseColor, width=20)
button_1.grid(row=1, column=2, padx=20)
label_none=Label(text="").grid(row=4, column=2)
button_2= Button(text="Choose second color", command= chooseColor2, width=20)
button_2.grid(row=5, column=2, padx=20)
label_none2=Label(text="").grid(row=8, column=2)
label_number= Label(text="Enter the number of interpolations:").grid(row=9, column=2)

e = Entry (root, width=10,  borderwidth=1 )
e.grid(row=10, column=2, )

def interpolate():
		broj = e.get()
		global broj2
		broj2=int(broj)+2
		

		#print(broj2)
		labelProba=Label(text="ukupno "+ str(broj2)).grid(row=13, column=2)
		for i in range(broj2//5):
			for j in range(5):
				print("/", end="")
				
			print()
		for k in range(broj2 % 5):
			print("/", end="")
					

label_none2=Label(text="").grid(row=11, column=2)

button_3= Button(text="Interpolate colors", command=interpolate,  width=20)
button_3.grid(row=12, column=2)






root.mainloop()