#-----------------------------------------------------------------
#
#-----------------------------------------------------------------
# by Rodrigo Wuerdig
#				Matheus Bohrer
#
#2020 - Porto Alegre
#-----------------------------------------------------------------
from tkinter import *

gscalingfactor=25 #use multiple of 10
#The bigger the value, more resolution you get
horz_entry_sequence=[1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
vert_entry_sequence=[1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
columns='' #horizontal sequence
lines='' 	#vertical sequence
for n in horz_entry_sequence:
	binar = bin(n)[2:]
	columns = columns + str(binar)
for n in vert_entry_sequence:
	binar = bin(n)[2:]
	lines = lines + str(binar)
#-----------------------------------------------------------------
def Vert1(cindex,nlines):
	yOffset = gscalingfactor
	canvas.create_text(cindex*gscalingfactor, gscalingfactor*0.7, text='1', font='Arial')
	for i in range(nlines) :
  		canvas.create_line(cindex*gscalingfactor, yOffset, cindex*gscalingfactor, yOffset+gscalingfactor)
  		yOffset = yOffset + gscalingfactor*2
	return 0

def Vert0(cindex,nlines):
	yOffset = gscalingfactor*2
	canvas.create_text(cindex*gscalingfactor, gscalingfactor*0.7, text='0', font='Arial')
	for i in range(nlines-1) :
  		canvas.create_line(cindex*gscalingfactor, yOffset, cindex*gscalingfactor, yOffset+gscalingfactor)
  		yOffset = yOffset + gscalingfactor*2
	return 0

def Hor1(lindex,ncolumns):
	xOffset = gscalingfactor
	canvas.create_text(gscalingfactor*0.7, lindex*gscalingfactor, text='1', font='Arial')
	for i in range(ncolumns) :
  		canvas.create_line(xOffset, lindex*gscalingfactor, xOffset+gscalingfactor, lindex*gscalingfactor)
  		xOffset = xOffset + gscalingfactor*2
	return 0

def Hor0(lindex,ncolumns):
	xOffset = gscalingfactor*2
	canvas.create_text(gscalingfactor*0.7, lindex*gscalingfactor, text='0', font='Arial')
	for i in range(ncolumns) :
  		canvas.create_line(xOffset, lindex*gscalingfactor, xOffset+gscalingfactor, lindex*gscalingfactor)
  		xOffset = xOffset + gscalingfactor*2
	return 0

#===============================================================
#Check if its an odd or evem columns
if ((len(columns))% 2)==0:
	hor_points = columns[:-1]
else:
	hor_points = columns

if ((len(lines))% 2)==0:
	ver_points = lines[:-1]
else:
	ver_points = lines
#===============================================================
#Generate dynamic window
root = Tk()
root.title('psicodelia')
canvas = Canvas(root, width=((len(hor_points)*gscalingfactor)+gscalingfactor*2), height=((len(ver_points)*gscalingfactor)+gscalingfactor*2), bg='white')

#start filling vertical lines
cind=1;
for bit in columns:
	if bit=='1':
		Vert1(cind,len(lines)//2)
	else:
		Vert0(cind,len(lines)//2)
	print(bit)
	cind=cind+1

#start filling horizontal lines
lind=1;
for bit in lines:
	if bit=='1':
		Hor1(lind,len(columns)//2)
	else:
		Hor0(lind,int((len(hor_points))/2))
	print(bit)
	lind=lind+1

canvas.pack()
canvas.update()
canvas.postscript(file="file.ps", colormode='color')
root.mainloop()


