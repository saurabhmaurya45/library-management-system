import pymysql as ms

mypass = "root"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
mycursor = con.cursor()
#creating database
mycursor.execute('create database library')

 #creating login table

mycursor.execute('create table login(login_id int(6) not null primary key,name varchar(255) not null,password varchar(255) not null)')

#create table issue
mycursor.execute('create table issue(book_id int(10) primary key,stu_id int(10) not null, stu_name varchar(255) not null, class int(4) not null, issued_from varchar(25) not null, issued_to varchar(25) not null ,submition_date varchar(25))')

#create table book

mycursor.execute('create table books(Book_Id int(6) primary key not null,title varchar(255) not null,subject varchar(255) not null, author varchar(255),status varchar(255)')

