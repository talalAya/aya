from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Employee.db")


color1 = '#1d3587'
#main window نافذه صغيره داخل مكتبه التيكنتر
root = Tk() 
root.title("employees management system")

root.geometry("1240x580+0+0")
root.resizable(False,False)
root.configure(bg=color1)

name =StringVar()
age =StringVar()
job =StringVar()
gender =StringVar()
email =StringVar()
mobile =StringVar()
search_by=StringVar()
search_value=StringVar()






# حقول النافذة
ent_frame =Frame(root,bg=color1)
ent_frame.place(x=1,y=1,width=360,height=550)
title = Label(ent_frame,text="employees company",font=('Calibri',18,'bold'),bg=color1,fg='white')
title.place(x=10,y=1)
#######################
lblName = Label(ent_frame,text="Name",font=('Calibri',16),bg=color1,fg='white')
lblName.place(x=10,y=50)
txtName =Entry(ent_frame,textvariable =name,width=20,font=('Calibri',16))
txtName.place(x=120,y=50) 
#######################
lbljob = Label(ent_frame,text="Job",font=('Calibri',16),bg=color1,fg='white')
lbljob.place(x=10,y=90)
txtjob =Entry(ent_frame,textvariable =job,width=20,font=('Calibri',16))
txtjob.place(x=120,y=90) 
###########################
lblgen = Label(ent_frame,text="Gender",font=('Calibri',16),bg=color1,fg='white')
lblgen.place(x=10,y=130)
comogen =ttk.Combobox(ent_frame,textvariable =gender,state='readonly',width=18,font=('Calibri',16))
comogen['values'] =("Male","Famale")
comogen.place(x=120,y=130)
##################################
lblage = Label(ent_frame,text="Age",font=('Calibri',16),bg=color1,fg='white')
lblage.place(x=10,y=170)
txtage =Entry(ent_frame,textvariable =age,width=20,font=('Calibri',16))
txtage.place(x=120,y=170) 
###############################
lblemail = Label(ent_frame,text="email",font=('Calibri',16),bg=color1,fg='white')
lblemail.place(x=10,y=210)
txtemail =Entry(ent_frame,textvariable =email,width=20,font=('Calibri',16))
txtemail.place(x=120,y=210) 
###########################
lblmobile = Label(ent_frame,text="Mobile",font=('Calibri',16),bg=color1,fg='white')
lblmobile.place(x=10,y=250)
txtmobile =Entry(ent_frame,textvariable =mobile,width=20,font=('Calibri',16))
txtmobile.place(x=120,y=250) 
###############################
lbladdress = Label(ent_frame,text="Address:",font=('Calibri',16),bg=color1,fg='white')
lbladdress.place(x=10,y=290)
txtaddress =Text(ent_frame,width=30,height=2,font=('Calibri',16))
txtaddress.place(x=10,y=330)


#======define======

def hide():
 root.geometry("360x504+0+0")

def show():
    root.geometry("1240x580+0+0")

btnhide = Button(ent_frame,text='Hide',cursor='hand2',command=hide,bg='white',bd=1,relief='solid')
btnhide.place(x=270,y=10)

btnshow = Button(ent_frame,text='Show',cursor='hand2',command=show,bg='white',bd=1,relief='solid')
btnshow.place(x=310,y=10)

def getData(event):
    selected_row= tv.focus()
    data = tv.item(selected_row)
    global row 
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7]) 


def displayAll():

    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def delete():
    if txtName.get() == ""  or txtage.get() == "" or txtjob.get() == "" or txtemail.get() == "" or txtmobile.get()=="" or comogen.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error", "Please chose employee" )
        return
    
    if messagebox.askokcancel("Warning", "are you sure you want to delete?") == True:
     db.remove(row[0])
     Clear()
     displayAll()
     messagebox.showinfo("Success", "employee deleted successfully!")



def Clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    txtaddress.delete(1.0,END)



def add_employee():
    if txtName.get() == ""  or txtage.get() == "" or txtjob.get() == "" or txtemail.get() == "" or txtmobile.get()=="" or comogen.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error", "Please fill all the entry" )
        return
    
    db.insert(
        txtName.get(),
        txtage.get(),
        txtjob.get(),
        txtemail.get(),
        comogen.get(),
        txtmobile.get(),
        txtaddress.get(1.0,END))
    messagebox.showinfo("Success", "Added new Employee")
    Clear()
    displayAll()

