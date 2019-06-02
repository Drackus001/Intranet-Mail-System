#!C:\Python27\python.exe
import time
import base64             
import cgi, cgitb
cgitb . enable()
form = cgi.FieldStorage() 
sid =base64.b64decode(form.getvalue('sid'))

no =form.getvalue('no')

time=time.strftime("%c")
 


to = form.getvalue('rn')

message = form.getvalue('message')
reply = form.getvalue('reply')
gr = form.getvalue('gr')
greply = form.getvalue('greply')


import MySQLdb
import sys
db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()
print "Content-type:text/html"
print """
<html>
<head>"""
a="select user_id from session where session_id='"+str(sid)+"'"
v=cursor.execute(a)
row=cursor.fetchall()
if(v==0):
	print "<meta http-equiv='refresh' content='0;url=../index.py' />"
for row in cursor:
	sname=row[0]


	
	
n=cursor.execute("select * from mailcon where rname like ('%"+sname+"%')")
if(gr==str(1)):
	minfo=cursor.execute("select * from group_mail where gm_no=('"+str(no)+"')")
else:
	minfo=cursor.execute("select * from mailcon where no=('"+str(no)+"')")

print """

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Reply Mail.</title>

    <!-- BOOTSTRAP STYLES-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FONTAWESOME STYLES-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
    <!-- PAGE LEVEL STYLES -->
    <link href="assets/css/prettyPhoto.css" rel="stylesheet" />
    <!--CUSTOM BASIC STYLES-->
    <link href="assets/css/basic.css" rel="stylesheet" />
    <!--CUSTOM MAIN STYLES-->
    <link href="assets/css/custom.css" rel="stylesheet" />
    <!-- GOOGLE FONTS-->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />"""
if (reply==str(1)):
	cursor.execute("select * from mailcon where no='"+str(no)+"'")
	row=cursor.fetchall()
	for row in cursor:
		subject=row[2]
		field=row[4]
	cursor.execute("INSERT INTO mailcon (message,sub,rname,field,date,sname,status) values  ('"+base64.b64encode(message)+"','"+subject+"','"+to+"','"+field+"','"+time+"','"+sname+"','"+str(0)+"')")
	sql = """commit"""
	print "<meta http-equiv='refresh' content='0;url=inbox.py?sid="+base64.b64encode(str(sid))+"' />"
	cursor.execute(sql)
if (greply==str(1)):
	cursor.execute("select * from group_mail where gm_no='"+str(no)+"'")
	row=cursor.fetchall()
	for row in cursor:
		gn=row[1]
		subject=row[3]
		rname=row[4]
	cursor.execute("INSERT INTO group_mail (Group_no,message,sub,rname,date,sname) values  ('"+str(gn)+"','"+base64.b64encode(message)+"','"+subject+"','"+rname+"','"+time+"','"+sname+"')")
	sql = """commit"""
	print "<meta http-equiv='refresh' content='0;url=group.py?sid="+base64.b64encode(str(sid))+"' />"
	cursor.execute(sql)

print"""</head>

<body>
    <div id="wrapper">
        <nav class="navbar navbar-default navbar-cls-top " role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" >Intranet Mail System</a>
            </div>

            <div class="header-right">"""

 
            


print """          </div>
        </nav>
        <!-- /. NAV TOP  -->
        <nav class="navbar-default navbar-side" role="navigation">
            <div class="sidebar-collapse">
                <ul class="nav" id="main-menu">
                    <li>
                        <div class="user-img-div">
                            <img src="assets/img/user.png" class="img-thumbnail" />
<div class="inner-text">"""
print sname
print """       
                       </div>
                        </div>

                    </li>


 <li>"""
