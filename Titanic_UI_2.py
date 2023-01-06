import tensorflow as tf
from tkinter import *
from tkinter import ttk
import pickle
import numpy as np

# [pclass , sex , age , sibsp , parch , fare , cabin , embarked] # Fix index of each specific features.

def replace_embarked(x):
    if x == "Southampton":
        return 0
    elif x == "Cherbourg":
        return 1
    elif x == "Queenstown":
        return 2


def replace_cabin(x):
    dic_cabin = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'T': 7}
    return dic_cabin[x]

def define_sex(x):
    if x == "male":
        return 1
    elif x == "female":
        return 0

def predict_state(arr):
  for p in arr:
    if p[0] > 0.5 and p[0] > p[1]:
      return "Die"
    elif p[1] > 0.5 and p[1] > p[0]:
      return "Survive"


def instance():
    pclass = float(pcc.get())
    sex = float(define_sex(sexc.get()))
    age = float(age_et.get())
    sibsp = float(sibet.get())
    parch = float(paret.get())
    fare = float(faet.get())
    cabin = float(replace_cabin(cabc.get()))
    emb_bf = emc.get()
    embark = replace_embarked(emb_bf)
    person = np.array([[pclass , sex , age , sibsp , parch , fare , cabin , embark]])
    return person

def run_model():
    model_path_1 = "modelV5_2_2D_cop1.h5"
    model_path_2 = "modelV5_3_1D_cop1.h5"
    model_path_3 = "Model_RF_V2_1D.pkl"
    data = instance()
    ch = modc.get()
    result_et.delete(0,END)
    if ch == "Model V5":
        modelV5_2 = tf.keras.models.load_model(model_path_1)
        predictions = modelV5_2.predict(data)
        result_et.insert("", f"{predictions[0][1]*100:.2f}")
    elif ch == "Model V5 (Norm)":
        modelV5_3 = tf.keras.models.load_model(model_path_2)
        predictions = modelV5_3.predict(data)
        result_et.insert("", f"{predictions[0][1]*100:.2f}")
    elif ch == "Model V2 (RF)":
        modelRF_2 = pickle.load(open(model_path_3 , "rb"))
        predictions = modelRF_2.predict(data)
        result_et.insert("" , f"{predictions[0][1]*100:.2f}")




def Clear():
    age_et.delete(0,END)
    sibet.delete(0 ,END)
    paret.delete(0,END)
    faet.delete(0 ,END)

Home =  Tk()
Home.geometry("1000x1000")
style = ttk.Style()
style.configure("Bold.TLabel", font=("Times", 9, "roman"))
frame = Frame(Home)
frame.pack()

# model drop down menu
model_tup = ("Model V5" , "Model V5 (Norm)" , "Model V2 (RF)" )
l1 = StringVar()
modc = ttk.Combobox( width = 30, textvariable = l1, state='readonly',font=("Times", 15, "roman"))
modc["values"]=  model_tup
modc.place(x=  400 , y=  10)
modc.current(0)
lab_model = Label(text = "Models",font=("Times", 15, "roman"))
lab_model.place(x = 320, y =10)

# passenger class drop down menu
pclass_tup = ("1" , "2" , "3")
l2  = StringVar()
pcc = ttk.Combobox( width = 30, textvariable = l2, state='readonly',font=("Times", 15, "roman"))
pcc["values"] = pclass_tup
pcc.place(x = 400 , y = 50)
pcc.current(0)
lab_pc = Label(text = "Passenger class",font=("Times", 15, "roman"))
lab_pc.place(x = 300  ,y =50)

# sex drop down menu
sex_tup = ("male" , "female")
l3 = StringVar()
sexc = ttk.Combobox( width = 30, textvariable = l3, state='readonly',font=("Times", 15, "roman"))
sexc["values"] = sex_tup
sexc.place(x = 400 , y = 90)
sexc.current(0)
lab_sex = Label(text = "Sex",font=("Times", 15, "roman"))
lab_sex.place(x = 320 , y= 90)

# age entry
age_et = ttk.Entry(frame, width=90,font=("Times", 15, "roman"))
age_et.pack(pady = 130 , padx = 28)# y=  130 , x = 28
lab_age = Label(text = "Age",font=("Times", 15, "roman"))
lab_age.place(x =300 , y= 130)



# Sibsp entry
sibet = ttk.Entry(frame, width=90,font=("Times", 15, "roman"))
sibet.place(x = 110 , y =170)
lab_sib = Label(text = "Number of Siblings and Spouses",font=("Times", 15, "roman"))
lab_sib.place(x = 225, y= 170)

# parch entry
paret = ttk.Entry(frame, width=90,font=("Times", 15, "roman"))
paret.place(x = 110 , y= 210)
lab_par = Label(text = "Number of Parents and child",font=("Times", 15, "roman"))
lab_par.place(x = 230 , y= 210)

# fare entry
faet = ttk.Entry(frame, width=90,font=("Times", 15, "roman"))
faet.place(x = 110 , y = 250)
lab_faet = Label(text = "Fare",font=("Times", 15, "roman"))
lab_faet.place(x = 350 , y = 250)

# cabin drop down menu
cab_tup = ("A" , "B" , "C" , "D" ,"E" , "F" , "G" ,"T")
l4 = StringVar()
cabc = ttk.Combobox( width = 30, textvariable = l4, state='readonly',font=("Times", 15, "roman"))
cabc["values"] = cab_tup
cabc.place(x = 400 , y = 290)
cabc.current(0)
lab_cab = Label(text = "Cabins level",font=("Times", 15, "roman"))
lab_cab.place(x = 300 , y = 290)

# embarked drop down menu
em_tup = ("Southampton" , "Cherbourg" , "Queenstown")
l5 = StringVar()
emc = ttk.Combobox( width = 30, textvariable = l5, state='readonly',font=("Times", 15, "roman"))
emc["values"] = em_tup
emc.place(x = 400 , y = 330)
emc.current(0)
lab_em = Label(text = "Embarked",font=("Times", 15, "roman"))
lab_em.place(x = 325 , y = 330)

# result (Survived / died)
result_et = ttk.Entry(frame, width=40,font=("Times", 25, "roman"))
result_et.pack(pady = 130 , padx = 28)
lab_result = Label(text = "This person survival chance is",font=("Times", 15, "roman"))
lab_result.place(x = 260 , y = 430)
lab_result2 = Label(text = "%",font=("Times", 15, "roman"))
lab_result2.place(x = 1000 , y= 430)


# Clear button
clear_but = Button(Home , text = "clear" , command= Clear)
clear_but.place(x = 800 , y = 370) # x = 500 , y = 370

# run model
run_but = Button(Home , text = "Run Model" , command= run_model)
run_but.place(x = 500 , y = 370)

# Image of Titanic
photo = PhotoImage(file = "NicePng_cargo-ship-png_513814.png" )
phot = Label(Home , image= photo , width = 1000 , height = 250)
phot.place(x = 300 ,  y = 500)

title = Label(text = "Titanic : Machine Learning from disaster", font=("Times", 50, "roman"))
title.place(x = 300 , y = 800)
frame.mainloop()
