from tkinter import * 
from tkinter.colorchooser import *
import tkinter
import functools







root = Tk()
root.title('Color interpolation') 
root.geometry("340x400")
label=Label(text="Select 2 colors to interpolate between them", padx=50, pady=20).grid(row=0,column=2)
root.resizable(0,0)





alist = []

rColor1=0
def chooseColor():

	color = askcolor()
	label=Label(text="First color is:").grid(row=2, column=2)
	canvas= tkinter.Canvas(width=30, height=30)
	canvas.grid(row=3, column=2)
	canvas.configure(background=color[1])
	global statusCheck
	statusCheck1= True
	alist.append(1)
	global color1Str
	color1Str=str(color[1])
	print(color1Str)
	r1Color1=color1Str[1:2]
	print(r1Color1)
	r2Color1=color1Str[2:3]
	print(r2Color1)
	g1Color1=color1Str[3:4]
	print(g1Color1)
	g2Color1=color1Str[4:5]
	print(g2Color1)
	b1Color1=color1Str[5:6]
	print(b1Color1)
	b2Color1=color1Str[6:7]
	print(b2Color1)

	color_list1=[r1Color1, r2Color1, g1Color1, g2Color1, b1Color1, b2Color1]
	lenth1=len(color_list1)
	for i in range(lenth1):
		if "a" in color_list1:
			color_list1[i]=color_list1[i].replace("a", "10")
		if "b" in color_list1:
			color_list1[i]=color_list1[i].replace("b", "11")
		if "c" in color_list1:
			color_list1[i]=color_list1[i].replace("c", "12")
		if "d" in color_list1:
			color_list1[i]=color_list1[i].replace("d", "13")
		if "e" in color_list1:
			color_list1[i]=color_list1[i].replace("e", "14")
		if "f" in color_list1:
			color_list1[i]=color_list1[i].replace("f", "15")					
	print(color_list1)

	global rc1
	rColor1=int(color_list1[0])*16 + int(color_list1[1])
	rc1=rColor1
	print(rColor1)


	global gc1
	gColor1=int(color_list1[2])*16 + int(color_list1[3])
	print(gColor1)
	gc1=gColor1

	global bc1
	bColor1=int(color_list1[4])*16 + int(color_list1[5])
	print(bColor1)
	bc1=bColor1





  
  

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


	global rc2
	rColor2=int(color_list[0])*16 + int(color_list[1])
	print(rColor2)
	rc2=rColor2

	global gc2
	gColor2=int(color_list[2])*16 + int(color_list[3])
	print(gColor2)
	gc2=gColor2

	global bc2
	bColor2=int(color_list[4])*16 + int(color_list[5])
	print(bColor2)
	bc2=bColor2


	





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
	#brojInt=int(broj)+1

	
	

	if ( 1 in alist ) and ( 2 in alist ) and not len(e.get()) ==0:
		labelMessage=Label(text="", width=50).grid(row=13, column=2)
		broj = e.get()
		global broj2
		try:
			broj2=int(broj)+2
			brojInt=int(broj)+1
			rColorDiffValue=abs(rc1-rc2)
			print(rColorDiffValue)
			gColorDiffValue=abs(gc1-gc2)
			print(gColorDiffValue)
			bColorDiffValue=abs(bc1-bc2)
			print(bColorDiffValue)

			rStep=rColorDiffValue/brojInt
			print(rStep)
			gStep=gColorDiffValue/brojInt
			print(gStep)
			bStep=bColorDiffValue/brojInt
			print(bStep)
			if broj2>2 and broj2<=502:
				
				
				
				
				top=Toplevel()
				top.title("Color palette "+ "(" + color1Str + "  -  " + color2Str + ",  " + broj +")")
				top.geometry()
				
				
				

				if broj2>19:
					for m in range(broj2//20):
						print(m)
						for j in range(20):
							print(m+j)
							print(j)
							print (m)
							print("/", end="")
							canvas= tkinter.Canvas(top, width=20, height=20)
							canvas.grid(row=1+m, column=j)
							canvas.configure(background="red")
							if rc1>rc2:
								canRColor=rc1-rStep*(20*m+j)
								print(canRColor)

								canRColorPaint=int(round(canRColor))
								print(canRColorPaint)
								quotientR=canRColorPaint//16
								rest1R=canRColorPaint%16
								rest2R=quotientR%16
								rest1RStr=str(rest1R)
								rest2RStr=str(rest2R)
								print(rest1R)
								print(rest2R)

							else:
								canRColor=rc1+rStep*(20*m+j)
								print(canRColor)

								canRColorPaint=int(round(canRColor))
								print(canRColorPaint)
								quotientR=canRColorPaint//16
								rest1R=canRColorPaint%16
								rest2R=quotientR%16
								rest1RStr=str(rest1R)
								rest2RStr=str(rest2R)
								print(rest1R)
								print(rest2R)	

							if gc1>gc2:

								canGColor=gc1-gStep*(20*m+j)												
								print(canGColor)

								canGColorPaint=int(round(canGColor))
								print(canGColorPaint)
								quotientG=canGColorPaint//16
								rest1G=canGColorPaint%16
								rest2G=quotientG%16
								rest1GStr=str(rest1G)
								rest2GStr=str(rest2G)
								print(rest1G)
								print(rest2G)

							else:
								canGColor=gc1+gStep*(20*m+j)
								print(canGColor)

								canGColorPaint=int(round(canGColor))
								print(canGColorPaint)
								quotientG=canGColorPaint//16
								rest1G=canGColorPaint%16
								rest2G=quotientG%16
								rest1GStr=str(rest1G)
								rest2GStr=str(rest2G)
								print(rest1G)
								print(rest2G)

							if bc1>bc2:

								canBColor=bc1-bStep*(20*m+j)
								print(canBColor)

								canBColorPaint=int(round(canBColor))
								print(canBColorPaint)
								quotientB=canBColorPaint//16
								rest1B=canBColorPaint%16
								rest2B=quotientB%16
								rest1BStr=str(rest1B)
								rest2BStr=str(rest2B)
								print(rest1B)
								print(rest2B)

							else:
								canBColor=bc1+bStep*(20*m+j)
								print(canBColor)

								canBColorPaint=int(round(canBColor))
								print(canBColorPaint)
								quotientB=canBColorPaint//16
								rest1B=canBColorPaint%16
								rest2B=quotientB%16
								rest1BStr=str(rest1B)
								rest2BStr=str(rest2B)
								print(rest1B)
								print(rest2B)


											
											
							colorHex_list=[rest2RStr, rest1RStr, rest2GStr, rest1GStr, rest2BStr,rest1BStr]
							lenthcolorHex=len(colorHex_list)
							for i in range(lenthcolorHex):
								if "10" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("10", "a")
								if "11" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("11", "b")
								if "12" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("12", "c")
								if "13" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("13", "d")
								if "14" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("14", "e")
								if "15" in colorHex_list:
									colorHex_list[i]=colorHex_list[i].replace("15", "f")				
																	
							print(colorHex_list)
							canvas.configure(background="#"+colorHex_list[0]+colorHex_list[1]+colorHex_list[2]+colorHex_list[3]+colorHex_list[4]+colorHex_list[5])		
													

										
					for k in range(broj2 % 20):
						print("/", end="")
						canvas= tkinter.Canvas(top, width=20, height=20)
						canvas.grid(row=2+m, column=k)
										
						canvas.configure(background="blue")

						if rc1>rc2:
							canRColor=rc1-rStep*(20*m+j+k)
							print(canRColor)

							canRColorPaint=int(round(canRColor))
							print(canRColorPaint)
							quotientR=canRColorPaint//16
							rest1R=canRColorPaint%16
							rest2R=quotientR%16
							rest1RStr=str(rest1R)
							rest2RStr=str(rest2R)
							print(rest1R)
							print(rest2R)

						else:
							canRColor=rc1+rStep*(20*m+j+k)
							print(canRColor)

							canRColorPaint=int(round(canRColor))
							print(canRColorPaint)
							quotientR=canRColorPaint//16
							rest1R=canRColorPaint%16
							rest2R=quotientR%16
							rest1RStr=str(rest1R)
							rest2RStr=str(rest2R)
							print(rest1R)
							print(rest2R)	

						if gc1>gc2:

							canGColor=gc1-gStep*(20*m+j+k)												
							print(canGColor)

							canGColorPaint=int(round(canGColor))
							print(canGColorPaint)
							quotientG=canGColorPaint//16
							rest1G=canGColorPaint%16
							rest2G=quotientG%16
							rest1GStr=str(rest1G)
							rest2GStr=str(rest2G)
							print(rest1G)
							print(rest2G)

						else:
							canGColor=gc1+gStep*(20*m+j+k)
							print(canGColor)

							canGColorPaint=int(round(canGColor))
							print(canGColorPaint)
							quotientG=canGColorPaint//16
							rest1G=canGColorPaint%16
							rest2G=quotientG%16
							rest1GStr=str(rest1G)
							rest2GStr=str(rest2G)
							print(rest1G)
							print(rest2G)

						if bc1>bc2:

							canBColor=bc1-bStep*(20*m+j+k)
							print(canBColor)

							canBColorPaint=int(round(canBColor))
							print(canBColorPaint)
							quotientB=canBColorPaint//16
							rest1B=canBColorPaint%16
							rest2B=quotientB%16
							rest1BStr=str(rest1B)
							rest2BStr=str(rest2B)
							print(rest1B)
							print(rest2B)

						else:
							canBColor=bc1+bStep*(20*m+j+k)
							print(canBColor)

							canBColorPaint=int(round(canBColor))
							print(canBColorPaint)
							quotientB=canBColorPaint//16
							rest1B=canBColorPaint%16
							rest2B=quotientB%16
							rest1BStr=str(rest1B)
							rest2BStr=str(rest2B)
							print(rest1B)
							print(rest2B)


											
											
						colorHex_list=[rest2RStr, rest1RStr, rest2GStr, rest1GStr, rest2BStr,rest1BStr]
						lenthcolorHex=len(colorHex_list)
						for i in range(lenthcolorHex):
							if "10" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("10", "a")
							if "11" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("11", "b")
							if "12" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("12", "c")
							if "13" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("13", "d")
							if "14" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("14", "e")
							if "15" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("15", "f")				
																	
						print(colorHex_list)
						canvas.configure(background="#"+colorHex_list[0]+colorHex_list[1]+colorHex_list[2]+colorHex_list[3]+colorHex_list[4]+colorHex_list[5])	
										
				else:			
					for l in range(broj2):
						print("/", end="")
						canvas= tkinter.Canvas(top, width=20, height=20)
						canvas.grid(row=1, column=l)
											
						canvas.configure(background="green")

						if rc1>rc2:
							canRColor=rc1-rStep*l
							print(canRColor)

							canRColorPaint=int(round(canRColor))
							print(canRColorPaint)
							quotientR=canRColorPaint//16
							rest1R=canRColorPaint%16
							rest2R=quotientR%16
							rest1RStr=str(rest1R)
							rest2RStr=str(rest2R)
							print(rest1R)
							print(rest2R)
						else:
							canRColor=rc1+rStep*l
							print(canRColor)

							canRColorPaint=int(round(canRColor))
							print(canRColorPaint)
							quotientR=canRColorPaint//16
							rest1R=canRColorPaint%16
							rest2R=quotientR%16
							rest1RStr=str(rest1R)
							rest2RStr=str(rest2R)
							print(rest1R)
							print(rest2R)

						if gc1>gc2:

							canGColor=gc1-gStep*l												
							print(canGColor)

							canGColorPaint=int(round(canGColor))
							print(canGColorPaint)
							quotientG=canGColorPaint//16
							rest1G=canGColorPaint%16
							rest2G=quotientG%16
							rest1GStr=str(rest1G)
							rest2GStr=str(rest2G)
							print(rest1G)
							print(rest2G)

						else:
							canGColor=gc1+gStep*l
							print(canGColor)

							canGColorPaint=int(round(canGColor))
							print(canGColorPaint)
							quotientG=canGColorPaint//16
							rest1G=canGColorPaint%16
							rest2G=quotientG%16
							rest1GStr=str(rest1G)
							rest2GStr=str(rest2G)
							print(rest1G)
							print(rest2G)

						if bc1>bc2:

							canBColor=bc1-bStep*l
							print(canBColor)

							canBColorPaint=int(round(canBColor))
							print(canBColorPaint)
							quotientB=canBColorPaint//16
							rest1B=canBColorPaint%16
							rest2B=quotientB%16
							rest1BStr=str(rest1B)
							rest2BStr=str(rest2B)
							print(rest1B)
							print(rest2B)

						else:
							canBColor=bc1+bStep*l
							print(canBColor)

							canBColorPaint=int(round(canBColor))
							print(canBColorPaint)
							quotientB=canBColorPaint//16
							rest1B=canBColorPaint%16
							rest2B=quotientB%16
							rest1BStr=str(rest1B)
							rest2BStr=str(rest2B)
							print(rest1B)
							print(rest2B)

						colorHex_list=[rest2RStr, rest1RStr, rest2GStr, rest1GStr, rest2BStr,rest1BStr]
						lenthcolorHex=len(colorHex_list)
						for i in range(lenthcolorHex):
							if "10" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("10", "a")
							if "11" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("11", "b")
							if "12" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("12", "c")
							if "13" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("13", "d")
							if "14" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("14", "e")
							if "15" in colorHex_list:
								colorHex_list[i]=colorHex_list[i].replace("15", "f")				
																	
						print(colorHex_list)
						canvas.configure(background="#"+colorHex_list[0]+colorHex_list[1]+colorHex_list[2]+colorHex_list[3]+colorHex_list[4]+colorHex_list[5])		
			else:
				labelMessage=Label(text="You must enter an entire positive number between 1 and 500", width=50).grid(row=13, column=2)
							
										
		except (TypeError, ValueError, ZeroDivisionError):
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



						
							




label_none2=Label(text="").grid(row=11, column=2)
button_3= Button(root, text="Interpolate colors",  command=interpolate,   width=20)

button_3.grid(row=12, column=2)






root.mainloop()