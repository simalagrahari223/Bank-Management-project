#SAG
#bank management project by SIMAL AGRAHARI


import mysql.connector as MSC
conn=MSC.connect(host='localhost',user='root',passwd="#sag",database='bank')
cur = conn.cursor()

#cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print()
print("#"*27," WELCOME TO SAG's BANK ","#"*27)
print()
print('1.REGISTER')
print('2.LOGIN')

n=int(input('enter your choice='))

if n== 1:
    name=input('Enter a Username=')
    passwd=int(input('Enter a 4 DIGIT Password='))
    V_SQLInsert="INSERT INTO user_table (passwrd,username) values (%s,%s)" #+ str (passwd) + ",' " + name + " ') "
    cur.execute(V_SQLInsert,(passwd,name))
    conn.commit()
    print('USER created succesfully')
    
if n==2 :
    name=input('Enter your Username=')
    passwd=int(input('Enter your 4 DIGIT Password='))
    V_Sql_Sel="select * from user_table where passwrd=%s and username=%s" #+str (passwd)+"' and username= ' " +name+ " ' "
    cur.execute(V_Sql_Sel,(passwd,name))
    if cur.fetchone() is None:
        print('Invalid username or password')
    else:
        import menu
