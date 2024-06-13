from tkinter import *
from tkinter import messagebox
def login():
    if usernameentry.get()=='' or  passwordentry.get()=='':
        messagebox.showerror("ERROR !","Fields can't be empty !")
    elif usernameentry.get()=='KEC' and passwordentry.get()=='1234':
        messagebox.showinfo("Success","Welcome")
        window.destroy()
        import sms

    else:
        messagebox.showerror("ERROR !","Please enter correct credentials!")


window = Tk()
window.geometry('1280x700+0+0')
window.title("Login System Of Student Management System")
window.resizable(False, False)

# Load the PNG background image
background_image = PhotoImage(file="img.png")

# Create a label to display the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0)

loginframe=Frame(window)
loginframe.place(x=400,y=150)

logoimg=PhotoImage(file='exchange.png')
logolabel=Label(loginframe,image=logoimg)
logolabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameimg=PhotoImage(file='group (1).png')
usernamelabel=Label(loginframe,image=usernameimg,text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernamelabel.grid(row=1,column=0,pady=5,padx=10)

usernameentry=Entry(loginframe,bd=5,width=30,font=('times new roman',14,'bold'))
usernameentry.grid(row=1,column=1,pady=15,padx=15)

passwordimg=PhotoImage(file='padlock.png')
passwordlabel=Label(loginframe,image=passwordimg,text='Password',compound=LEFT,font=('times new roman',20,'bold'))
passwordlabel.grid(row=2,column=0,pady=10,padx=10)

passwordentry=Entry(loginframe,bd=5,width=30,font=('times new roman',14,'bold'))
passwordentry.grid(row=2,column=1,pady=15,padx=15)

LOGINBUTTON=Button(loginframe,text='LOGIN',font=('times new roman',14,'bold'),pady=1,width=10,fg='white',bg='green',cursor='hand2',command=login)
LOGINBUTTON.grid(row=3,column=1)


window.mainloop()

