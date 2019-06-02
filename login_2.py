#!C:\Python27\python.exe

# Import modules for CGI handling 
import random
import base64


import cgi, cgitb
cgitb . enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
uname = form.getvalue('uname')
password = form.getvalue('pass')
stu=0

#uname=uname+"@imail.py"
#first_name = "Hello"
#last_name  = "World"
if(uname is None):
        uname="NULL"
if(password is None):
        password="NULL"
import MySQLdb
#import sys


db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()
        #cursor.execute("select * from login",(uname,password))
#a="select * from user where user_id=('"+uname+"') and password=('"+password+"')"
v=cursor.execute("select * from user where user_id=%s && password=%s",(uname,password))
#a= "select Account_type from user where user_id=%s",(uname)
        #v="""cursor.execute("select * from login where user_name=%s && password=%s",(uname,password))"""
#row=cursor.fetchall()
        #\cursor.execute(v)
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login verification</title>"
print "</head>"
print "<body>"
cursor.execute("select Account_type,status from user where user_id=('"+uname+"') and Password=('"+base64.b64encode(password)+"')")
row=cursor.fetchone()
for row in cursor:
        acc=row[0]
        stu=row[1]
                
                
if(stu==1):
        for row in cursor:
                sid=random.randrange(100000000000,999999999999)
                print "<h4>Processing...</h4><br>"
                cursor.execute("delete from session where User_id=('"+uname+"')")
                cursor.execute("commit")
                cursor.execute("insert into session values(%s,%s)",(sid,uname))
                cursor.execute("commit")
                #print sid
                #print account
                if(acc=='admin'):
                        print "<meta http-equiv='refresh' content='0;url=ADMIN/index_admin.py?sid="+base64.b64encode(str(sid))+"' />"
                else:
                        print "<meta http-equiv='refresh' content='0;url=user/index_user.py?sid="+base64.b64encode(str(sid))+"' />"
                #print "<a href='index_admin.py?sid="+str(sid)+"'>Inbox</a>"
else:
        print """<meta http-equiv='refresh' content='0;url=index.py' />
     		   </body>
     		   
     		   <script type="text/javascript">
				if (confirm("Invalid Username and Password!") == true) {
        		
    			
    		}    
    
				</script>
				
				"""

#print """<a href="sent.html">sent mail</a> """
#print "<input type="""""
#print "Location: sent.html\n"


print "</html>"

        #cursor.execute(sql)
cursor.close()
db.close()
        #sys.exit()
