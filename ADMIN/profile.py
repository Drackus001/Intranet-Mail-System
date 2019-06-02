#!C:\Python27\python.exe
import cgi, cgitb
cgitb . enable()
import base64
form = cgi.FieldStorage()
sid = base64.b64decode(form.getvalue('sid'))
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

n=cursor.execute("select * from user where User_id='"+sname+"'")
print "Content-type:text/html"
print """

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Profile</title>

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
print '<a class="btn btn-info" title="New Message"><b>%s</b><i class="fa fa-envelope-o fa-2x"></i></a>' %(n)
print """


            </div>
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
print "<a class='active-menu' href='index_admin.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-ge'></i>Dashboard</a>"
print "</li><li>"
print "<a href='Profile.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-user'></i>Profile</a>"
print "</li><li>"
print "<a href='AddAccount.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-plus-circle'></i>Add Account</a>"
print "</li><li>"
print "<a href='Request.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-check'></i>Registration Request</a>"
print "</li><li>"
print "<a href='ActiveUser.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-circle'></i>Active User</a>"
print "</li><li>"
print "<a href='startingmail.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-table'></i>Starting Mail</a>"
print "</li><li>"
print "<a href='EDE.py?sid="+base64.b64encode(str(sid))+"&cp="+str(1)+"'><i class='fa fa-lock'></i>encryption and decryption</a>"
print "</li><li>" 
print "<a href='change_password.py?sid="+base64.b64encode(str(sid))+"&cp="+base64.b64encode(str(1))+"'><i class='fa fa-recycle'></i>Change password</a>"
print "</li><li>" 
print "<a href='PasswordRecover.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-recycle'></i>Password Recover</a>"
print "</li><li>" 
print "<a href='DeleteAccount.py?sid="+base64.b64encode(str(sid))+"'><i class='fa fa-remove'></i>Delete Account</a>"
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
                        <h1 class="page-head-line">PROFILE</h1>
                        

                  <div class="col-md-8">

                        <div class="table-responsive">
                            <table class="table table-striped table-bordered table-hover">
                                
                                <tbody>
                                
"""
row=cursor.fetchall()
i=0
for row in cursor:
    i=i+1
    no=row[0]
    print "<tr><th>#no:</th><td>",row[0],"</td><tr>"
    print "<tr><th>User_id:</th><td>",row[1],"</td><tr>"
    print "<tr><th>First Name:</th><td>",row[2],"</td><tr>"
    print "<tr><th>Last Name:</th><td>",row[3],"</td><tr>"
    print "<tr><th>Gender:</th><td>",row[4],"</td><tr>"
    print "<tr><th>Email-Address:</th><td>",row[5],"</td><tr>"
    print "<tr><th>D.O.B :</th><td>",row[6],"</td><tr>"
    print "<tr><th>Id_no:</th><td>",row[7],"</td><tr>"
    print "<tr><th>Mobile No:</th><td>",row[8],"</td><tr>"
    print "<tr><th>Designation:</th><td>",row[9],"</td><tr>"
    print "<tr><th>Account type:</th><td>",row[10],"</td><tr>"
    #print "<tr><td>",row[0],"</td><br><td>",row[7],"</td></br><td>",row[2],"</td><td>",row[6],"</td></tr>"

    

      




                         
    print "</tbody>"
    print "</table>"
    print "<a href='Profile_edit.py?sid="+base64.b64encode(str(sid))+"'><button  class='btn btn-danger'>Edit </button></a>"
    print """
                        </div>




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