def update():
    if txtName.get() == "" or txtage.get() == "" or txtjob.get() == "" or txtemail.get() == "" or txtmobile.get()=="" or comogen.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error", "Please fill all the entry" )
        return
    if messagebox.askokcancel("Warning", "are you sure you want to update?") == True:
      db.update(row[0],
          txtName.get(),
          txtage.get(),
          txtjob.get(),
          txtemail.get(),
          comogen.get(),
          txtmobile.get(),
          txtaddress.get(1.0,END))
      Clear()
      displayAll()
      messagebox.showinfo("Success", "The employee's date has been updated")



def search():
   
     db.cur.execute("select * from employees where " +str(search_by.get()+" LIKE '%")+search_value.get()+"%'")
     rows = db.cur.fetchall()
     return rows
   

def search2():
   row= search()
   tv.delete(*tv.get_children())
   for row in search():
        tv.insert("",END,values=row)
  
   
def refrsh():
    displayAll()
    Clear()
    search_by.set("")
    search_value.set("")

   




    
    





################ الازرار
btn_frame=Frame(ent_frame,bg=color1,bd=0,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=145)

btn_add= Button(btn_frame,
            text='add',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='black',
            bg='#a8dadc',
            bd=0,cursor='hand2',
            command=add_employee).place(x=4,y=9,)
########################################################
btn_edit= Button(btn_frame,
            text='update',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='black',
            bg='#457b9d',
            bd=0,cursor='hand2',
            command=update).place(x=4,y=56)   
########################################################
btn_del= Button(btn_frame,
            text='delete',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='black',
            bg='#e63946',
            bd=0,cursor='hand2',
            command=delete).place(x=170,y=9)         
########################################################
btn_clear= Button(btn_frame,
            text='clear',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='black',
            bg='#f1faee',
            bd=0,cursor='hand2',
            command=Clear).place(x=170,y=56)   
#########################################################
btn_refrsh= Button(btn_frame,
            text='refrsh',
            width=29,
            height=1,
            font=('Calibri',16),
            fg='black',
            bg='#219ebc',
            bd=0,cursor='hand2',command=refrsh).place(x=4,y=105)
          




 #==============table frame================================

tree_frame= Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=610)
style= ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))

tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="40")

tv.heading("2",text="Name")
tv.column("2",width="140")

tv.heading("3",text="Age")
tv.column("3",width="50")

tv.heading("4",text="Job")
tv.column("4",width="120")

tv.heading("5",text="Email")
tv.column("5",width="150")

tv.heading("6",text="Gender")
tv.column("6",width="90")

tv.heading("7",text="Mobile")
tv.column("7",width="150")

tv.heading("8",text="Address")
tv.column("8",width="150")
#ترتيب الحقول وضبط المسافه الزايدة
tv['show']= 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=45,height=610,width=875)
#نفس عمل بليس لكن هذه تحدد اماكن العناصر افقي 
#tv.pack()
#####################################search##########
search_frame=Frame(tree_frame,bg=color1)
search_frame.place(x=0,y=0,height=45,width=875)

lbl_searc=Label(search_frame,text="search for employee", font=('Calibri',12),fg='white',bg=color1)
lbl_searc.place(x=50,y=10)

com_searc=ttk.Combobox(search_frame,width=10,font=('Calibri',13),justify='center',textvariable =search_by)
com_searc['value']=('id', 'name','age','job','gender','mobile','address')
com_searc.place(x=200,y=10)

ent_searc=Entry(search_frame,font=('Calibri',13),width=15,textvariable =search_value)
ent_searc.place(x=340,y=10)

bt_search=Button(search_frame,text='Search',font=('Calibri',10),cursor='hand2',activebackground='black',activeforeground='white',command=search2)
bt_search.place(x=500,y=10)


displayAll()

# a=db.fetch()
# file=open('aa.txt','w')
# file.write(str(a))
#امر تشغيل النافذه
#root.mainloop()
def loggin():
  lbll_fram=Frame(root,height=0,width=0)

# myapp= App()
# myapp.mainloop()1240x580

# lbll_fram=Frame(root,height=580,width=1240)
# lbll_fram.place(x=0,y=0)



# btn_add= Button(lbll_fram,
#             text='Login',
#             width=14,
#             height=1,
#             font=('Calibri',16),
#             fg='white',
#             bg='#457b9d',
#             bd=0,cursor='hand2',command=loggin).place(x=280,y=480)

root.mainloop()
