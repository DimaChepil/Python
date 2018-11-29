import shutil
import os


text=open('v15.txt', 'r').read()
rev = text[::-1]
z1=rev[1].upper()+rev[2:]
f=open('151.txt','w')
f.write(z1)
f.close()
