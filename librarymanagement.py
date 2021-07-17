from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
from typing import List
import mysql.connector
import datetime


class login_system():
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.login_window = Toplevel(self.root)
        self.login_window.title('Login')
        self.login_window.geometry('500x250')
        self.login_window.config(background='black')
        self.loggedin = False

        user = Label(self.login_window, text='Username:', font=('times new roman',20, 'bold'), fg='white', bg='black', padx=15,pady=10)
        user.grid(row=0, column=0, padx=10, pady=10)

        password = Label(self.login_window, text='Password:', font=('times new roman',20, 'bold'), fg='white', bg='black', padx=15 )
        password.grid(row=1, column=0, padx=10, pady=10)

        self.user_var= StringVar()
        self.pass_var= StringVar()

        user_ent = Entry(self.login_window, width=20, font=('times new roman',18, 'bold'),textvariable=self.user_var)
        user_ent.grid(row=0, column=1)

        pass_ent = Entry(self.login_window, width=20,font=('times new roman',18, 'bold'),textvariable=self.pass_var)
        pass_ent.grid(row=1, column=1)

        submit = Button(self.login_window, text='Login', command=self.login,font=('times new roman',18, 'bold'))
        submit.grid(row=3, column=1, pady=10)

    def login(self):
        
        userinfo = self.user_var.get()
        passinfo= self.pass_var.get()
        conn = mysql.connector.connect(host='localhost', username='root', password = 'twarit@28', database = 'librarydb')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT username, password FROM login_system')
        rows = my_cursor.fetchall()

        conn.close()
        for row in rows:
            if row[0] ==userinfo:
                if row[1]==passinfo:
                    
                    tmsg.showinfo('Successful!', 'Logged In')
                    self.loggedin=True
                    self.newWindow= Toplevel(self.root)
                    
                    self.app = LibraryManagementSystem(self.newWindow)
                    self.login_window.destroy()
                                                  
                    
                else:
                    tmsg.showinfo('Incorrect', 'Incorrect Password. Please try again')
                    break
            else:
                tmsg.showinfo('Incorrect', 'Incorrect username. Please try again')
                break
        

