from tkinter import *


##########     Generator Leap Year     ##########

def convert_leap():
     leap_year_show.delete("0.0", END)
     year=int(year_input.get())
     if(year % 400 == 0) and(year % 100 == 0):
         leap_year_show.insert("0.0",str(year)+ " is a leap year")
     elif(year % 4 == 0) and(year % 100 != 0):
         leap_year_show.insert("0.0",str(year)+ " is a leap year")
     else:
         leap_year_show.insert("0.0",str(year)+ " is not a leap year")
      
   
          
sonu=Tk()

sonu.title("Leap Year")
sonu.geometry("800x800")
sonu.config(padx=30, pady=30, bg="#B8B8D7")




####  label  ####
label_title=Label(text="Leap Year Detection System", bg="#FFDADE",borderwidth=6,relief=SUNKEN, fg="#030101", font=("Arial", 30, "bold"))
label_title.pack(pady=10)



label_before_input = Label(text="I want a Convert leap year",bg="#FCBB8A",fg="#F7F7F7",font=("Arial", 15, "bold"))
label_before_input.pack()





### input ###
year_input=Entry(sonu,bg="#64EDE9",width=15)
year_input.pack(pady=30)







###  Button  ###


generate_year_button = Button(text="Generate Leap Year",bg="light green",font=("Arial",15,"bold"),height=2,width=20,command=convert_leap)
generate_year_button.pack()





################     shows    ##############
leap_year_show = Text(bg="yellow",font=("Arial", 20, "bold"), width=30,height=3)
leap_year_show.pack(pady=60)



1


#close sonu Tk()
sonu.mainloop()







 

   
 

             
     
    
    
        
   

   

   
   




























