#!C:\Python27\python.exe

import cgi, cgitb
cgitb . enable()


form = cgi.FieldStorage() 

sid = form.getvalue('sid')




print "Content-type:text/html\r\n\r\n"
print """

<html>
<body>
	"""
print sid


print """

<center>
<form method="get" action="send2.py">
<table border="0">
<tr align="center">
<td colspan="2">
--Send mail--
</h2></th></tr><br><br>

<tr align="center"><td>to:</td> <td><input type="text" name="rn"/></td></tr>
<tr align="center"><td>subject:</td><td><input type="text" name="subject"/></td></tr>
<tr ><td>message:</td><td><textarea name="message" cols="50" rows="10"></textarea></td></tr>
"""
print '<tr align="center"><td></td><td><input type="hidden" name="sid" value="%s"/></td></tr>' %(sid)
print """
<tr ><td><input type="submit" /></td></tr>

"""
#print "<a href='send2.py?sid="+str(sid)+"'>send mail</a>"

print """</table>
</form>
</center>
</body>
</html>"""
