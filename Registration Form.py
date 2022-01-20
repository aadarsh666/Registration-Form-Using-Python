from cProfile import label
from cgitb import text
from tkinter import *
from tokenize import Number
from unicodedata import name
root = Tk()
root.geometry("500x300") #setting size of layout

def getvals():
    print("Your form submitted successfully.")

#Heading---------->
Label(root, text="Registration Form", font="bold").grid(row=0, column=5)

#Field Name---------->
Name = Label(root,text="Name").grid(row=1, column=2)
Number = Label(root,text="Number").grid(row=2, column=2)
Gender = Label(root,text="Gender").grid(row=3, column=2)
Gmail = Label(root,text="Gmail").grid(row=4, column=2)
Paymentmode = Label(root,text="Paymentmode").grid(row=5, column=2)
Password = Label(root,text="Password").grid(row=6, column=2)

#Variables for storing data---------->
namevalue = StringVar
numbervalue = StringVar
gendervalue = StringVar
gmailvalue = StringVar
paymentvalue = StringVar
passwordvalue = StringVar
checkvalue = IntVar

#creating entry field---------->
nameentry = Entry(root, textvariable=namevalue) .grid(row=1,column=3)
numberentry = Entry(root, textvariable=numbervalue).grid(row=2,column=3)
genderentry = Entry(root, textvariable=gendervalue).grid(row=3,column=3)
gmailentry = Entry(root, textvariable=gmailvalue).grid(row=4,column=3)
paymententry = Entry(root, textvariable=paymentvalue).grid(row=4,column=3)
passwordentry = Entry(root, textvariable=paymentvalue).grid(row=5,column=3)

#craeting checkbox---------->
checkbtn = Checkbutton(text="Remember Me", variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit button---------->
Button(text="Submit", command=getvals).grid(row=7,column=3)

root.mainloop()
