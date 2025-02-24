#table.py->>made by simal agrahari

import mysql.connector as MSC
mydb = MSC.connect(host="localhost" ,user="root" ,passwd="#sag",database="bank")
print(mydb)
mycur = mydb.cursor()
mycur.execute("Show tables")
for i in mycur:
    print(i)

#mycur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float)')


