import tkinter as tk
import joblib
import numpy as np
from tkinter import filedialog
from PIL import Image,ImageTk
# PIL--> pillow

items=["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",  "Sandal",  "Shirt", "Sneaker", "Bag", "Ankle boot"]


model=joblib.load("fasion-images-predictor.joblib")

def image_predictor(image_path):
    img=Image.open(image_path)
    resize_image=img.convert("L").resize((28,28))
    
    image_array=np.array(resize_image)
    
    convert_to_oneD = image_array.flatten()
    
    if convert_to_oneD.shape != (784,):
        predict_result.config(text=f"the result is ")
    else:
        my_img=model.predict(convert_to_oneD.reshape(1,-1))
    return my_img        
    
    

def upload_image():
    
    filepath=filedialog.askopenfilename()
    
    myimage=Image.open(filepath)
    
    myimage.thumbnail((400,400))
    img=ImageTk.PhotoImage(myimage)
    
    imageshow.config(image=img)
    imageshow.image=img
    
    result=image_predictor(filepath)
    predict_result.config(text=f"The result is  = {items[result[0]]}")

app=tk.Tk()
app.geometry("600x700")
app.title("Image classification")
app.config(background="#c1d6f7")

# flat, groove, raised, ridge, solid, or sunken

frame1=tk.Frame(app,relief="raised",borderwidth=5,background="#6789bf")
frame1.pack(fill="x",pady=15)

lbl=tk.Label(frame1,text="Fasion Items Predictor",font=("robort",24,"bold"),background="#6789bf",foreground="black")
lbl.pack(pady=10)

btn=tk.Button(app,text="upload image",font=("robort",17,"bold"),background="black",foreground="#c1d6f7",command=upload_image)
btn.pack()

imageshow=tk.Label(app,background="#c1d6f7")
imageshow.pack(pady=10)

frame3=tk.Frame(app,relief="groove",borderwidth=5,background="white")
frame3.pack(pady=10)

predict_result=tk.Label(frame3,text="",font=("robort",15,"bold"),background="white")
predict_result.pack()

app.mainloop()