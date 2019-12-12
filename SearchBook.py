from tkinter import *

from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "saurabh"
mydatabase="library"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table
    

def search():
    
    global SearchBtn,labelFrame,lb1,en1,quitBtn,root
    
    sub = en1.get()

    SearchBtn.destroy()
    quitBtn.destroy()
    lb1.destroy()
    en1.destroy()

    same = True
    n = 0.3

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.25

    Label(labelFrame, text="%-25s%-40s%-35s%-40s%-25s" % ('BID', 'Title', 'Subject', 'Author', 'Status'),
          font=("times new roman", 14, "bold"), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame,
          text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
          bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    searchSql = "select * from "+bookTable+" where subject = '"+sub+"'"
    try:
        cur.execute(searchSql)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-25s%-35s%-35s%-45s%-25s" % (i[0], i[1], i[2], i[3], i[4]), bg='black',
                  font=("times new roman", 14, "bold"),
                  fg='white').place(relx=0.07, rely=y)
            y += 0.1
            print(i)
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(sub)
    
    quitBtn = Button(root,text=" Back",bg='#455A64', fg='white',bd=10, relief =GROOVE, font=('times new ronam',18,'bold'), command=searchBook)
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    
def searchBook():
    global lb1, en1, con, cur, bookTable, root,SearchBtn,quitBtn

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    title = Label(root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="violet", fg="black")
    title.pack(side=TOP, fill=X)

    labelFrame = Frame(root, bg='black', bd=10, relief=GROOVE)
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.3)

    headingFrame1 = Frame(root, bg="crimson", bd=10, relief=GROOVE)
    headingFrame1.place(relx=0.25, rely=0.15, relwidth=0.60, relheight=0.13)

    headingLabel = Label(headingFrame1, text="SEARCH BOOK", bg='crimson', fg='black',
                         font=("bookman old style", 34, "bold"))
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Enter Subject : ", bg='black', fg='white', font=("bookman old style", 20, "bold"))
    lb1.place(relx=0.08, rely=0.39)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.43, relwidth=0.62, relheight=0.15)

    # Submit Button
    SearchBtn = Button(root, text="SEARCH", bg='#d1ccc0', fg='black', font=("times new roman", 18, "bold"),
                       relief=GROOVE, bd=10, command=search)
    SearchBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=("times new roman", 18, "bold"), relief=GROOVE,
                     bd=10, command=root.quit)
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()
