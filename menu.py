
#menu.py --> made by simal agrahari

import mysql.connector as MSC
from datetime import date

conn= MSC.connect(host='localhost',user='root',passwd='#sag',database='bank')
cur = conn.cursor()

conn.autocommit = True

print('1.CREATE BANK ACCOUNT')
print('2.TRANSACTION')
print('3.CUSTOMER DETAILS')
print('4.TRANSACTION DETAILS')
print('5.DELETE DETAILS')
print('6.QUIT')

n=int(input('Enter your CHOICE='))

if n == 1:
    acc_no=int(input('Enter your ACCOUNT NUMBER='))
    acc_name=input('Enter your ACCOUNT NAME=')
    ph_no=int(input('Enter your PHONE NUMBER='))
    add=(input('Enter your place='))
    cr_amt=int(input('Enter your credit amount=')) 
    V_SQLInsert="INSERT INTO customer_details values (%s,%s,%s,%s,%s)" # + str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
    cur.execute(V_SQLInsert,(acc_no,acc_name,ph_no,add,cr_amt))
    print('Account Created Succesfully!!!!!')
    conn.commit()
     
if n == 2:
    acc_no=int(input('Enter Your Account Number='))
    trans = 'select * from customer_details where acct_no=%s'
    cur.execute(trans,(acc_no,)) #+str (acc_no) )
    data=cur.fetchall()
    count=cur.rowcount
    conn.commit()
    if count == 0:
        print('Account Number Invalid Sorry Try Again Later')
    else:
        print('1.WITHDRAW AMOUNT')
        print('2.ADD AMOUNT')
        x=int(input('Enter your CHOICE='))
        trans_date = date.today()
        if x == 1:
            amt=int(input('Enter withdrawl amount='))
            cur.execute('update customer_details set cr_amt=cr_amt-%s where acct_no= %s',(amt,acc_no)) #+str(amt) + ' where acct_no=' +str(acc_no) )
            cur.execute("INSERT INTO transactions (acct_no, date, withdraw_amt, amt_added) VALUES (%s, %s, %s, NULL)",(acc_no, trans_date, amt))
            conn.commit()
            print('Account Updated Succesfully!!!!!')
        if x== 2:
            amt=int(input('Enter amount to be added='))
            cur.execute('Update customer_details set cr_amt=cr_amt+%s where acct_no=%s',(amt,acc_no)) #+str(amt) + ' where acct_no='+str(acc_no) )
            cur.execute("INSERT INTO transactions (acct_no, date, withdraw_amt, amt_added) VALUES (%s, %s, NULL, %s)",(acc_no, trans_date, amt))
            conn.commit()
            print('Account Updated Succesfully!!!!!')
if n == 3:
    acc_no=int(input('Enter your account number='))
    cur.execute('select * from customer_details where acct_no=%s',(acc_no,) )
    if cur.fetchone() is None:
        print('Invalid Account number')
    else:
        cur.execute('select * from customer_details where acct_no=%s',(acc_no,) )
        data=cur.fetchall()
        for row in data:
            print('ACCOUNT NO=',acc_no)
            print('ACCOUNT NAME=',row[1])
            print('PHONE NUMBER=',row[2])
            print('ADDRESS=',row[3])
            print('cr_amt=',row[4]) 
if n== 4:
    acc_no=int(input('Enter your account number='))
    print()
    cur.execute('select * from customer_details where acct_no=%s',(acc_no,) )
    if cur.fetchone() is None:
        print()
        print('Invalid Account number')
    else:
        cur.execute('select * from transactions where acct_no=%s',(acc_no,) )
        data=cur.fetchall()
        for row in data:
            print('ACCOUNT NO=',acc_no)
            print('DATE=',row[1])
            print('WITHDRAWAL AMOUNT=',row[2])
            print('AMOUNT ADDED=',row[3])
            print()
if n == 5:
    print('DELETE YOUR ACCOUNT')
    acc_no=int(input('Enter your account number='))
    cur.execute('delete from customer_details where acct_no=%s',(acc_no,) )
    print('ACCOUNT DELETED SUCCESFULLY')
if n == 6:
    quit()

