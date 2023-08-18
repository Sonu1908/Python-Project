from tkinter import *
import pyttsx3
print(dir(pyttsx3))


##########     Generator Auido     ##########
def convert_speech():
    Auido_show.delete("0.0", END)
    engine = pyttsx3.init()
    speaker=str(text_input.get())
    engine.say(speaker)
    engine.runAndWait()
    Auido_show.insert("0.0", speaker)

    



############## User Interface      ###############
root=Tk()

root.title("Convert Text Voice")
root.geometry("800x800")
root.config(padx=50, pady=50, bg="#64EDAE")




label_title=Label(text="Convert Text To Speech",borderwidth=6,relief=SUNKEN, bg="red", fg="#030101", font=("Arial", 40, "bold"))
label_title.pack(pady=10)





label_before_input = Label(text="I want a Conver text",bg="#D9BB41",fg="#F7F7F7",font=("Arial", 15, "bold"))
label_before_input.pack()




text_input=Entry(root,bd=10,bg="skyblue",width=50)
text_input.pack(pady=30)




########    Button    ########
generate_auido_button = Button(text="Convert Auido",bg="yellow",font=("Arial",15,"bold"),height=3,width=20,command=convert_speech)
generate_auido_button.pack()







################     Auido show    ##############
Auido_show = Text(bg="#ABABC7",font=("Arial", 15, "bold"), width=50,height=10)
Auido_show.pack(pady=60)






#close root Tk()
root.mainloop()






