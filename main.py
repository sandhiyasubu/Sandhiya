import sqlite3
con=sqlite3.connect('user.db')
con.execute("create table users(STUDENT NAME,MARK,AVERAGE,TOTAL,GRADE);")
def insertData(student name,mark,average,total,grade):
    qry=f'insert into users (STUDENT NAME,MARK,AVERAGE,TOTAL,GRADE) values ("{student name}","{mark}","{average}","{total}","{grade}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(student name):
    qry='select * from users where student name="student name";'
    result=con.execute(qry)
    print("student name \t mark \t average \ttotal \t grade")
    for row in result:
        print("|\t    ".join(row))
def display():
    qry='select * from users;'
    result=con.execute(qry)
    print("student name\t mark \t average \t total \t grade")
    for row in result:
        print("|\t    ".join(row))

print("1.Insert Data \n2.search Actor \n3.display all")
ch="y"
while(ch.lower()=='y'):
    c=int(input())
    if(c==1):
        print("add record")
       student name=input("Enter the name of the student:")
        mark=input("Enter the name of the mark:")
        average=input("Enter the name of the average")
        total=input("Enter the name of the total")
        grade=input("Enter the year of grade")
        insertData(student name,mark,average,total,grade)
    elif (c==2):
        print("select")
        select(input("student name:"))
    elif(c==3):
        display()
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")
