#!/usr/bin/env python3
# -*- coding: cp1251 -*-

#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from datetime import date



dict_room = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}


sdate = input("������ start ���� � ������ [18.10.2017] = ")
edate = input("������ end ���� � ������ [18.10.2017] = ")

teacher = '����� (�) ���� �����������'

url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi"
headers = {'Content-Type': 'text/html; charset=windows-1251'}

data = {'teacher':teacher.encode('cp1251'), 'sdate': sdate, 'edate': edate}


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
print(dict_line)
