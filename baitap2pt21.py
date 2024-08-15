# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:07:48 2024

@author: Student
"""

#import thư viện
import math
    
print("giải phương trình bậc 2: ax^2 + bx + c=0")

a= float(input("nhập a: "))
b= float(input("nhập b: "))
c= float(input("nhập c: "))

if a==0:
    if b==0:
        if c==0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        if c==0:
            print("phương trình có một nghiệm x=0")
        else:
            print("phương trình có một nghiệm x= ", -c/b)

delta = b**2 - 4*a*c
if( delta<0):
    print("Phương trình vô nghiệm")
elif( delta==0):
    x= (-b)/(2*a)   
    print("phương trình có nghiệm kép x1=x2=", x)
else:
    x1 = (-b-math.sqrt(delta))/2*a
    x2 = (-b+math.sqrt(delta))/2*a
    print("phương trình có 2 nghiệm phân biệt: ")
    print("x1", x1)
    print("x2", x2)
    

    
    
    
     