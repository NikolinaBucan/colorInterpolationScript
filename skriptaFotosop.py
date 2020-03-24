from tkinter import * 
from tkinter.colorchooser import *
import tkinter
import functools



root = Tk()
root.title('Color interpolation') 
root.geometry("340x400")
label=Label(text="Select 2 colors to interpolate between them", padx=50, pady=20).grid(row=0,column=2)
#canvas= tkinter.Canvas(width=30, height=30)
#canvas.grid(row=1, column=3, )
#canvas["bg"]="green"

alist = []
print("a")
def chooseColor():
	#global color

	#print(color)
  color = askcolor()
  label=Label(text="First color is:").grid(row=2, column=2)
  canvas= tkinter.Canvas(width=30, height=30)
  canvas.grid(row=3, column=2)
	#canvas.print(color)	
	#canvas["bg"]="red"
  canvas.configure(background=color[1])
  global statusCheck
  statusCheck1= True
  print(str(statusCheck1))
  alist.append(1)
  

 


def chooseColor2():
	#global color2

	color2 = askcolor()
			#print(color)
	label2=Label(text="Second color is:").grid(row=6, column=2)
	canvas2= tkinter.Canvas(width=30, height=30)
	canvas2.grid(row=7, column=2)
			#canvas.print(color)	
			#canvas["bg"]="red"
	canvas2.configure(background=color2[1])
	global statusCheck
	statusCheck2= True
	print(str(statusCheck2))
	alist.append(2)
	









button_1= Button(text="Choose first color", command= chooseColor, width=20)
button_1.grid(row=1, column=2, padx=20)
label_none=Label(text="").grid(row=4, column=2)
button_2= Button(text="Choose second color", command= chooseColor2, width=20)
button_2.grid(row=5, column=2, padx=20)
label_none2=Label(text="").grid(row=8, column=2)
label_number= Label(text="Enter the number of interpolations:").grid(row=9, column=2)

e = Entry (root, width=10,  borderwidth=1 )
e.grid(row=10, column=2, )

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

x_list=[]
i = 0
while i<100:
    x_list.append(i)
    i += 1
print(x_list)    

labelMessage=Label(text="", width=50).grid(row=13, column=2)
def interpolate():
	
	alist.append(3)
	broj = e.get()
	#brojI=int(broj)
	#print(brojI)

	if ( 1 in alist ) and ( 2 in alist ) and not len(e.get()) ==0: 
					labelMessage=Label(text="", width=50).grid(row=13, column=2)
					top=Toplevel()
					top.title("Color palette")
					top.geometry("242x350")	
					broj = e.get()
					global broj2
					broj2=int(broj)+2
					#print(broj2)
					if broj2>9:
						for i in range(broj2//10):
							for j in range(10):
								print("/", end="")
								canvas= tkinter.Canvas(top, width=20, height=20)
								canvas.grid(row=1+i, column=j)
								#canvas.configure(background="red")
								canvas.configure(background="red")	

							
						for k in range(broj2 % 10):
							print("/", end="")
							canvas= tkinter.Canvas(top, width=20, height=20)
							canvas.grid(row=2+i, column=k)
							#canvas.configure(background="red")
							canvas.configure(background="red")
					else:			
						 for l in range(broj2):
								print("/", end="")
								canvas= tkinter.Canvas(top, width=20, height=20)
								canvas.grid(row=1, column=l)
								#canvas.configure(background="red")
								canvas.configure(background="red")


	elif not ( 1 in alist ) and not ( 2 in alist ) and  len(e.get()) ==0:
			labelMessage=Label(text="You must enter all the information", width=50).grid(row=13, column=2)							
	elif ( 1 in alist ) and not ( 2 in alist ) and len(e.get()) ==0:
			labelMessage=Label(text="Select the second color and enter the number", width=50).grid(row=13, column=2)
	elif ( 1 in alist ) and not ( 2 in alist ) and not len(e.get()) ==0:
			labelMessage=Label(text="Select the second color", width=50).grid(row=13, column=2)
	elif ( 1 in alist ) and ( 2 in alist ) and len(e.get()) ==0:
			labelMessage=Label(text="Enter the number of interpolations", width=50).grid(row=13, column=2)


	elif not ( 1 in alist ) and ( 2 in alist ) and not len(e.get()) ==0:
			labelMessage=Label(text="Select the first color", width=50).grid(row=13, column=2)
	elif not ( 1 in alist ) and ( 2 in alist ) and len(e.get()) ==0:
			labelMessage=Label(text="Select the first color and enter the number ", width=50).grid(row=13, column=2)


	elif not ( 1 in alist ) and not ( 2 in alist ) and not len(e.get()) ==0:
			labelMessage=Label(text="Select the first and second colors", width=50).grid(row=13, column=2)		
			
	else:			
			labelMessage=Label(text="You must enter an entire positive number", width=50).grid(row=13, column=2)
			    	
						

def interpolate2():
	broj = e.get()
	global broj2
	broj2=int(broj)+2
	labelProba=Label(text="ukupno "+ str(broj2)).grid(row=13, column=2)	



label_none2=Label(text="").grid(row=11, column=2)
button_3= Button(root, text="Interpolate colors",  command=interpolate,   width=20)

button_3.grid(row=12, column=2)






root.mainloop()