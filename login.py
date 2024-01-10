import tkinter as tk
#from main import root
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
from PIL import* 

class login(tk.Tk):
    global usname 
     #usname = StringVar()
    global paswd
    # paswd=StringVar()
    def __init__(self):
         super().__init__()
         
         self.geometry("700x600+400+140")
         self.title("My App")
         self.config(bg="green")
         self.title('Login Page')
         color1 = '#219ebc'
         usname=StringVar()
         paswd=StringVar()
         #=========background img====================
         self.bg_frame = Image.open('images\\background1.png')
         photo = ImageTk.PhotoImage(self.bg_frame )
         self.bg_frame2=ImageTk.PhotoImage(file='images\\background1.png')
         self.bg_panel = Label(self,image=photo)# mage=photo)
         self.bg_panel.image_names = photo
         self.bg_panel.pack(fill='both', expand='yes')
         # ====== Login Frame =========================
         self.lgn_frame = Frame(self, bg=color1, width=500, height=560)
         self.lgn_frame.place(x=110, y=20)

         self.heading = Label(self.lgn_frame, text="WELCOME", font=('yu gothic ui', 25, "bold"), bg=color1,fg='white',relief=FLAT)
         self.heading.place(x=100, y=30, width=300, height=35)
        # ============ Sign In Image =============================================
         self.sign_in_image = Image.open('images\\hyy.png')
         photo = ImageTk.PhotoImage(self.sign_in_image)
         self.sign_in_image_label = Label(self.lgn_frame,  bg=color1,image=photo)
         self.sign_in_image_label.image_names = photo
         self.sign_in_image_label.place(x=180, y=100)
         # ============ Sign In label =============================================
         self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg=color1, fg="white",font=("yu gothic ui", 17, "bold"))
         self.sign_in_label.place(x=210, y=215)
        # ============================username====================================
         self.username_label = Label(self.lgn_frame, text="Username", bg=color1, fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
         self.username_label.place(x=90, y=300)

         self.username_entry = Entry(self.lgn_frame, highlightthickness=0, textvariable=usname,relief=FLAT, fg="#6b6a69",font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
         self.username_entry.place(x=120, y=335, width=270)

         self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#457b9d", highlightthickness=0)
         self.username_line.place(x=90, y=359)
         # ===== Username icon =========
         self.username_icon = Image.open('images\\username_icon.png')
         photo = ImageTk.PhotoImage(self.username_icon)
         self.username_icon_label = Label(self.lgn_frame, bg=color1, image=photo)
         self.username_icon_label.image = photo
         self.username_icon_label.place(x=90, y=332)
          # ============================password====================================
         self.password_label = Label(self.lgn_frame, text="Password", bg=color1, fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
         self.password_label.place(x=90, y=380)

         self.password_entry = Entry(self.lgn_frame, highlightthickness=0,textvariable=paswd, relief=FLAT,  fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
         self.password_entry.place(x=120, y=416, width=270)

         self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#457b9d", highlightthickness=0)
         self.password_line.place(x=90, y=440)
         # ======== Password icon ================
         self.password_icon = Image.open('images\\password_icon.png')
         photo = ImageTk.PhotoImage(self.password_icon)
         self.password_icon_label = Label(self.lgn_frame, bg=color1,image=photo)
         self.password_icon_label.image = photo
         self.password_icon_label.place(x=90, y=414)
         #============login button =================================================================
         btn_add= Button(self,
            text='Login',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='white',
            bg='#457b9d',
            bd=0,cursor='hand2',command=self.loggin).place(x=280,y=480)
         # ========= show/hide password ==================================================================
         self.show_image = ImageTk.PhotoImage \
             (file='images\\show.png')

         self.hide_image = ImageTk.PhotoImage \
             (file='images\\hide.png')

         self.show_button = Button(self.lgn_frame,command=self.show, relief=FLAT,image=self.show_image,activebackground="white", borderwidth=0, background="white", cursor="hand2")
         self.show_button.place(x=370, y=420)#image=self.show_image,

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=370, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white" , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=370, y=420)
        self.password_entry.config(show='*')
    
    def loggin(self):  
        if  self.username_entry.get()=="" and self.password_entry.get() =="":
            messagebox.showeinf("","nooo")
        elif self.username_entry.get()=="ff" and self.password_entry.get() =="g":
             # self.windo=Toplevel(root)
             self.win=root(self)
             

        else:
            messagebox.showerror("","no")
       


    
log=login()
log.mainloop()





