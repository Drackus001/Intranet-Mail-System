#!C:\Python27\python.exe
import cgi, cgitb
import base64
cgitb . enable()

form = cgi.FieldStorage()
sid = base64.b64decode(form.getvalue('sid'))
user=form.getvalue('submit')
                
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
val=0
val2=0





        
n=cursor.execute("select * from mailcon where  rname=('"+sname+"')")      

print """


    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Registr New User</title>

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
if (user==str(1)):

        F="null"
        L="null"
        G="null"
        E="null"
        D="null"
        I="null"
        M="null"
        DE="null"
        AT="user"
        U=form.getvalue('UI')
        P=form.getvalue('P')
        C=form.getvalue('C')
        M="null"
        if ((U and P) and C):
                if (C==P):
                        cursor.execute("INSERT INTO user (User_id,First_name,Last_name,Gender,Email_addr,Bdate,Id_no,Mobile_no,Designation,Account_type,Password,status) values  ('"+U+"','"+F+"','"+L+"','"+G+"','"+E+"','"+D+"','"+I+"','"+M+"','"+DE+"','"+AT+"','"+base64.b64encode(P)+"','"+str(1)+"')")
                        sql = """commit"""
                        cursor.execute(sql)
                        href='index_admin.py?sid="+str(sid)+"'
                        print "<meta http-equiv='refresh' content='0;url=index_admin.py?sid="+base64.b64encode(str(sid))+"' />"
                else:
                        val2=1
        else:
                val=1
print """       </div>
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
                        <h1 class="page-head-line">Add Account</h1>
                        
<div class="col-md-6 col-sm-6 col-xs-12"><div class="panel panel-danger">
                        <div class="panel-heading">
                           Registr New User"""

if(val==1):
	print"<h1 style='color:#e30000'>Enter All info.</h1>"
if(val2==1):
	print"<h1 style='color:#e30000'>Enter Same Password</h1>"



print                        """</div>
                        <div class="panel-body">
                            <form role="form" method="post" action="AddAccount.py">
                                        
                                 <div class="form-group">
                                          
                                            <label>User ID:</label>
                                            <input class="form-control" type="text" name="UI" placeholder="IMS@imail.py">
                                    
                                            <label>Enter Password</label>
                                            <input class="form-control" type="password"name="P" placeholder="Enter Your Password">
                              <label>Confirm Password:</label>
                                            <input class="form-control" type="password" name="C" placeholder="confirm Password">
                                           
                                            
                                            

                                            
                                            
                                            
                                   
                                        </div>
                                
                                 """
print "<input type='text' name='sid' value='"+base64.b64encode(str(sid))+"' hidden/>"                                 
print """    <button type="submit" name="submit" value="1" class="btn btn-danger">Register </button>

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

