from tkinter import *
from tkinter import filedialog
global root
root=Tk()

root.title("IMAGE ENCRYPTION AND DECRYPTION")
root.geometry('1900x280')
root.configure(bg="orange")
global entry1

def encrypt_image():

    file1=filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
            file_name=file1.name
            key=entry1.get(1.0,END)
            k=Label(root,text="Image successfully encrypted or decrypted",font=("STENCIL",20))
            k.pack()
            root.after(4000,k.destroy)
                
            fi=open(file_name,'rb')
            image=fi.read()
            fi.close()
            image=bytearray(image)
            for index,values in enumerate(image):
                image[index]=(values)^(int(key))
            fi1=open(file_name,'wb')
            fi1.write(image)
            fi1.close()
L1=Label(root,text=" Enter the secret key \n  Click the Button ENTER to encrypt the image or decrypt the encrypted image ",font=("times new roman",26),bg="black",fg="sky blue")
L1.pack()

entry1=Text(root,height=1,width=40,font=("times new roman",30))
entry1.pack()
entry1.focus_set()

b1=Button(root,text="ENTER",command=lambda:encrypt_image(),pady=20,bg="green",fg="white",font="stencil")
b1.pack()

root.mainloop()



