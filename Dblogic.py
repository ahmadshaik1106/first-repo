

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="ahmad" ,database= "database")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

rows = mycursor.fetchall()

mycursor.close()
mydb.close()

lst=[]
for row in rows:
    lst.append(row[0])
print(lst)

rollno=input("Enter Roll Number:")

def something():
    counter = 0
    for row in rows:
        count = 0
        if count==1:
            break
        else:
            for row in rows:
                if (row[0]==rollno or row[0]==rollno.upper()) and counter<1:
                    count+=1
                    counter+=1
                    print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    break

        if count==0 and counter==0:
            print('Nothing over here like',rollno)
            break
something()

