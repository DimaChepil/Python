from math import*
from tkinter import*

x0, y0 = 200, 300
x1 = 50; x2 = 350; dx = 10

root = Tk()
root.title('Chepil Dmytro')
root.geometry("800x800")
root.config(width=400, height=400, background='SpringGreen2', borderwidth=10, relief=RIDGE)

label = Label(root, text="Побудова графіка", font="Comic", bg='SpringGreen3')
label.pack(fill=X)

canvas = Canvas(root, height=600, width=700, bg='SpringGreen1')

canvas.create_line(0,y0,430,y0, fill='black', arrow=LAST) #vis X
canvas.create_line(x0,110,x0,450,fill='black', arrow=FIRST) #vis Y

canvas.create_text(225,310,text='25') #x_25
canvas.create_text(300,310,text='100') #x_100
canvas.create_text(215,200,text='100') #y_100
canvas.create_text(x0+5,110,text='y',anchor=W) #name vis Y
canvas.create_text(425,300,text='x',anchor=NW) #name vis X

canvas.create_rectangle([198,298],[203,303],width=0, fill='orange') #orange kvadrat

p = 50
while p<=350:
    canvas.create_line(p,295,p,305,fill='blue') 
    canvas.create_line(195,p+100,205,p+100,fill='blue')
    p+=10 #krok mitki

parabola=[]
for x in range(x1+30,x2+dx+30,dx):
    y = y0 - (x-(x0+30))**2/100
    z = (x,y)
    parabola.append(z)

pryama=[]
for x in range(x1+30,x2+30+dx,dx):
    y= y0-(abs(x-x0-30))
    z = (x,y)
    pryama.append(z)

print(parabola)
print(len(parabola))
canvas.create_line(parabola,fill='yellow', smooth=1,width=2)

print(pryama)
print(len(pryama))
canvas.create_line(pryama, fill='red', smooth=1, width=2)

canvas.pack()
button = Button(root, text='Закривушка насяльніка', command=quit)
button.pack()