class LibraryManagementSystem():
    def __init__(self, root):
        self.root= root
        self.root.title('Library Management System')
        self.root.geometry('1366x768')
        
        #--------------------------- Variables------------------------------
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()



        lbltitle = Label(self.root, text='Library Management System', bg='black', fg='white', relief=RIDGE, bd=12, font= ('times new roman', 40 , 'bold'), padx=10, pady=10)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, bg= 'black',  relief=RIDGE, padx=15 )
        frame.place(x=0, y=100, width=1366, height=390)

        #------------------------------DataFrame Left-----------------------------------------
        DataFrameLeft = LabelFrame(frame, text='Membership Information', bg='black', fg='white', relief=RIDGE, bd=12, font= ('times new roman', 20 , 'bold'), padx=10, pady=10)
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMember = Label(DataFrameLeft, text='Member Type: ' ,bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblMember.grid(row=0, column=0, sticky=W)
        comMember= ttk.Combobox(DataFrameLeft,font= ('times new roman', 15 , 'bold'), textvariable=self.member_var,state='readonly', width=20)
        comMember['value']= ('Admin Staff', 'Teacher', 'Student')   
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, text='PRN Number: ', bg='black',  fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22,textvariable=self.prn_var )
        txtPRN_NO.grid(row=1, column=1)

        lblID_NO = Label(DataFrameLeft, text='ID Number: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblID_NO.grid(row=2, column=0, sticky=W)
        txtID_NO = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22 ,textvariable=self.id_var)
        txtID_NO.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, text='First Name: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22 ,textvariable=self.firstname_var)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, text='Last Name: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22 ,textvariable=self.lastname_var)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, text='Address 1: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22,textvariable=self.address1_var)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, text='Address 2: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22,textvariable=self.address2_var)
        txtAddress2.grid(row=6, column=1)

        lblPostcode= Label(DataFrameLeft, text='Post Code: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblPostcode.grid(row=7, column=0, sticky=W)
        txtPostcode = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22,textvariable=self.postcode_var)
        txtPostcode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, text='Mobile: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=22,textvariable=self.mobile_var)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataFrameLeft, text='Book ID: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24 ,textvariable=self.bookid_var)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, text='Book Title: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1, column=3)

        lblAuthorName = Label(DataFrameLeft, text='Author Name: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblAuthorName.grid(row=2, column=2, sticky=W)
        txtAuthorName = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.author_var)
        txtAuthorName.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, text='Days Borrowed: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, text='Date Due: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.datedue_var)
        txtDateDue.grid(row=4, column=3)

        lblDaysonBook = Label(DataFrameLeft, text='Days On Book: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblDaysonBook.grid(row=5, column=2, sticky=W)
        txtDaysonBook = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.daysonbook_var)
        txtDaysonBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, text='Late Fine: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine= Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.latefine_var)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, text='Date Overdue: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, text='Actual Price: ', bg='black', fg='white',font= ('times new roman', 15 , 'bold'), padx=2, pady=2)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft,font= ('times new roman', 15 , 'bold'), width=24,textvariable=self.actualprice_var)
        txtActualPrice.grid(row=8, column=3)


        #------------------------DataFrame Right-------------------------------
        DataFrameRight = LabelFrame(frame, text='Book Information', bg='black', fg='white', relief=RIDGE, bd=12, font= ('times new roman', 20 , 'bold'), padx=10, pady=10)
        DataFrameRight.place(x=810, y=5, width=500, height=350)

        listbooks = ['Atomic Habits', 'The Subtle Art of Not Givig a *', 'The Psychology of Money', 'Machine Learning Yearning', 'Start With Why', 'Deep Learning.ai', 'The Intelligent Investor', 'Ikigai', 'Mein Kamph', 'Python for Everybody', 'Sapiens',
                        'Anything You Want', 'The Personal MBA', 'Say it Like Obama', 'Market Wizards', 'Anything You Want', 'The 4 hour work week','The Jungle Book', 'I am Kalam' ]

        listScrollBar= Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky='ns')

        def selectbook(event=""):
            value= str(listbox.get(listbox.curselection()))
            
            
            if (value=='Atomic Habits'):
                self.bookid_var.set('BK0001')
                self.booktitle_var.set('Atomic Habits')
                self.author_var.set('James Clear')
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days=15)
                d3= d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set(50)
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set(599)

            elif (value=='The Subtle Art of Not Givig a *'):
                self.bookid_var.set('BK0002')
                self.booktitle_var.set('The Subtle Art of Not Givig a *')
                self.author_var.set('Mark Manson')
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days=15)
                d3= d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set(50)
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set(749)

            elif (value=='The Psychology of Money'):
                self.bookid_var.set('BK0003')
                self.booktitle_var.set('The Psychology of Money')
                self.author_var.set('Morgan Housel')
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days=15)
                d3= d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set(50)
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set(1000)

            elif (value=='Machine Learning Yearning'):
                self.bookid_var.set('BK0004')
                self.booktitle_var.set('Machine Learning Yearning')
                self.author_var.set('Andrew NG')
                d1= datetime.datetime.today()
                d2= datetime.timedelta(days=15)
                d3= d1+d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set(50)
                self.dateoverdue_var.set('NO')
                self.actualprice_var.set(749)

            


        listbox= Listbox(DataFrameRight, font= ('times new roman', 10 , 'bold'), width=20, height=16)
        listbox.bind("<<ListboxSelect>>", selectbook)
        listbox.grid(row=0, column=0, padx=2)
        listScrollBar.config(command= listbox.yview)

        for item in listbooks:
            listbox.insert(END, item)

        self.txtbox= Text(DataFrameRight, font= ('times new roman', 10 ), width=40, height=16,padx=2, pady=4, state='normal')
        self.txtbox.grid(row=0, column=2, padx=5)

        #-----------------------Button Frame------------------
        FrameButton = Frame(self.root, bg='black',relief=RIDGE, bd=12,padx=10)
        FrameButton.place(x=0, y=490, width=1366, height=60)

        btnAddData = Button(FrameButton, text='Add Data', width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black', command=self.add_data)
        btnAddData.grid(row=0, column=0, padx=4)

        btnShowData = Button(FrameButton, text='Show Data',command=self.show_data, width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black')
        btnShowData.grid(row=0, column=1, padx=4)

        btnUpdate = Button(FrameButton, text='Update', command=self.update_data, width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black')
        btnUpdate.grid(row=0, column=2, padx=4)

        btnDelete = Button(FrameButton, text='Delete',command=self.delete_data, width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black')
        btnDelete.grid(row=0, column=3, padx=4)

        btnReset = Button(FrameButton, text='Reset',command=self.reset, width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black')
        btnReset.grid(row=0, column=4, padx=4)

        btnExit = Button(FrameButton, text='Exit',command=self.iExit, width=22, font= ('Lucida', 11 , 'bold'), bg='#EAE8E8', fg='black')
        btnExit.grid(row=0, column=5, padx=4)


        #-------------------------Information Frame----------------------

        FrameDetails = Frame(self.root, bg='black',relief=RIDGE, bd=10,padx=5, pady=5)
        FrameDetails.place(x=0, y=550, width=1366, height=150)

        Table_frame = Frame(FrameDetails, bg='black', relief=RIDGE, bd=6)
        Table_frame.place(x=0, y=2, width=1335, height=120)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table= ttk.Treeview(Table_frame, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set,  columns=('membertype', 'prnno', 'idnumber', 'firstname', 'lastname', 'address1', 'address2', 'postcode', 'mobile',
                                                            'bookid', 'booktitle', 'authorname', 'daysborrowed', 'datedue', 'daysonbook', 'latefine', 'dateoverdue', 'actualprice' )) #These are just dummy variables

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command= self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        names= ['Member Type','PRN NO','ID Number','First Name', 'Last Name', 'Address 1', 'Address 2', 'Post Code',
                'Mobile', 'Book ID', 'Book Title', 'Author Name', 'Days Borrowed', 'Date Due', 'Days On Book', 'Late Fine', 'Dats Overdue', 'Actual Price'] 
        cols= ['membertype', 'prnno', 'idnumber', 'firstname', 'lastname', 'address1', 'address2', 'postcode', 'mobile',
                                                            'bookid', 'booktitle', 'authorname', 'daysborrowed', 'datedue', 'daysonbook', 'latefine', 'dateoverdue', 'actualprice']

        for name, col in zip(names, cols):
            self.library_table.heading(col, text=name)
       


        self.library_table['show']= 'headings'
        self.library_table.pack(fill=BOTH, expand=1)
        
        
        for col in cols:
            self.library_table.column(col, width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_data_from_db )

    def add_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password= 'twarit@28', database= 'librarydb')
        my_cursor= conn.cursor()
        my_cursor.execute("INSERT INTO libb VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(
                                                                                                self.member_var.get(),
                                                                                                self.prn_var.get(),
                                                                                                self.id_var.get(),
                                                                                                self.firstname_var.get(),
                                                                                                self.lastname_var.get(),
                                                                                                self.address1_var.get(),
                                                                                                self.address2_var.get(),
                                                                                                self.postcode_var.get(),
                                                                                                self.mobile_var.get(),
                                                                                                self.bookid_var.get(),
                                                                                                self.booktitle_var.get(),
                                                                                                self.author_var.get(),
                                                                                                self.dateborrowed_var.get(),
                                                                                                self.datedue_var.get(),
                                                                                                self.daysonbook_var.get(),
                                                                                                self.latefine_var.get(),
                                                                                                self.dateoverdue_var.get(),
                                                                                                self.actualprice_var.get()
                                                                                             
        ) )
        conn.commit()
        self.fetch_data()
        conn.close()
        tmsg.showinfo('Successful!', 'Member has been inserted successfully!')

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password= 'twarit@28', database= 'librarydb')
        my_cursor= conn.cursor()
        my_cursor.execute(" SELECT * FROM libb")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("", END, values=row)

            conn.commit()

        conn.close()

    def get_data_from_db(self, event=""):
        cursor_row = self.library_table.focus()
        content= self.library_table.item(cursor_row)
        row= content['values']
        
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),  
        self.actualprice_var.set(row[17])

    def show_data(self):
        self.txtbox.insert(END, "Member Type\t\t"+ self.member_var.get()+ "\n")
        self.txtbox.insert(END, "PRN NO\t\t"+ self.prn_var.get()+ "\n")
        self.txtbox.insert(END, "ID No.\t\t"+ self.id_var.get()+ "\n")
        self.txtbox.insert(END, "First Name\t\t"+ self.firstname_var.get()+ "\n")
        self.txtbox.insert(END, "Last Name\t\t"+ self.lastname_var.get()+ "\n")
        self.txtbox.insert(END, "Address 1\t\t"+ self.address1_var.get()+ "\n")
        self.txtbox.insert(END, "Address 2\t\t"+ self.address2_var.get()+ "\n")
        self.txtbox.insert(END, "Post Code\t\t"+ self.postcode_var.get()+ "\n")
        self.txtbox.insert(END, "Mobile\t\t"+ self.mobile_var.get()+ "\n")
        self.txtbox.insert(END, "Book ID\t\t"+ self.bookid_var.get()+ "\n")
        self.txtbox.insert(END, "Book Title\t\t"+ self.booktitle_var.get()+ "\n")
        self.txtbox.insert(END, "Author\t\t"+ self.author_var.get()+ "\n")
        self.txtbox.insert(END, "Date Borrowed\t\t"+ self.dateborrowed_var.get()+ "\n")
        self.txtbox.insert(END, "Date Due\t\t"+ self.datedue_var.get()+ "\n")
        self.txtbox.insert(END, "Days On Book\t\t"+ self.daysonbook_var.get()+ "\n")
        self.txtbox.insert(END, "Late Fine\t\t"+ self.latefine_var.get()+ "\n")
        self.txtbox.insert(END, "Date Overdue\t\t"+ self.dateoverdue_var.get()+ "\n")
        self.txtbox.insert(END, "Actual Price\t\t"+ self.actualprice_var.get()+ "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(''),
        self.address1_var.set(''),
        self.address2_var.set(''),
        self.postcode_var.set(''),
        self.mobile_var.set(''),
        self.bookid_var.set(''),
        self.booktitle_var.set(''),
        self.author_var.set(''),
        self.dateborrowed_var.set(''),
        self.datedue_var.set(''),
        self.daysonbook_var.set(''),
        self.latefine_var.set(''),
        self.dateoverdue_var.set(''),  
        self.actualprice_var.set('')
        self.txtbox.delete('1.0',END)

    def iExit(self):
        iExit= tmsg.askyesno("Exit?", 'Do you want to exit?')
        if iExit>0:
            self.root.destroy()
            

    def update_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password= 'twarit@28', database= 'librarydb')
        my_cursor= conn.cursor()
        my_cursor.execute(" UPDATE libb SET  Member=%s, PRN_NO=%s, ID=%s, FirstName= %s, LastName=%s, Address1=%s, Address2=%s, PostCode= %s, Mobile=%s, BookID=%s, BookTitle=%s, AuthorName=%s, DaysBorrowed=%s, DateDue=%s, DaysonBook=%s, LateFine=%s, DateOverdue=%s, ActualPrice=%s WHERE PRN_NO=%s", (
                                                                                                self.member_var.get(),
                                                                                                self.prn_var.get(),
                                                                                                self.id_var.get(),
                                                                                                self.firstname_var.get(),
                                                                                                self.lastname_var.get(),
                                                                                                self.address1_var.get(),
                                                                                                self.address2_var.get(),
                                                                                                self.postcode_var.get(),
                                                                                                self.mobile_var.get(),
                                                                                                self.bookid_var.get(),
                                                                                                self.booktitle_var.get(),
                                                                                                self.author_var.get(),
                                                                                                self.dateborrowed_var.get(),
                                                                                                self.datedue_var.get(),
                                                                                                self.daysonbook_var.get(),
                                                                                                self.latefine_var.get(),
                                                                                                self.dateoverdue_var.get(),
                                                                                                self.actualprice_var.get(),
                                                                                                self.prn_var.get()
                                                                                             
        ) )

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        tmsg.showinfo('Successful!', 'Member Details updated Successfully!')

    def delete_data(self):
        if self.prn_var.get()=='' or self.id_var.get()=='':
            tmsg.showerror('Error', 'First Select an entry to delete')

        else:
            conn = mysql.connector.connect(host='localhost', username='root', password= 'twarit@28', database= 'librarydb')
            my_cursor= conn.cursor()
            query= "DELETE FROM libb WHERE PRN_NO = %s"
            value= (self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            tmsg.showinfo('Successful!', 'Entry deleted Successfully!')



        


if __name__=='__main__':
    root=Tk()
    root.iconify()
    login_system(root)
    root.mainloop()
    