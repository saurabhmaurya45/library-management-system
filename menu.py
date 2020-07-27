
from ViewBooks import *
from AddBooks import *
from IssueBook import *
from DeleteBook import *
from SearchBook import *



def empMenu():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    root.config(bg='#0099cc')
    title = Label(root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="red", fg="white")
    title.pack(side=TOP, fill=X)

    mycursor ='saurabh'

    headingFrame1 = Frame(root, bg="blue", bd=10, relief=GROOVE)
    headingFrame1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="blue")
    headingFrame2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="MENU",bg='blue', fg='white', font=("bookman old style", 36, "bold"))
    headingLabel.place(relx=0.25, rely=0.20, relwidth=0.5, relheight=0.55)

    headingFrame3=Label(root,text="User:"+mycursor+"",fg='green',font=("bookman old style", 18, "bold"))
    headingFrame3.place(relx=0.85, rely=0.12)

    btn1 = Button(root, text="Add Book Details", bg='black', fg='white',relief=GROOVE,bd=5,font=("times new roman", 18, "bold"), command=addBooks)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white',relief=GROOVE,bd=5,font=("times new roman", 18, "bold"), command=delete)
    btn2.place(relx=0.28, rely=0.41, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Book List", bg='black', fg='white',relief=GROOVE,bd=5,font=("times new roman", 18, "bold"), command=View)
    btn3.place(relx=0.28, rely=0.52, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Search Book", bg='black', fg='white',relief=GROOVE,bd=5,font=("times new roman", 18, "bold"), command=searchBook)
    btn4.place(relx=0.28, rely=0.63, relwidth=0.45, relheight=0.1)

    btn5 = Button(root, text="Issue/Submit  Book  to/from  Student", bg='black', fg='white',relief=GROOVE,bd=5,font=("times new roman", 18, "bold"), command=issuebooks)
    btn5.place(relx=0.28, rely=0.74, relwidth=0.45, relheight=0.1)
    

    root.mainloop()





