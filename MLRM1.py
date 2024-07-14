import tkinter as tk
import joblib 
import numpy as np

model=joblib.load("student_result_predictor.joblib")

def pred():
    x1=Enter1.get()
    x2=Enter2.get()
    x3=Enter3.get()
    x4=Enter4.get()
    
    beta=model.coef_
    intercept=model.intercept_
    
    y=intercept+beta[0]*float(x1)+beta[1]*float(x2)+beta[2]*float(x3)+beta[3]*float(x4)
    
    show.config(text=f"Your Performance Result is : {y}")

app=tk.Tk()
app.geometry("600x440")
app.title("Student Result Predictor")
app.config(background="white")

frame1=tk.Frame(app,relief="flat",borderwidth=5,background="skyblue")
frame1.pack(fill="x")

label=tk.Label(frame1,text="Performance Predictor",font=("roboto",25,"bold"),background="skyblue")
label.pack(pady=9)

frame2=tk.Frame(app,relief="flat",borderwidth=5,background="skyblue")
frame2.pack(pady=25)

# lbl=tk.Label(frame2,text="")
# lbl.grid(row=0,column=0,padx=10,pady=10)

label1=tk.Label(frame2,text="Hours Studied",font=("robort",15,"bold"),background="skyblue")
label2=tk.Label(frame2,text="Previous Scores",font=("robort",15,"bold"),background="skyblue")
label3=tk.Label(frame2,text="Sleep Hours",font=("robort",15,"bold"),background="skyblue")
label4=tk.Label(frame2,text="PYQ's Practiced",font=("robort",15,"bold"),background="skyblue")

label1.grid(row=1,column=1,pady=8,padx=8)
label3.grid(row=3,column=1,pady=8,padx=8)
label4.grid(row=4,column=1,pady=8,padx=8)
label2.grid(row=2,column=1,pady=8,padx=8)

label5=tk.Label(frame2,text=":",font=("robort",15,"bold"),background="skyblue")
label6=tk.Label(frame2,text=":",font=("robort",15,"bold"),background="skyblue")
label7=tk.Label(frame2,text=":",font=("robort",15,"bold"),background="skyblue")
label8=tk.Label(frame2,text=":",font=("robort",15,"bold"),background="skyblue")

label5.grid(row=1,column=2,padx=5)
label6.grid(row=2,column=2,padx=5)
label7.grid(row=3,column=2,padx=5)
label8.grid(row=4,column=2,padx=5)

Enter1=tk.Entry(frame2,font=("robort",15))
Enter2=tk.Entry(frame2,font=("robort",15))
Enter3=tk.Entry(frame2,font=("robort",15))
Enter4=tk.Entry(frame2,font=("robort",15))

Enter1.grid(row=1,column=3)
Enter2.grid(row=2,column=3)
Enter3.grid(row=3,column=3)
Enter4.grid(row=4,column=3)

frame3=tk.Frame(app,relief="flat",borderwidth=5,background="white")
frame3.pack()

Button=tk.Button(frame3,text="Check Performance",command=pred,background="skyblue")
Button.pack()

frame4=tk.Frame(app,relief="flat",borderwidth=5,background="skyblue")
frame4.pack(fill="x",pady=25)

show=tk.Label(frame4,text="",font=("robort",15,"bold"),background="skyblue")
show.pack()

app.mainloop()