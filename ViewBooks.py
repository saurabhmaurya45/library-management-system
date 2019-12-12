from tkinter import *

from tkinter import messagebox
import pymysql as ms

# Add your own database name and password here to reflect in the code
mypass = "saurabh"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"  # Book Table


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    title = Label(root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="violet", fg="black")
    title.pack(side=TOP, fill=X)

    same = True
    n = 0.3




    labelFrame = Frame(root, bg='black',relief=GROOVE,bd=10)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    headingFrame1 = Frame(root, bg="crimson", bd=10, relief=GROOVE)
    headingFrame1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="VIEW BOOKS",bg='crimson',fg='black',font=("bookman old style", 34, "bold") )
    headingLabel.place(relx=0.25, rely=0.20, relwidth=0.5, relheight=0.55)

    y = 0.25

    Label(labelFrame, text="%-25s%-40s%-35s%-40s%-25s" % ('BID', 'Title', 'Subject', 'Author', 'Status'),font=("times new roman", 14, "bold"), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-25s%-35s%-35s%-45s%-25s" % (i[0], i[1], i[2], i[3], i[4]), bg='black',font=("times new roman", 14, "bold"),
                  fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Bad Format", "Can't fetch files from database")

    root.mainloop()

