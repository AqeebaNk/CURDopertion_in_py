# *******************Connection Setup*********************


import mysql.connector

sqldb = mysql.connector.connect( host = "localhost", user = "root", passwd = "0000", database = "sample1")


#checking the connection with try and exception
try:
    print(sqldb.connection_id)
except:
    print("connection fail")    



# installation of cursor
objcur = sqldb.cursor()

# # excuting the databases
# objcur.execute("show databases")

# for i in objcur:
#     print(i)


#********************Creating the CURD operations***********************
# note:all the steps are for one time use you once use it and comment it out 
# if you won't commit it will excute again and again.


#-------------------------Creating databases--------------------------
 
q1 = "create database sample1"
objcur.execute(q1)

# creating tables in the created database

q2 = "create table test1(id int ,name varchar(30), mobile bigint)"
objcur.execute(q2)

# Inserting Data into the table

#first method

q3 = "insert into test1 values(%s,%s,%s)"
rec1 = (1,"aqeeb",676786876)
rec2 = (2,"fatha",767678689)
rec3 = (3,"akash",656751281)

objcur.execute(q3, rec1)
objcur.execute(q3, rec2)
objcur.execute(q3, rec3)
sqldb.commit()

#second method
 
whitelist = [(4,"paroq",678672876), (5,"Javed",767678689),(6,"faizan",656751281)]
objcur.executemany(q3,whitelist)
sqldb.commit()


#-------------------------------Read Operation-----------------------

q4 = "select * from test1"
objcur.execute(q4)
res  = objcur.fetchall()
for val in res:
    print(val)

# -----------------------------Update Operation----------------------

q5 = "update test1 set mobile = 12345678 where id = 6"
objcur.execute(q5)
sqldb.commit()


# -----------------------------Delete Operation-----------------------

q6 = "delete from test1 where name = 'aqeeb'"
objcur.execute(q6)
sqldb.commit()



