from SearchBook import *
from menu import *

# Add your own database name and password here to reflect in the code
mypass = "saurabh"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("1350x700+0+0")
title = Label(root, text="Welcome to Sterling's Library", bd=15, relief=GROOVE,
              font=("algerian", 40, "bold"), bg="yellow", fg="white")
title.pack(side=TOP, fill=X)

'''
MAIN PAGE
'''
'''
checking login
'''


def gettingLoginDetails():
    global login, password, getpassword, en1, en2

    login = int(en1.get())
    password = en2.get()

    sqlLoginID = "select login_Id from login where password = '" + password + "'"
    sqlpassword = "select password from login where password = '" + password + "'"

    try:
        cur.execute(sqlLoginID)
        for i in cur:
            getLoginID = i[0]

        cur.execute(sqlpassword)
        for i in cur:
            getpassword = i[0]

        if (getLoginID == login and getpassword == password):
            messagebox.showinfo("SUCCESS", "Login successful, Welcome to MENU Page")
            en1.delete(0, END)
            en2.delete(0, END)
            empMenu()

        else:
            messagebox.showerror("Failure", "Can't log in, check your credentials")
    except:
        messagebox.showinfo("FAILED", "Please check your credentials")

    print(login)
    print(password)


same=True
n=0.3

labelFrame = Frame(root, bd=10, bg='#333945', relief=GROOVE)
labelFrame.place(relx=0.1, rely=0.2, relwidth=0.35, relheight=0.5)

title = Label(labelFrame, text='Librarian Login', bg='#333945', fg='white',
              font=('bookman old style', 30, 'bold', 'italic'))
title.place(relx=0.15, rely=0.05)

# Login ID

lb1 = Label(labelFrame, text="Login ID : ", bg='#333945', fg='white', font=('bookman old style', 20, 'bold'))
lb1.place(relx=0.05, rely=0.30)

en1 = Entry(labelFrame)
en1.place(relx=0.42, rely=0.33, relwidth=0.35, relheight=0.060)

# Password
lb2 = Label(labelFrame, text="Password : ", bg='#333945', fg='white', font=('bookman old style', 20, 'bold'))
lb2.place(relx=0.05, rely=0.55)

en2 = Entry(labelFrame)
en2.place(relx=0.42, rely=0.57, relwidth=0.35, relheight=0.060)

# Submit Button
SubmitBtn = Button(labelFrame, text="LOGIN", bg='#d1ccc0', fg='black',bd=10,relief=GROOVE, font=('times new roman', 17, 'bold'),
                   command=gettingLoginDetails)
SubmitBtn.place(relx=0.42, rely=0.75, relwidth=0.3, relheight=0.15)

# search

labelFrame1 = Frame(root, bd=10, bg='#333945', relief=GROOVE)
labelFrame1.place(relx=0.55, rely=0.2, relwidth=0.35, relheight=0.5)

lb1 = Label(labelFrame1, text="To see the available book ", bg='#333945', fg='white', font=('bookman old style', 20, 'bold'))
lb1.place(relx=0.05, rely=0.30)

click = Button(labelFrame1, text="CLICK HERE", bg='#d1ccc0', fg='black', font=("times new roman", 18, "bold"), bd=10,
                   relief=GROOVE, command=View)
click.place(relx=0.3, rely=0.55, relwidth=0.45, relheight=0.2)


# search
labelFrame3 = Frame(root,bd=6 ,bg='#333945', relief=RIDGE)
labelFrame3.place(relx=0.1, rely=0.72, relwidth=0.8, relheight=0.25)

search=Label(labelFrame3, text='Disclaimer',bg ='#333945', fg='white', font=('bookman old style',20,'bold',))
search.place(relx=0.4, rely=0.1)








root.mainloop()
