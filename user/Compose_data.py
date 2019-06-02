#!C:\Python27\python.exe

# Import modules for CGI handling 
import time
import cgi, cgitb
cgitb . enable()
form = cgi.FieldStorage()

to = form.getvalue('rn')
subject = form.getvalue('subject')
message = form.getvalue('message')
time=time.strftime("%c")
sid = form.getvalue('sid')


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title></title>"
print "</head>"
print "<body>"
print "<h2>sent Imail</h2>"
print "<a href='index_student.py?sid="+str(sid)+"'>home</a>"
#print to
#print message
print "</body>"
print "</html>"

import MySQLdb
db = MySQLdb.connect("localhost","root","system","python" )
cursor = db.cursor()
print sid
#print "select user_name from login_session where session_id=("%s")",(sid)
a="select user_name from login_session where session_id='"+str(sid)+"'"
#a="select user_name from login_session where session_id='343112381485'"

#print cursor.execute("select user_name from login_session where session_id='"+str(sid)+"'")
v=cursor.execute(a)
row=cursor.fetchall()
#print a
#print v
#print "if"
if (a>0):
    print "for"
    for row in cursor:
        sname=row[0]
        print sname


cursor.execute("INSERT INTO mailcon values ('"+message+"','"+sname+"','"+to+"','"+subject+"','"+time+"')")
#cursor.execute("INSERT INTO mailcon values (%s,%s,%s,%s,%s)",(message,sname,to,subject,time))
      
sql = """commit"""
cursor.execute(sql)
#cursor.execute(sql)

db.close()