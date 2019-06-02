#!C:\Python27\python.exe

# Import modules for CGI handling 
import random



import cgi, cgitb
cgitb . enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
uname = form.getvalue('uname')
password = form.getvalue('pass')


#first_name = "Hello"
#last_name  = "World"

import MySQLdb
#import sys

db = MySQLdb.connect("localhost","root","system","python" )
cursor = db.cursor()
#cursor.execute("select * from login",(uname,password))
v=cursor.execute("select * from registration where user_name=%s && password=%s",(uname,password))

#v="""cursor.execute("select * from login where user_name=%s && password=%s",(uname,password))"""
row=cursor.fetchall()
#\cursor.execute(v)
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login</title>"
print "</head>"
print "<body>"
#v=10	
if(v==1):
	for row in cursor:
		sid=random.randrange(100000000000,999999999999)
		print "sucessful login",row[5], row[6],"<br>"
		cursor.execute("insert into login_session values(%s,%s)",(sid,uname))
		cursor.execute("commit")
		print sid
		print "<a href='send1.py?sid="+str(sid)+"'>send mail</a>"
		print "<a href='index_Faculty.py?sid="+str(sid)+"'>Inbox</a>"
#else
#	print "Login failed"


#print """<a href="sent.html">sent mail</a> """
#print "<input type="""""
#print "Location: sent.html\n"
print "</body>"
print "</html>"

#cursor.execute(sql)
cursor.close()
db.close()
#sys.exit()
