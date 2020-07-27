from tkinter import *
from tkinter import messagebox,ttk
import pymysql as ms

# Add your own database name and password here to reflect in the code
mypass = "saurabh"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"  # Book Table


def View():
    class student:
        def __init__(self, root):
            self.root = root
            self.root.title("Library")
            self.root.minsize(width=400, height=400)
            self.root.geometry("1350x700+0+0")
            root.config(bg='#0099cc')
            title = Label(self.root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                          font=("algerian", 40, "bold"), bg="red", fg="white")
            title.pack(side=TOP, fill=X)

 
            # ----------------------------------------------------table frame--------------------------------------------------------------------------
            frame=Frame(self.root,bd=10,relief=GROOVE,bg='#333945')
            frame.place(x=200, y=220, width=1000, height=350)

            t_frame = Frame(frame)
            t_frame.place(x=45, y=25, width=900, height=270)

            headingFrame1 = Frame(self.root, bg="blue", bd=10, relief=GROOVE)
            headingFrame1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.13)

            headingLabel = Label(headingFrame1, text="VIEW BOOKS", bg='blue', fg='white',
                                 font=("bookman old style", 34, "bold"))
            headingLabel.place(relx=0.25, rely=0.20, relwidth=0.5, relheight=0.55)
            # back

            quitBtn = Button(root, text="Quit", bg='#d1ccc0', fg='black', font=("times new roman", 18, "bold"), bd=10,
                     relief=GROOVE, command=root.quit)
            quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

            scroll_x = Scrollbar(t_frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(t_frame, orient=VERTICAL)

            self.student_table = ttk.Treeview(t_frame,
                                                  columns=("BID", "TITLE", "SUBJECT", "AUTHOR", "STATUS"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)

            self.student_table.heading("BID", text="BID")
            self.student_table.heading("TITLE", text="TITLE")
            self.student_table.heading("SUBJECT", text="SUBJECT")
            self.student_table.heading("AUTHOR", text="AUTHOR")
            self.student_table.heading("STATUS", text="STATUS")


            self.student_table['show'] = 'headings'

            self.student_table.column("BID", width=10)
            self.student_table.column("TITLE", width=100)
            self.student_table.column("SUBJECT", width=25)
            self.student_table.column("AUTHOR", width=50)
            self.student_table.column("STATUS", width=10)

            self.student_table.pack(fill=BOTH, expand=1)
            
            self.fetch_data()


        def fetch_data(self):
            con = ms.connect(host="localhost", user="root", password="saurabh", database="library")
            cur = con.cursor()
            cur.execute("select * from books")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', END, values=row)

                con.commit()

            con.close()








    root = Tk()
    ob = student(root)
    root.mainloop()

    # ===========================================================================================================================================
