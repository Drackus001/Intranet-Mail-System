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

n=cursor.execute("select * from mailcon where sname=('"+sname+"') or rname=('"+sname+"')")	
print "Content-type:text/html"
print """
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Add Account</title>

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
                <a class="navbar-brand" href="index.html">Intranet Mail System</a>
            </div>

            <div class="header-right">
"""
print '<a href="message-task.py" class="btn btn-info" title="New Message"><b>%s</b><i class="fa fa-envelope-o fa-2x"></i></a>' %(n)             
                


print """            </div>
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
print """                            </div>
                        </div>
                    </li>
<li>
 """
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
print """                   </li>
            </div>

        </nav>
        <!-- /. NAV SIDE  -->

        <div id="page-wrapper">
            <div id="page-inner">
                <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-head-line">Add Account</h1>
                        
<div class="col-md-6 col-sm-6 col-xs-12"><div class="panel panel-danger">
                        <div class="panel-heading">
                           Registration Form
                        </div>
                        <div class="panel-body">
                            <form role="form">
                                        
                                 <div class="form-group">
                                            <label>First name:</label>
                                            <input class="form-control" type="text" name="fn" placeholder="Enter Your First Name.">
                                            <label>last Name:</label>
                                            <input class="form-control" type="text" name="ln" placeholder="Enter Your Last Name.">
                                    
                                    		<label>Id.:</label>
                                            <input class="form-control" type="number" name="id" placeholder="Enter Your Id Number.">
                                    
                                    		<label>Dept name:</label>
                                            <input class="form-control" type="text" name="dn" placeholder="Enter Your Department Name.">
                                    
                                    		<label>M no:</label>
                                            <input class="form-control" type="number" name="mn" placeholder="Enter Your Mobile Number.">
                                    		<label>Account type:</label><br>
                                   <label> Faculty: <input type="radio"    name="r" value="Faculty"/>     Student: <input type="radio" value="Student" name="r"/></td></tr></label><br>
                                    
                                   
                                            <label>User Name:</label>
                                            <input class="form-control" type="text" name="un" placeholder="Enter Your User Name(used at login time).">
                                    
                                            <label>Enter Password</label>
                                            <input class="form-control" type="password"name="p" placeholder="Enter Your Password(used at login time).">
                              
                                           
                                            
                                            

                                            
                                            
                                            
                                   
                                        </div>
                                 
                                        <button type="submit" class="btn btn-danger">Register </button>

                                    </form>
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
