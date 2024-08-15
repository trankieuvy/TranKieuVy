# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:10:49 2024

@author: Admin
"""

sotien=0

sokm=int(input("nhập số km đã làm tròn: "))
   
if (sokm==1):
    sotien= 20000*sokm
elif (1<sokm<=3):
    sotien= 13000*sokm
elif (4<=sokm<=8):
    sotien=3*13000+(sokm-3)*12000

else:
    sotien= 3*13000+(sokm-3)*12000+(sokm-8)*10000
    
if(sotien>100000):
    sotien= (3*13000+(sokm-3)*12000+(sokm-8)*10000)*0.92
    
print("tổng số tiền: ", int(sotien), "VND")


    



















