#!C:\Python27\python.exe

import cgi, cgitb
import base64
import MySQLdb
import sys
cgitb . enable()
form = cgi.FieldStorage() 

sid = base64.b64decode(form.getvalue('sid'))
d=base64.b64decode(form.getvalue('num'))


db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()

#a="delete from login_session where session_id='"+str(sid)+"'"

	
print "Content-type:text/html\r\n\r\n"
print """<html>

"""
if (d==str(1)):
	cursor.execute("delete from session where session_id='"+str(sid)+"'")
	sql = """commit"""
	cursor.execute(sql)
	print "<meta http-equiv='refresh' content='0;url=../index.py' />"
print """
<body>
</body>
</html>
"""
