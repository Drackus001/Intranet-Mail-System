#!C:\Python27\python.exe

import cgi, cgitb
import MySQLdb
import sys
cgitb . enable()
form = cgi.FieldStorage() 

sid = form.getvalue('sid')
d=form.getvalue('num')

db = MySQLdb.connect("localhost","root","system","python" )
cursor = db.cursor()

#a="delete from login_session where session_id='"+str(sid)+"'"
if (d==str(1)):
	cursor.execute("delete from login_session where session_id='"+str(sid)+"'")
	sql = """commit"""
	cursor.execute(sql)
	
print "Content-type:text/html\r\n\r\n"
print """<html>

<body>

<fieldset style="background-color: #70eaed;">
<legend><marquee style{align:"right";}><h2>Login USER</h2></marquee></legend>
<center>
<form method="post" action="login_2.py" >
<table >




<tr><td>User name:</td><td><input type="text" name="uname" /></td></tr>
<tr><td>Password:</td><td><input type="password" name="pass" /></tr>




<tr align="center"><td colspan="2"><input type="submit" value="submit" /></td></tr>
<tr align="center"><td colspan="2"><h1><a href="registration_1.py">Register new user</a></h1></td></tr>
</table>
</form>
</center>
</fieldset>
</body>
</html>"""
print d
	
