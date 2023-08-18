
from tkinter import *
import pyqrcode
import png
from PIL import Image


'''
link=input("Enter anython to generate QR : ")
qr_code=pyqrcode.create(link)
qr_code.png("QRCode.png",scale=5)
Image.open("QRCode.png")
'''


window = Tk()  
window.geometry('300x350')
window.title('QR Code')





def create_qrcode():
    s1= qr_input.get()
    qr_code = pyqrcode.create(s1)
    qr_code.png('QRCode.png', scale = 6)
    qr_input.insert(0, s1)
    

    
#label
label_title=Label(text="Create QR Code",borderwidth=6,relief=SUNKEN, bg="red", font=("Arial", 20, "bold"))
label_title.pack(pady=30)

 




#input
qr_input=Entry(window,font='arial 15')
qr_input.pack(pady=10)



#Button
btn=Button(window,text='Create',bg='pink',font=("Arial", 15, "bold"),command=create_qrcode)
btn.pack()



#close
window.mainloop()
