# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:39:07 2021

@author: taru_
"""

from tkinter import *
import random
root=Tk()
root.geometry("400x400")
root.title("Guess the Password - Mini Game")

password_input=Entry(root)
display_input=Label(root)
genpass_disp=Label(root)
array_3d=[[['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],["Pawn","Knight","Bishop","Castle","King","Queen"],['!','@','#','$','%','^','&','*']]]
def genPass():
    random_no=random.randint(0,25)
    random_no2=random.randint(0,5)
    random_no3=random.randint(0,7)
    randval1=array_3d[0][0][random_no]
    randval2=array_3d[0][1][random_no2]
    randval3=array_3d[0][2][random_no3]
    genpass_disp["text"]="Generated password: " + randval1+randval2+randval3
    input_val=password_input.get()
    display_input["text"]="The password you entered: " + str(input_val)

password_input.place(relx=0.5,rely=0.2,anchor=CENTER)
display_input.place(relx=0.5,rely=0.35,anchor=CENTER)
button1=Button(root,text="Generate the passsword!", command=genPass)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
genpass_disp.place(relx=0.5,rely=0.75,anchor=CENTER)
root.mainloop()