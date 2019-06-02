#!C:\Python27\python.exe
# Import modules for CGI handling 
import cgi, cgitb
cgitb . enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
error = form.getvalue('error')
password = form.getvalue('pass')
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>login verification</title>"
print "</head>"
print "<body><center><h3>"
print error
print "</h3></center></body>"
print "</html>"