print "<a class='active-menu' href='index_admin.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-ge'></i>Dashboard</a>"
print "</li><li>"      
print "<a href='inbox.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Inbox</a>"
print "</li><li>"
print "<a href='Compose.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Compose</a>"
print "</li><li>"
print "<a href='sentmail.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Sent Mail</a>"
print "</li><li>"
print "<a href='Label.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-archive'></i>Label</a>"
print "</li><li>"
print "<a href='Group.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-group'></i>Group</a>"
print "<a href='draft.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Draft</a>"
print "</li><li>"
print "<a href='dmail.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-recycle'></i>Recycle Now!</a>"
print "</li><li>" 
print "<a href='logout.py?sid="+base64.b64encode(str(sid))+"&num="+base64.b64encode(str(1))+"'><i class='fa fa-sign-out'></i>Logout</a>"
print """                    </li>
                      
            </div>


        </nav>
        <!-- /. NAV SIDE  -->
        <div id="page-wrapper">
            <div id="page-inner">
                <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-head-line">reply Mail.</h1>
                

                    <div class="col-md-8">

                        <div class="table-responsive">
            <form method="get" action="reply.py">
                            <table class="table table-striped table-bordered table-hover">
                                


"""


row=cursor.fetchall()
i=0
if(gr==str(1)):
	for row in cursor:
		i=i+1
		no=row[0]
		print "<tr><td colspan='2'>"
		print "<textarea style='margin: 0px; height: 346px; width: 953px;' name='message'>Previous mail info:-"
		print "Sender ID:-",row[6]
		print "Subject:- ",row[3]
		print "Message:- ",base64.b64decode(row[2])
		print "Time: ",row[5]
		print "message of reply mail=></textarea></td></tr>"
		print "<input type='text' name='sid' value='"+base64.b64encode(str(sid))+"' hidden/><input type='text' name='greply' value='"+str(1)+"' hidden/><input type='text' name='no' value='",row[0],"' hidden/>"
else:
	for row in cursor:
		i=i+1
		no=row[0]
		print "<tr align='center'><td>to:- </td><td><input type='text' name='rn' value='",row[6],"'/></td></tr>"
		print "<tr><td colspan='2'>"
		print "<textarea style='margin: 0px; height: 346px; width: 953px;' name='message'>Previous mail info:-"
		print "Sender ID:-",row[6]
		print "Subject:- ",row[2]
		print "Message:- ",base64.b64decode(row[1])
		print "Time: ",row[5]
		print "message of reply mail=></textarea></td></tr>"
		print "<input type='text' name='sid' value='"+base64.b64encode(str(sid))+"' hidden/><input type='text' name='reply' value='"+str(1)+"' hidden/><input type='text' name='no' value='",row[0],"' hidden/>"
	
	
#<a href='reply.py?sid="+str(sid)+"&no="+str(no)+"'></a>
print "<tr align='center'><td colspan='2'><button type='submit' class='btn btn-danger'>Send</button>"
print """
         </td></tr>  




                         
                                </tbody>
                            </table>
                            </form>
                        </div>




                    </div>
                    
                
                <!--/.Row-->
                        

                    </div>
                </div>
                
                   <!-- /. ROW  -->
                <div id="port-folio">
                      <div class="row " >
                     
               
               


            </div>

            <div class="row " style="padding-top: 50px;">
                
                


            </div>
                    <div class="row "  style="padding-top: 50px;" >
                
                

            </div>
                </div>
                              
             </div></div>
    <!-- /. WRAPPER  -->
    <div id="footer-sec">
        &copy; 2016-17 <b>I</b>NTRANET <b>M</b>AIL <b>S</b>ystem | Design By : unKnOwN$</a>
    </div>
    <!-- /. FOOTER  -->
    <!-- SCRIPTS -AT THE BOTOM TO REDUCE THE LOAD TIME-->
    <!-- JQUERY SCRIPTS -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!-- BOOTSTRAP SCRIPTS -->
    <script src="assets/js/bootstrap.js"></script>
     <!-- PAGE LEVEL SCRIPTS -->
    <script src="assets/js/jquery.prettyPhoto.js"></script>
    <script src="assets/js/jquery.mixitup.min.js"></script>
    <!-- METISMENU SCRIPTS -->
    <script src="assets/js/jquery.metisMenu.js"></script>
    <!-- CUSTOM SCRIPTS -->
    <script src="assets/js/custom.js"></script>
     <!-- CUSTOM Gallery Call SCRIPTS -->
    <script src="assets/js/galleryCustom.js"></script>
</body>
</html>
"""






