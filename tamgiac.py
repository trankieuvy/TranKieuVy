# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:40:32 2024

@author: Student
"""

print("Kiểm tra 3 cạnh của tam giác")

a = int(input("nhập cạnh a: "))
b = int(input("nhập cạnh b: "))
c = int(input("nhập cạnh c: "))
 
if (a+b>0) and (a+c>0) and (b+c>0):
    print("{}, {}, {} là 3 cạnh của tam giác". format( a, b, c))
if(a==b==c):
    print("tam giác đều")
elif(a*a + b*b== c*c) or (a*a + c*c==b*b) or (b*b + c*c== a*a):
     print("tam giác vuông")
else:
    print("tam giác thường")
    
        
    