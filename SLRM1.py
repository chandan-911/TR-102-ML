# Tkinter ---> python gui
import tkinter as tk
import joblib
import numpy as np

model = joblib.load("package-predictor.joblib")

def mypredictor():
    cgpa=ent.get()
    cgpa=np.array([float(cgpa)])
    new_cgpa=cgpa.reshape(-1,1)
    # print(new_cgpa.shape,"xxxxxxxxxxxx")
    pkg=model.predict(new_cgpa)
    pkgg=str(pkg[0])
    newpkg=pkgg[:4]
    
    showpkg.config(text=F"Your Package is : {newpkg} lacs]")
    
    ent.delete(0,tk.END)
    
app = tk.Tk()
app.geometry("600x300")
app.title("Package Predictor")
app.config(background ="white")

header=tk.Label(app,text="Check Your Package on CGPA",font=("robort",20,"bold"),background="white",foreground="black")
header.pack(fill ="x",ipady=10)

lbl=tk.Label(app,text="Enter CGPA",font=("robort",30,"bold"),foreground="skyblue",background="white")
lbl.pack(pady=17)

ent=tk.Entry(app,font=("robort",20,"italic"))
ent.pack()

btn=tk.Button(app,text="check package",font=("robort",15,"bold"),bg="black",fg="white",command=mypredictor)
btn.pack(pady=17)

showpkg = tk.Label(app, foreground = "#2f730a", background = "white", font = ("robort", 15))
showpkg.pack()

app.mainloop()

