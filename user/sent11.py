#!C:\Python27\python.exe

import MySQLdb
import cgi, cgitb
cgitb . enable()


form = cgi.FieldStorage() 

sid = form.getvalue('sid')




#db = MySQLdb.connect("localhost","root","system","python" )
#cursor = db.cursor()


#a="select * from login_session where session_id='"+str(sid)+"'"
#print a


#v=cursor.execute(a)
#rows=cursor.fetchall()

#print "if"
#if (v==1):
	#for row in rows:
        #print row[0],"and",row[1]

#abc=368742290143

#sid=368742290143
print "Content-type:text/html\r\n\r\n"
print """

<html>
<body>
	"""
print sid

db = MySQLdb.connect("localhost","root","system","python" )
cursor = db.cursor()

a="select user_name from login_session where session_id='"+str(sid)+"'"
print a


v=cursor.execute(a)

row=cursor.fetchall()

print v
print "if"
if (a>0):
    print "for"
    for row in cursor:
        print "gdfjgsd"
        print row[0],"and"


print """
</body></html>"""
