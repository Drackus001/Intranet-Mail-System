#!C:\Python27\python.exe
import time
import base64
import cgi, cgitb
cgitb . enable()

form = cgi.FieldStorage()
sid =base64.b64decode(form.getvalue('sid'))
dd=form.getvalue('num')
ln = form.getvalue('ln')

time=time.strftime("%c")

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
	

val=0

	
n=cursor.execute("select * from mailcon where  rname=('"+sname+"')")	

print """


    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>New Label</title>

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
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
</head>
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

            <div class="header-right">
"""
             
                
if (dd==str(1)):
	if (ln):
		cursor.execute("INSERT INTO label (label_name,user_id,date) values  ('"+ln+"','"+sname+"','"+time+"')")
		sql = """commit"""
		cursor.execute(sql)
		print "<meta http-equiv='refresh' content='0;url=label.py?sid="+base64.b64encode(str(sid))+"' />"
	else:
		val=1
	

print """         </div>
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
print """                                    
                        </li>
                      
            </div>

        </nav>
        <!-- /. NAV SIDE  -->

        <div id="page-wrapper">
            <div id="page-inner">
                <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-head-line">New Label</h1>
                        
<div class="col-md-6 col-sm-6 col-xs-12"><div class="panel panel-danger">
                        <div class="panel-heading">
                           Label Registration"""
if(val==1):
	print"<h1 style='color:#e30000'>Enter Label name.</h1>"
print"""                       </div>
                        <div class="panel-body">
                            <form role="form" method="post" action="new_label.py">
                                        
                                 <div class="form-group">
                                            <label>Label name:</label>
                                            <input class="form-control" type="text" name="ln" placeholder="Enter Your Label Name.">
                                            """
print"<input type='text' name='num' value='"+str(1)+"' hidden/><input type='text' name='sid' value='"+base64.b64encode(str(sid))+"' hidden/>"
                                    
                                            
                                            
                                   
print""" </div>"""
                                 
                                      
print "<button type='submit' class='btn btn-danger'>Register </button>"
#print "<a href='login_1.py?sid="+str(sid)+"&num="+str(1)+"'><i class='fa fa-sign-out'></i>Logout</a>"
print"""                                    </form>
                            </div>
                        </div>
                            </div>


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
