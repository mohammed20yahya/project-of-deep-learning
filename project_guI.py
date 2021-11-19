# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:43:52 2021

@author: moham
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import os

import numpy as np
#load the trained model to classify the images
from keras.models import load_model
model = load_model('GD.h5')
#dictionary to label all the CIFAR-10 dataset classes.

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Image Classification of Rock_Paper_Scissor')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((150,150))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    image = np.vstack([image])
    class1 = model.predict(image, batch_size=10)
    #print(class1)
    if (class1[0,0]==1):
        prediction="The image is : Paper"
    elif (class1[0,1]==1):
        prediction="The image is : Rock"
        
    elif (class1[0,2]==1):
        prediction="The image is : Scissor"
    
    
    
    
    #pred = model.predict_classes([image])[0]
    #sign = classes[pred]

    #print(sign)
  
    
    label.configure(foreground='#011638', text=prediction) 
def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
    command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    
    classify_b=Button(top,text="add_details      ",
    command=login,padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.55)
    
    
    
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
    
  
def next_page():
    global upload,sign_image,label,heading
    root_label.place_forget()
    my_label2.place_forget()
    myButton.place_forget()  
    
    upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
    upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
    upload.pack(side=BOTTOM,pady=50)
    sign_image.pack(side=BOTTOM,expand=True)
    label.pack(side=BOTTOM,expand=True)
    heading = Label(top, text="Image Classification of Rock_Paper_Scissor",pady=20, font=('arial',20,'bold'))
    heading.configure(background='#CDCDCD',foreground='#364156')
    heading.pack()

def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(top)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Provide the Credentials", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)
    
    

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(top)
                account_dashboard.title('Parameters')
                #Labels
                Label(account_dashboard, text="parameters_details", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="dataset name : "+name, font=('Calibri',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Traing details",font=('Calibri',12),width=30,command=training_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Modify",font=('Calibri',12),width=30,command=modify).grid(row=3,sticky=N,padx=10)
                
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!!")
                return
    login_notif.config(fg="red", text="No account found !!")
    
    

def modify():

    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_age1 = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(top)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Please enter new training parameters", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="d_name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="epochs_n", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Otimiz", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="PassW", font=('Calibri',12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=6,sticky=N,pady=10)
    
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)
    temp_age1=temp_age
    #Buttons
    Button(register_screen, text="Change", command = finish_reg, font=('Calibri',12)).grid(row=5,sticky=N,pady=10)
 
def finish_reg():
    global model
    name = temp_name.get()
    age = temp_age.get()

    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    model = load_model(gender)
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="All fields requried * ")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="modification is successful")

    
  
def training_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #Personal details screen
    training_details_screen = Toplevel(top)
    training_details_screen.title('Personal Details')
    #Labels
    Label(training_details_screen, text="trainig details", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(training_details_screen, text="d_name : "+details_name, font=('Calibri',12)).grid(row=1,sticky=W)
    Label(training_details_screen, text="epochs : "+details_age, font=('Calibri',12)).grid(row=2,sticky=W)
    Label(training_details_screen, text="Optimiz : "+details_gender, font=('Calibri',12)).grid(row=3,sticky=W)



#myFont = font.Font(family='Helvetica', size=20, weight='bold')
root_label=Label(top,text="Welcome to classifier ")
#root_label['font']=myFont
image1=ImageTk.PhotoImage(Image.open('rock-paper-scissors.jpg'))
my_label2=Label(image=image1)
myButton=Button(top,text="Welcome to Rock_paper_scissor classifier",font=('Calibri',20),padx=50,pady=50,command=next_page)
#root_label.grid(row=1,column=4,columnspan=3)
root_label.place(relx=0.5, rely=0.3, anchor=CENTER)
my_label2.place(relx=0.0, rely=0.0)

myButton.place(relx=0.5, rely=0.5, anchor=CENTER)
top.mainloop()
   
    
    
    
    
    


