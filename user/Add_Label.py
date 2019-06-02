#!C:\Python27\python.exe

# Import modules for CGI handling 
import random
import base64



import cgi, cgitb
cgitb . enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
sid =base64.b64decode(form.getvalue('sid'))
no = form.getvalue('no')
ln = form.getvalue('ln')

import MySQLdb
#import sys


db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()
a="select label_name from label where no='"+str(ln)+"'"
v=cursor.execute(a)
row=cursor.fetchall()
for row in cursor:
	lname=row[0]

#first_name = "Hello"
#last_name  = "World"


cursor.execute("update mailcon set field='"+lname+"' where no='"+no+"'")
sql = """commit"""
cursor.execute(sql)
        #cursor.execute("select * from login",(uname,password))
#a="select * from user where user_id=('"+uname+"') and password=('"+password+"')"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login verification</title>"
print "</head>"
print "<body>"
print "<h4>Processing...</h4><br>"
               
print "<meta http-equiv='refresh' content='0;url=index_user.py?sid="+base64.b64encode(str(sid))+"' />"
                
print "</body>"
print "</html>"

        #cursor.execute(sql)
cursor.close()
db.close()
        #sys.exit()
