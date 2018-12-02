import requests
from bs4 import BeautifulSoup
from datetime import date
from tkinter import *

root = Tk()
root.title('Кількість пар ПНУ \t © Dmytro Chepil')
root.geometry('376x239')

sdate = StringVar()
edate = StringVar()

sdate_label = Label(text="Введіть початкову дату у форматі [18.10.17] ")
edate_label = Label(text="Введіть кінцеву дату у форматі      [18.10.17] ")
 
sdate_label.grid(row=1, column=0, sticky="w")
edate_label.grid(row=2, column=0, sticky="w")
 
sdate_entry = Entry(textvariable=sdate)
edate_entry = Entry(textvariable=edate)
 
sdate_entry.grid(row=1,column=1, padx=5, pady=5)
edate_entry.grid(row=2,column=1, padx=5, pady=5)

lba_label=Label(text="Кількість пар: ")
lba_label.grid(row=4,column=1)

text=Text(width=15, height=8)
text.grid(row=5,column=1)

dict_room = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}

listbox_items = ['Гой Тарас Петрович',
                 'Махней Олександр Володимирович',
                 'Костишин Любов Павлівна',
                 'Василишин Павло Богданович',
                 'Мазуренко Віктор Володимирович',
                 'Казмерчук Анатолій Іванович',
                 'Заторський Роман Андрійович',
                 'Савка Іван Ярославович']

def select_item(event):
    value = (listbox.get(listbox.curselection()))
    if value == 'Гой Тарас Петрович':
          global teacher
          teacher = 'Гой Тарас Петрович'
          return teacher
    elif value == 'Махней Олександр Володимирович':
          teacher = 'Махней Олександр Володимирович'
          return teacher
    elif value == 'Костишин Любов Павлівна':
          teacher = 'Костишин Любов Павлівна'
          return teacher
    elif value == 'Василишин Павло Богданович':
          teacher = 'Василишин Павло Богданович'
          return teacher
    elif value == 'Мазуренко Віктор Володимирович':
          teacher = 'Мазуренко Віктор Володимирович'
          return teacher
    elif value == 'Казмерчук Анатолій Іванович':
          teacher = 'Казмерчук Анатолій Іванович'
          return teacher
    elif value == 'Заторський Роман Андрійович':
          teacher = 'Заторський Роман Андрійович'
          return teacher 
    else:
          teacher = 'Савка (п) Іван Ярославович'
          return teacher
      
             
listbox_label=Label(text="Виберіть викладача: ")
listbox_label.grid(row=4,column=0)

listbox = Listbox(root, width=40, height=8, font=('times', 10))
listbox.bind('<<ListboxSelect>>', select_item)
listbox.grid(row=5, column=0)

for item in listbox_items:
    listbox.insert(END, item)


def deleteText():
    text.delete(1.0, END)

def parser():
      sqdate=sdate.get()
      eqdate=edate.get()

      url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi"
      headers = {'Content-Type': 'text/html; charset=windows-1251'}

      data = {'teacher':teacher.encode('cp1251'), 'sdate': sqdate, 'edate': eqdate}


      r = requests.post(url, headers=headers, data = data )

      r.encoding = 'cp1251'
       
      soup = BeautifulSoup(r.text, "html.parser")
      rows = soup.find_all('tr')
      dict_line = {}

      if rows:
             for row in rows:
                  cols = row.find_all('td')
                  if cols[2].text != '':
                        if (len(cols[2].text.split()) !=0):
                              key=cols[2].text.split()[-1]
                              if (key in dict_line.keys()):
                                    dict_line[key]+=1
                              else:
                                    dict_line[key] =1
      for kv in dict_line.items():
            text.insert(1.0,(str(kv[0]) + " = " + str(kv[1])+ "\n"))


button = Button(text="Порахувати пари", command=parser, width=33)
button.grid(row=6,column=0)

buttonclear = Button(text="Очистити", command=deleteText, width=16)
buttonclear.grid(row=6,column=1)

root.mainloop()
