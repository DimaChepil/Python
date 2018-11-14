# Импорт модулей python
from tkinter import *
clk = 0
clk2 = 0
clk3 = 0
lsum = 0
def btn_click():
    global clk
    global lsum
    clk += 1
    lsum += 1
    lbab1.config(text = "Button 1 clicked: {}".format(clk))
    lsuml.config(text = "SUM: {}".format(lsum))

def btn_click2():
    global clk2
    global lsum
    clk2 += 1
    lsum = lsum - 1
    lbab2.config(text = "Button 2 clicked: {}".format(clk2))
    lsuml.config(text = "SUM: {}".format(lsum))
    

def btn_click3():
    global clk3
    global lsum
    clk3 += 1
    lsum += 2
    lbab3.config(text = "Button 3 clicked: {}".format(clk3))
    lsuml.config(text = "SUM: {}".format(lsum))
    
def ent_enter(event):
    global clk
    txt = ent.get()
    lba.config(text = "Текст: " + txt,
    bg = 'yellow', fg = 'blue')
# Создание окна
root = Tk()
root.title('Моє вікно')
root.geometry('300x200+300+50')
#
# поле Entry
ent = Entry(root)
ent.config(fg = "blue", font = 'Courer_New 10', width = '300')
ent.insert(1,"Введіть текст і натисніть Enter")
ent.bind('<Return>', ent_enter)
ent.pack(side = TOP)
#
# метка Label
lba = Label(root)
lba.config(text = 'Метка')
lba.pack(side = TOP)

lbab1 = Label(root)
lbab1.config(text = 'Button 1 clicked: 0')
lbab1.pack(side = TOP)

lbab2 = Label(root)
lbab2.config(text = 'Button 2 clicked: 0')
lbab2.pack(side = TOP)

lbab3 = Label(root)
lbab3.config(text = 'Button 3 clicked: 0')
lbab3.pack(side = TOP)

lsuml = Label(root)
lsuml.config(text = 'SUM: 0')
lsuml.pack(side = TOP)

#
# кнопка Button
btn1 = Button(root)
btn1.config(text = '+1',fg = 'green' , command = btn_click)
btn1.pack(side = TOP)

btn2 = Button(root)
btn2.config(text = '-1',fg = 'red', command = btn_click2)
btn2.pack(side = TOP)

btn3 = Button(root)
btn3.config(text = '+2',fg = 'blue', command = btn_click3)
btn3.pack(side = TOP)
# Вывод окна на экран
root.mainloop()
