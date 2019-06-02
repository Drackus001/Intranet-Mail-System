#!C:\Python27\python.exe
import exceptions
import cgi, cgitb
import MySQLdb
import sys
cgitb . enable()
form = cgi.FieldStorage() 
sid = form.getvalue('sid')
d=form.getvalue('num')

db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()

try:
        
        #a="delete from login_session where session_id='"+str(sid)+"'"

                
        print "Content-type:text/html\r\n\r\n"
        print """<html>
        <head>
        """
        if (d==str(1)):
                cursor.execute("delete from session where session_id='"+str(sid)+"'")
                sql = """commit"""
                cursor.execute(sql)
                print "<meta http-equiv='refresh' content='0;url=login_1.py' />"
        print"""
        </head>

        <body>

        <fieldset style="background-color: #70eaed;">
        <legend><marquee style{align:"right";}><h2>Login USER</h2></marquee></legend>
        <center>
        <form method="get" action="login_2.py" >
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
except urllib.error.HTTPError: 
    print "Image fetch failed."

	
