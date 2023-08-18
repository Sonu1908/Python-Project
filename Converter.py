    
from tkinter import *
from currency_converter import CurrencyConverter


a=CurrencyConverter()
#print(a.convert(2,"USD","INR"))





sonu=Tk()

sonu.title("Currency")
sonu.geometry("500x400")
sonu.config(padx=30, pady=30, bg="skyblue")


#Convert Currency
def nigam():
    txt.delete("0.0", END)
    amount=int(en1.get())
    cur1=en2.get()
    cur2=en3.get()
    data = a.convert(amount,cur1,cur2)
    txt.insert("0.0",data)
  
    



####  label  ####
l1=Label(sonu,text="Currency Converter", bg="#FFDADE",borderwidth=6,relief="ridge", fg="#030101", font=("Times", 40, "bold"))
l1.pack(pady=20)


l2=Label(sonu,text="Enter Amount Here: ",borderwidth=5,relief=SUNKEN, bg="red",fg="#030101", font=("Times", 15, "bold"))
l2.pack()

en1=Entry()
en1.pack(pady=10)



l3=Label(sonu,text="From..... : ",borderwidth=5,relief=SUNKEN,  bg="light green",fg="#030101", font=("Times", 15, "bold"))
l3.pack()

en2=Entry()
en2.pack(pady=10)


l4=Label(sonu,text="To..... : ",borderwidth=5,relief=SUNKEN,  bg="yellow",fg="#030101", font=("Times", 15, "bold"))
l4.pack()

en3=Entry()
en3.pack(pady=10)


#button
btn=Button(sonu,text="Click me",height=2,width=20,bg="orange",command=nigam)
btn.pack(pady=25)



#show
txt=Text(sonu,bg="gray", width=25,height=10,font=("Times", 35, "bold"))
txt.pack()







#close
sonu.mainloop()
