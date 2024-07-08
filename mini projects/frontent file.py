# Tkinter ---> python gui
import tkinter as tk
import joblib
import numpy as np

model=joblib.load("package-predictor.joblib")

def mypredictor():
    cgpa=ent.get(),
    cgpa=np.array([float(cgpa)])
    new_cgpa=cgpa.reshape(1,-1)
    # print(new_cgpa.shape,"xxxxxxxxxxxx")
    pkg=model.predict(new_cgpa)
    pkg=str(pkg)
    newpkg=pkg[:4]
    
    showpkg.config(text=F"Your Package is : {newpkg}")
    
    ent.delete(0,tk.END)
    
app = tk.Tk()
app.geometry("600x300")
app.title("Package Predictor")
app.config(backgroung ="#94e3db")

haeder=tk.Label(app,text="Check Your Package on CGPA",font=("robort",20,"bold"),background="yellow")
haeder.pack(fill ="x",ipady=10)

lbl=tk.Label(app,text="Enter CGPA",Font=("robort",30,"bold"),foreground="green",background="#8fed5c")
lbl.pack(pady=17)

ent=tk.Entry(app,font=("robort",20,"italic"))
ent.pack()

btn=tk.Button(app,text="check package",Font=("robort",15,"bold"),bg="blue",fg="lightgreen",command=mypredictor)
btn.pack(pady=17)

showpkg = tk.Label(app, text = "", foreground = "#2f730a", background = "#8fed5c", font = ("robort", 15))
showpkg.pack()

app.mainloop()

