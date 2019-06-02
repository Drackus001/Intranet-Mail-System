#!C:\Python27\python.exe

import cgi, cgitb
cgitb . enable()


form = cgi.FieldStorage() 
sid = form.getvalue('sid')
import MySQLdb
import sys
db = MySQLdb.connect("localhost","root","system","python" )
cursor = db.cursor()
a="select user_name from login_session where session_id='"+str(sid)+"'"
v=cursor.execute(a)
row=cursor.fetchall()
for row in cursor:
	sname=row[0]

print "Content-type:text/html"

print """
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Inbox</title>

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
                <a class="navbar-brand" href="index_student.py">Intranet Mail System</a>
            </div>

            <div class="header-right">

 
            

          </div>
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
print "<a class='active-menu' href='index_faculty.py?sid="+str(sid)+"'><i class='fa fa-ge'></i>Dashboard</a>"
print "</li><li>"
print "<a href='AddAccount.py?sid="+str(sid)+"'><i class='fa fa-plus-circle'></i>Add Account</a>"
print "</li><li>"
print "<a href='Profile.py?sid="+str(sid)+"'><i class='fa fa-user'></i>Profile</a>"
print "</li><li>"
print "<a href='Compose.py?sid="+str(sid)+"'><i class='fa fa-send-o'></i>Compose</a>"
print "</li><li>"
print "<a  href='inbox.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Inbox</a>"                       
print "</li><li>"
print "<a href='SentMail.py?sid="+str(sid)+"'><i class='fa fa-send'></i>Sent Mail</a>"
print "</li><li>"
print "<a href='forwardmail.py?sid="+str(sid)+"'><i class='fa fa-forward'></i>Forward Mail</a>"
print "</li><li>"
print "<a href='replaymail.py?sid="+str(sid)+"'><i class='fa fa-reply'></i>Replay Mail</a>"
print "</li><li>"
print "<a href='Group.py?sid="+str(sid)+"'><i class='fa fa-group'></i>Group</a>"
print "</li><li>"     
print "<a href='Label.py?sid="+str(sid)+"'><i class='fa fa-archive'></i>Label</a>"
print "</li><li>"   
print "<a href='Search.py?sid="+str(sid)+"'><i class='fa fa-search'></i>Search</a>"
print "</li><li>"
print "<a href='draft.py?sid="+str(sid)+"'><i class='fa fa-dropbox'></i>Draft</a>"
print "</li><li>"
print "<a href='login_1.py?sid="+str(sid)+"&num="+str(1)+"'><i class='fa fa-sign-out'></i>Logout</a>"
print """                    </li>
                      
            </div>


        </nav>
        <!-- /. NAV SIDE  -->
        <div id="page-wrapper">
            <div id="page-inner">
                <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-head-line">compose</h1>
                

                    <div class="col-md-8">

                        <div class="table-responsive">
                        <form method="get" action="compose_data.py">
                            <table class="table table-striped table-bordered table-hover">
                                <tr align="center">
<td colspan="2">
--Send mail--
</h2></th></tr><br><br>

<tr align="center"><td>to:</td> <td><input type="text" name="rn"/></td></tr>
<tr align="center"><td>subject:</td><td><input type="text" name="subject"/></td></tr>
<tr ><td>message:</td><td><textarea name="message" cols="50" rows="10"></textarea></td></tr>
"""
print '<input type="hidden" name="sid" value="%s"/>' %(sid)
print""" 
<tr  align="center"><td colspan="2"><input type="submit" /></td></tr>                               <tbody>
                                

           




                         
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






