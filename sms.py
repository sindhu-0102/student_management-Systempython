from tkinter import *
import ttkthemes
import time
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def iexit():
    result=messagebox.askyesno('Confirm !','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=stdtable.get_children()
    newlist=[]
    for index in indexing:
        content=stdtable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['ID','NAME','MOBILE','EMAIL','ADDRESS','GENDER','DOB','ADDED DATE','ADDED TIME'])
    table.to_csv(url,index=False)
    messagebox.showinfo('SUCCESS !','Data is saved successfully!')



def toplevel_data(title,button_text,command):

    global identry,nameentry,phoneentry,emailentry,addressentry,genderentry,dobentry,screen
    screen = Toplevel()
    screen.title(title)
    screen.resizable(False, False)
    screen.grab_set()

    idlabel = Label(screen, text='ID', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    identry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(screen, text='NAME', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, padx=10, pady=15)

    phonelabel = Label(screen, text='PHONE', font=('times new roman', 20, 'bold'))
    phonelabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneentry.grid(row=2, column=1, padx=10, pady=15)

    emaillabel = Label(screen, text='EMAIL', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailentry.grid(row=3, column=1, padx=10, pady=15)

    addresslabel = Label(screen, text='ADDRESS', font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressentry.grid(row=4, column=1, padx=10, pady=15)

    genderlabel = Label(screen, text='GENDER', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=5, column=1, padx=10, pady=15)

    doblabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    doblabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobentry.grid(row=6, column=1, padx=10, pady=15)

    student_but = Button(screen, text=button_text, command=command)
    student_but.grid(row=7, columnspan=2, pady=15, padx=10)
    if title=='Update Student':
     indexing = stdtable.focus()
     content = stdtable.item(indexing)
     listdata = content['values']
     identry.insert(0, listdata[0])
     nameentry.insert(0, listdata[1])
     phoneentry.insert(0, listdata[2])
     emailentry.insert(0, listdata[3])
     addressentry.insert(0, listdata[4])
     genderentry.insert(0, listdata[5])
     dobentry.insert(0, listdata[6])



def update_data():
    query='update student set name=%s,mobile=%s,mail=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),date,currtime,identry.get()))
    con.commit()
    messagebox.showinfo('SUCCESS!',f'ID{identry.get()} is modified successfully!',parent=screen)
    screen.destroy()
    show_student()





def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    stdtable.delete(*stdtable.get_children())
    for data in fetched_data:
        stdtable.insert('', END, values=data)

def delete_student():
    indexing=stdtable.focus()
    content=stdtable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,(content_id,))
    con.commit()
    messagebox.showinfo('DELETED !',f'This {content_id} is deleted successfully' )
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    stdtable.delete(*stdtable.get_children())
    for data in fetched_data:
        stdtable.insert('',END,values=data)

def search_data():
    query='select * from student where id=%s or name=%s or  mail=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),phoneentry.get(),addressentry.get(),genderentry.get(),dobentry.get()))
    stdtable.delete(*stdtable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        stdtable.insert('',END,values=data)








def add_data():
    if identry.get()=='' or nameentry.get()=='' or phoneentry.get()=='' or emailentry.get()=='' or addressentry.get()=='' or genderentry.get()=='' or dobentry.get()=='':
        messagebox.showerror('ERROR!','All fields required',parent=screen)
    else:
        cdate = time.strftime('%d/%m/%Y')
        ctime = time.strftime('%H:%M:%S')
        try:
          query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          mycursor.execute(query,(identry.get(),nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),cdate,ctime))
          con.commit()
          result=messagebox.askyesno('CONFIRM!','Data added successfully .Do you want to clean the form?',parent=screen)
          if result:
            identry.delete(0,END)
            nameentry.delete(0, END)
            phoneentry.delete(0, END)
            emailentry.delete(0, END)
            addressentry.delete(0, END)
            genderentry.delete(0, END)
            dobentry.delete(0, END)
          else:
            pass
        except:
            messagebox.showerror('ERROR!','ID cant be repeated',parent=screen)
            return

        query='select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        stdtable.delete(*stdtable.get_children())
        for data in fetched_data:
            datalist=list(data)
            stdtable.insert('',END,values=datalist)



def connect_database():
    def connect():
        global mycursor,con
        try:
           con=pymysql.connect(host='localhost',user='root',password='Sparklesthunde6')
           mycursor=con.cursor()
           messagebox.showinfo('Success!','Database connection is successfull !')
           connectwindow.destroy()
           addbut.config(state=NORMAL)
           searchbut.config(state=NORMAL)
           deletebut.config(state=NORMAL)
           updatebut.config(state=NORMAL)
           showbut.config(state=NORMAL)
           exportbut.config(state=NORMAL)



        except:
            messagebox.showerror('Error!','Invalid Details !',parent=connectwindow)
            return
        try:
          query='create database studentmanagementsystem'
          mycursor.execute(query)
          query='use studentmanagementsystem'
          mycursor.execute(query)
          query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),mail varchar(30),address varchar(100),gender varchar(30),dob varchar(20),date varchar(50),time varchar(50))'
          mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('DATABASE CONNECTION')
    connectwindow.resizable(0,0)

    hostlabel=Label(connectwindow,text='HOST NAME',font=('ariel',20,'bold'))
    hostlabel.grid(row=0,column=0,padx=20)

    hostentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=30,pady=20)

    userlabel=Label(connectwindow,text='USER NAME',font=('ariel',20,'bold'))
    userlabel.grid(row=1,column=0,padx=20)

    userentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    userentry.grid(row=1, column=1, padx=30, pady=20)

    passlabel = Label(connectwindow, text='PASSWORD', font=('ariel', 20, 'bold'))
    passlabel.grid(row=2, column=0, padx=20)

    passentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    passentry.grid(row=2, column=1, padx=30, pady=20)

    connectButton=ttk.Button(connectwindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=4)


