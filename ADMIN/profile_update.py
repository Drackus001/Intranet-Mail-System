#!C:\Python27\python.exe
import time
import base64
import cgi, cgitb
cgitb . enable()

form = cgi.FieldStorage()
sid = base64.b64decode(form.getvalue('sid'))
fn=form.getvalue('fn')
ln = form.getvalue('ln')
dob = form.getvalue('dob')
em = form.getvalue('em')
mob = form.getvalue('mob')
degi = form.getvalue('degi')
id_no = form.getvalue('id_no')
g = form.getvalue('g')

import MySQLdb
import sys
db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()

a="select user_id from session where session_id='"+str(sid)+"'"
v=cursor.execute(a)
row=cursor.fetchall()

for row in cursor:
	sname=row[0]
	
#n=cursor.execute("select * from mailcon where rname=('%"+sname+"%')")	









#a="delete from login_session where session_id='"+str(sid)+"'"

cursor.execute ("UPDATE user set First_name=%s, Last_name=%s, Gender=%s, Email_addr=%s, bdate=%s, id_no=%s, Designation=%s, Mobile_no=%s  WHERE User_id=%s ", (fn,ln,g,em,dob,id_no,degi,mob,sname))
#cursor.execute("INSERT INTO mailcon (message,sub,rname,field,replay,date,sname) values  ('"+message+"','"+subject+"','"+to+"','"+field+"','"+str(0)+"','"+time+"','"+sname+"')")
sql = """commit"""
cursor.execute(sql)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login verification</title>"
print "</head>"
print "<body>"
print "<meta http-equiv='refresh' content='0;url=Profile.py?sid="+base64.b64encode(str(sid))+"' />"
print "</body>"
print "</html>"
