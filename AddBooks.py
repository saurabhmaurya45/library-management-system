from tkinter import *

from tkinter import messagebox
import pymysql as ms


def bookRegister():
    bid = en1.get()
    title = en2.get()
    subject = en3.get()
    author = en4.get()
    status = en5.get()
    status = status.lower()
    
    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + subject + "','" + author + "','" + status + "')"
    try:
        print(insertBooks)
        cur.execute(insertBooks)
        print(True)

        con.commit()
        print(True)
        lb6 = Label(labelFrame, text="Successfully added book ", bg='black', fg='white',
                    font=("times new roman", 18, "bold"))
        lb6.place(relx=0.3, rely=0.85)
        # messagebox.showinfo('Success','Successfully added book')
   
    except:
        lb6 = Label(labelFrame, text="Book addition failed    ", bg='black', fg='white',
                    font=("times new roman", 18, "bold"))
        lb6.place(relx=0.3, rely=0.85)
        #messagebox.showinfo("Error", "Can't insert book")

    print(bid)
    print(title)
    print(subject)
    print(author)
    print(status)

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)


def addBooks():
    global en1, en2, en3, en4, en5, con, cur, bookTable, root,labelFrame

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    root.config(bg='#0099cc')
    title = Label(root, text="Welcome to Sterling's Library", bd=15, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="red", fg="white")
    title.pack(side=TOP, fill=X)

    # Add your own database name and password here to reflect in the code
    mypass = "saurabh"
    mydatabase = "library"

    con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    same=True
    n=0.3

    labelFrame = Frame(root, bg='#333945',bd=10, relief=GROOVE)
    labelFrame.place(relx=0.15, rely=0.15, relwidth=0.75, relheight=0.65)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white',font=("times new roman", 18, "bold"))
    lb1.place(relx=0.05, rely=0.1)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.12, relwidth=0.60,relheight=0.05)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white',font=("times new roman", 18, "bold"))
    lb2.place(relx=0.05, rely=0.25)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3, rely=0.25, relwidth=0.60,  relheight=0.05)

    # Book Subject
    lb3 = Label(labelFrame, text="Subject : ", bg='black', fg='white',font=("times new roman", 18, "bold"))
    lb3.place(relx=0.05, rely=0.4)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3, rely=0.4, relwidth=0.60,relheight=0.05)

    # Book Author
    lb4 = Label(labelFrame, text="Author : ", bg='black', fg='white',font=("times new roman", 18, "bold"))
    lb4.place(relx=0.05, rely=0.55)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3, rely=0.55, relwidth=0.60,relheight=0.05)

    # Book Status
    lb5 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white',font=("times new roman", 18, "bold"))
    lb5.place(relx=0.05, rely=0.69)

    en5 = Entry(labelFrame)
    en5.place(relx=0.3, rely=0.70, relwidth=0.60,relheight=0.05)

    # Submit Button
    SubmitBtn = Button(root,text="SUBMIT", bg='#d1ccc0', fg='black',font=("times new roman", 18, "bold"),bd=10,relief=GROOVE, command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='#f7f1e3', fg='black',font=("times new roman", 18, "bold"),bd=10,relief=GROOVE,command = root.quit)
    quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()

