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
app.geometry("600x600")
app.title("Image classification")
app.config(background="skyblue")

lbl=tk.Label(app,text="Fasion Items Predictor",font=("robort",24,"bold"),background="skyblue",foreground="black")
lbl.pack(pady=10)

btn=tk.Button(app,text="upload image",font=("robort",17,"bold"),background="black",foreground="skyblue",command=upload_image)
btn.pack()

imageshow=tk.Label(app,background="skyblue")
imageshow.pack(pady=10)

predict_result=tk.Label(app,text="",font=("robort",10,"italic"),background="skyblue")
predict_result.pack()

app.mainloop()