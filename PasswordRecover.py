#!C:\Python27\python.exe
import cgi, cgitb
cgitb . enable()

form = cgi.FieldStorage()
sid = form.getvalue('sid')
import MySQLdb
import sys
db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()
cursor1 = db.cursor()

a="select user_id from session where session_id='"+str(sid)+"'"
v=cursor.execute(a)
row=cursor.fetchall()

for row in cursor:
	sname=row[0]
n=cursor.execute("select * from mailcon where sname=('"+sname+"') or rname=('"+sname+"')")	
print "Content-type:text/html"
print """
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Password Recover</title>

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
                <a class="navbar-brand" href="index_admin.py">Intranet Mail System</a>
            </div>

            <div class="header-right">"""
print '<a href="message-task.py" class="btn btn-info" title="New Message"><b>%s</b><i class="fa fa-envelope-o fa-2x"></i></a>' %(n)        


print"""          </div>
        </nav>
        <!-- /. NAV TOP  -->
        <nav class="navbar-default navbar-side" role="navigation">
            <div class="sidebar-collapse">
                <ul class="nav" id="main-menu">
                    <li>
                        <div class="user-img-div">
                            <img src="user.png" class="img-thumbnail" />
<div class="inner-text">"""
print sname
print """  

                     
                        </div>

                    </li>


                    <li>"""
                    
print "<a class='active-menu' href='index_admin.py?sid="+str(sid)+"'><i class='fa fa-ge'></i>Dashboard</a>"
print "</li><li>"
print "<a href='Profile.py?sid="+str(sid)+"'><i class='fa fa-user'></i>Profile</a>"
print "</li><li>"
print "<a href='AddAccount.py?sid="+str(sid)+"'><i class='fa fa-plus-circle'></i>Add Account</a>"
print "</li><li>"
print "<a href='ActiveUser.py?sid="+str(sid)+"'><i class='fa fa-circle'></i>Active User</a>"
print "</li><li>"
print "<a href='startingmail.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Starting Mail</a>"
print "</li><li>"
print "<a href='Group.py?sid="+str(sid)+"'><i class='fa fa-group'></i>Group</a>"
print "</li><li>"
print "<a href='Label.py?sid="+str(sid)+"'><i class='fa fa-archive'></i>Label</a>"
print "</li><li>"
print "<a href='Search.py?sid="+str(sid)+"'><i class='fa fa-search'></i>Search</a>"
print "</li><li>"
print "<a href='PasswordRecover.py?sid="+str(sid)+"'><i class='fa fa-recycle'></i>Password Recover</a>"
print "</li><li>"
print "<a href='DeleteAccount.py?sid="+str(sid)+"'><i class='fa fa-remove'></i>Delete Account</a>"
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
                        <h1 class="page-head-line">Password Recover</h1>
                

                    <div class="col-md-8">

                        <div class="table-responsive">
                            <table class="table table-striped table-bordered table-hover">
                                <thead>

                                    <tr>
                                        <th>#</th>
                                        
                                        <th>First Name</th>
                                        <th>Last Name</th>
                                        <th>User ID</th>
                                        <th>ID No.</th>
                                        <th>P. Recover</th>
                                    </tr>
                                </thead>
                                <tbody>
                                   """
a="admin@imail.py"
x=cursor.execute("select * from user where user_id!=('"+a+"')")
row=cursor.fetchall()
i=1
for row in cursor:
        print "<tr><td>",i,"</td><td>",row[2],"</td><td>",row[3],"</td><td>",row[1],"</td><td>",row[7],"</td><td><a href='Password_u.py?sid="+str(sid)+"&uid="+row[1]+"'>Recover</a>"
        print "</td></tr>"
        i=i+1                  
                                   
print """                                </tbody>
                            </table>
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