def clock():
    global date,currtime
    date=time.strftime('%d/%m/%Y')
    currtime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'   Date: {date}\nTime: {currtime}')
    datetimelabel.after(1000,clock)

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('adapta')
root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(0,0)
datetimelabel=Label(root,font=('times new roman',18,'bold'))
datetimelabel.place(x=5,y=5)
clock()


s='Student Management System'
sliderlabel=Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderlabel.place(x=200,y=0)

connectButton=ttk.Button(root,text="Connect To Database",width=20,cursor='hand2',command=connect_database)
connectButton.place(x=900,y=10)

leftframe=Frame(root)
leftframe.place(x=50,y=65,width=300,height=600)

logoimg=PhotoImage(file='assessment.png')
logolabel=Label(leftframe,image=logoimg)
logolabel.grid(row=0,column=0)

addbut=ttk.Button(leftframe,text='Add Student',width=20,state=DISABLED,command=lambda :toplevel_data('Add Student','Add',add_data))
addbut.grid(row=1,column=0,pady=20,padx=25)

searchbut=ttk.Button(leftframe,text='Search Student',width=20,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchbut.grid(row=2,column=0,pady=10,padx=25)

deletebut=ttk.Button(leftframe,text='Delete Student',width=20,state=DISABLED,command=delete_student)
deletebut.grid(row=3,column=0,pady=20,padx=25)

updatebut=ttk.Button(leftframe,text='Update Student',width=20,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatebut.grid(row=4,column=0,pady=20,padx=25)

showbut=ttk.Button(leftframe,text='Show Student',width=20,state=DISABLED,command=show_student)
showbut.grid(row=5,column=0,pady=20,padx=25)

exportbut=ttk.Button(leftframe,text='Export Student',width=20,state=DISABLED,command=export_data)
exportbut.grid(row=6,column=0,pady=20,padx=25)

exitbut=Button(leftframe,text='Exit Student',width=10,command=iexit)
exitbut.grid(row=7,column=0,pady=20)

rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=550)

scrollx=(Scrollbar(rightframe,orient=HORIZONTAL))
scrolly=(Scrollbar(rightframe,orient=VERTICAL))
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

stdtable=ttk.Treeview(rightframe,columns=('ID','NAME','MOBILE NO','EMAIL','ADDRESS','GENDER','D.O.B','ADDED DATE','ADDED TIME'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.config(command=stdtable.xview)
scrolly.config(command=stdtable.yview)

stdtable.pack(fill=BOTH,expand=1)

stdtable.heading('ID',text='ID')
stdtable.heading('NAME',text='NAME')
stdtable.heading('MOBILE NO',text='MOBILE NO')
stdtable.heading('EMAIL',text='EMAIL')
stdtable.heading('ADDRESS',text='ADDRESS')
stdtable.heading('GENDER',text='GENDER')
stdtable.heading('D.O.B',text='D.O.B')
stdtable.heading('ADDED DATE',text='ADDED DATE')
stdtable.heading('ADDED TIME',text='ADDED TIME')
stdtable.config(show='headings')

stdtable.column('ID',width=50,anchor=CENTER)
stdtable.column('NAME',width=300,anchor=CENTER)
stdtable.column('EMAIL',width=400,anchor=CENTER)
stdtable.column('MOBILE NO',width=400,anchor=CENTER)
stdtable.column('ADDRESS',width=200,anchor=CENTER)
stdtable.column('GENDER',width=100,anchor=CENTER)
stdtable.column('D.O.B',width=100,anchor=CENTER)
stdtable.column('ADDED DATE',width=200,anchor=CENTER)
stdtable.column('ADDED TIME',width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',15,'bold'),foreground='black',background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='black')
root.mainloop()


