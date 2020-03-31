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

  color = askcolor()
  label=Label(text="First color is:").grid(row=2, column=2)
  canvas= tkinter.Canvas(width=30, height=30)
  canvas.grid(row=3, column=2)
  canvas.configure(background=color[1])
  global statusCheck
  statusCheck1= True
  print(str(statusCheck1))
  alist.append(1)
  global Color1Str
  Color1Str=str(color2[1])
  print(Color1Str)
  print(Color1Str[0] *2)
  

def chooseColor2():
	
	color2 = askcolor()
	label2=Label(text="Second color is:").grid(row=6, column=2)
	canvas2= tkinter.Canvas(width=30, height=30)
	canvas2.grid(row=7, column=2)
	canvas2.configure(background=color2[1])
	global statusCheck
	statusCheck2= True
	print(str(statusCheck2))
	alist.append(2)
	print(color2)
	global color2Str
	color2Str=str(color2[1])
	print(color2Str)
	

	r1Color2=color2Str[1:2]
	print(r1Color2)
	r2Color2=color2Str[2:3]
	print(r2Color2)
	g1Color2=color2Str[3:4]
	print(g1Color2)
	g2Color2=color2Str[4:5]
	print(g2Color2)
	b1Color2=color2Str[5:6]
	print(b1Color2)
	b2Color2=color2Str[6:7]
	print(b2Color2)

	color_list=[r1Color2, r2Color2, g1Color2, g2Color2, b1Color2, b2Color2]
	lenth=len(color_list)
	for i in range(lenth):
		if "a" in color_list:
			color_list[i]=color_list[i].replace("a", "10")
		if "b" in color_list:
			color_list[i]=color_list[i].replace("b", "11")
		if "c" in color_list:
			color_list[i]=color_list[i].replace("c", "12")
		if "d" in color_list:
			color_list[i]=color_list[i].replace("d", "13")
		if "e" in color_list:
			color_list[i]=color_list[i].replace("e", "14")
		if "f" in color_list:
			color_list[i]=color_list[i].replace("f", "15")					
	print(color_list)

	rColor2=int(color_list[0])*16 + int(color_list[1])
	print(rColor2)
	gColor2=int(color_list[2])*16 + int(color_list[3])
	print(gColor2)
	bColor2=int(color_list[4])*16 + int(color_list[5])
	print(bColor2)




button_1= Button(text="Choose first color", command= chooseColor, width=20)
button_1.grid(row=1, column=2, padx=20)
label_none=Label(text="").grid(row=4, column=2)
button_2= Button(text="Choose second color", command= chooseColor2, width=20)
button_2.grid(row=5, column=2, padx=20)
label_none2=Label(text="").grid(row=8, column=2)
label_number= Label(text="Enter the number of interpolations between 1 and 500: ").grid(row=9, column=2)

e = Entry (root, width=10,  borderwidth=1 )
e.grid(row=10, column=2, )





labelMessage=Label(text="", width=50).grid(row=13, column=2)

def interpolate():
	
	alist.append(3)
	broj = e.get()
	
	#brojI=int(broj)
	#print(brojI)

	if ( 1 in alist ) and ( 2 in alist ) and not len(e.get()) ==0: 
						labelMessage=Label(text="", width=50).grid(row=13, column=2)
						
						broj = e.get()
						global broj2
						
						
						
						try:
							broj2=int(broj)+2
								
							if broj2>2 and broj2<=502:
								top=Toplevel()
								top.title("Color palette")
								top.geometry("242x350")
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
							else:
								labelMessage=Label(text="You must enter an entire positive number between 1 and 500", width=50).grid(row=13, column=2)
				
										
						except (TypeError, ValueError):
								labelMessage=Label(text="You must enter an entire positive number between 1 and 500", width=50).grid(row=13, column=2)


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

#def hexTodec():

				    	
							




label_none2=Label(text="").grid(row=11, column=2)
button_3= Button(root, text="Interpolate colors",  command=interpolate,   width=20)

button_3.grid(row=12, column=2)






root.mainloop()