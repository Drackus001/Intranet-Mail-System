#!C:\Python27\python.exe
import exceptions
import urllib
import cgi, cgitb
import MySQLdb
import sys
cgitb . enable()
form = cgi.FieldStorage() 
try:
        sid = form.getvalue('sid')
        db = MySQLdb.connect("localhost","root","system","IMS" )
        cursor = db.cursor()
        a="select user_id from session where session_id='"+str(sid)+"'"
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
                    <title>Dasboard</title>

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

                            <div class="header-right">
                """
        print '<a href="message-task.py" class="btn btn-info" title="New Message"><b>%s</b><i class="fa fa-envelope-o fa-2x"></i></a>' %(n)

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
        print ("<a class='active-menu' href='index_admin.py?sid="+str(sid)+"'><i class='fa fa-ge'></i>Dashboard</a>")
        print "</li><li>"	
        print "<a href='Profile.py?sid="+str(sid)+"'><i class='fa fa-user'></i>Profile</a>"
        print "</li><li>"
        print "<a href='AddAccount.py?sid="+str(sid)+"'><i class='fa fa-plus-circle'></i>Add Account</a>"
        print "</li><li>"
        print "<a href='ActiveUser.py?sid="+str(sid)+"'><i class='fa fa-circle'></i>Active User</a>"
        print "</li><li>"
        print "<a href='startingmail.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Starting Mail</a>"
        print "</li><li>"
        field="inbox"
        print "<a href='inbox.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Inbox</a>"
        print "</li><li>"
        print "<a href='Compose.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Compose</a>"
        print "</li><li>"
        print "<a href='sentmail.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Sent Mail</a>"
        print "</li><li>"
        print "<a href='replay_mail.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Reply Mail</a>"
        print "</li><li>"
        print "<a href='startingmail.py?sid="+str(sid)+"'><i class='fa fa-table'></i>Forward Mail</a>"
        print "</li><li>"
        print "<a href='new_Group.py?sid="+str(sid)+"'><i class='fa fa-group'></i>Group</a>"
        print "</li><li>"
        print "<a href='Label.py?sid="+str(sid)+"'><i class='fa fa-archive'></i>Label</a>"
        print "</li><li>"
        print "<a href='Search.py?sid="+str(sid)+"'><i class='fa fa-search'></i>Search</a>"
        print "</li><li>"
        print "<a href='PasswordRecoveer.py?sid="+str(sid)+"'><i class='fa fa-recycle'></i>Password Recover</a>"
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
                                <h1 class="page-head-line">welcome to ADMIN.</h1>
                                <h1 class="page-subhead-line">DASHBOARD </h1>
                                    </div>
                        </div>
                        
                           <!-- /. ROW  -->
                        <div id="port-folio">
                                      <div class="row " >
                             
                        <div class="col-md-4 ">
                                 <a href="profile.py">   <div class="portfolio-item awesome mix_all" data-cat="awesome" >


                                        <img src="profile_1x.png" class="img-responsive " alt="" />
                                        <div class="overlay">
                                            <p>
                                              PROFILE	
                                            </p>
                                            
                                        </div>
                                    </div></a>
                                </div>
                                <div class="col-md-4 ">

                                  <a href="AddAccount.py">  <div class="portfolio-item landscape mix_all" data-cat="landscape" >


                                        <img src="icon-account.png" class="img-responsive " alt="" />
                                        <div class="overlay">
                                            <p>
                                            ADD ACCOUNT
                                            </p>
                                        </div>
                                    </div></a>
                                </div>
                                <div class="col-md-4 ">
                <a href="ActiveUser.py">
                                    <div class="portfolio-item nature mix_all" data-cat="nature" >


                                        <img src="ag" class="img-responsive " alt="" />
                                        <div class="overlay">
                                          <p>
                                          
                                        ACTIVE USER
                                            </p>
                                            </div>
                                    </div>
                            </a>    </div>

                            </div>

                            <div class="row " style="padding-top: 50px;">
                                <div class="col-md-4 ">
                <a href="">
                                    <div  class="portfolio-item nature mix_all" data-cat="nature" >


                                        <img src="dg" class="img-responsive " alt="" />
                                        <div class="overlay">
                                           <p>
                                            Start Mailing
                                            </p>
                                        </div>
                                    </div>
                            </a>    </div>
                                <div class="col-md-4 ">
                <a href="Group.py">
                                    <div  class="portfolio-item nature mix_all" data-cat="nature" >


                                        <img src="ass" class="img-responsive " alt="" />
                                        <div class="overlay">
                                            <p>
                                                                GROUP
                                            </p>
                                            </div>
                                    </div></a>
                                </div>
                                <div class="col-md-4 ">
                <a href="Label.py">
                                    <div  class="portfolio-item nature mix_all" data-cat="nature" >


                                        <img src="ass" class="img-responsive " alt="" />
                                        <div class="overlay">
                                          <p>
                                           LABEL
                                            </p>
                                            </div>
                                    </div>
                            </a>    </div>

                            </div>
                                    <div class="row "  style="padding-top: 50px;" >
                                <div class="col-md-4 ">
                <a href="Search.py">
                                    <div  class="portfolio-item nature mix_all" data-cat="nature" >


                                        <img src="ass" class="img-responsive " alt="" />
                                        <div class="overlay">
                                            <p>
                                            SEARCH
                                            </p>
                                        </div>
                                    </div>
                            </a>    </div>
                                <div class="col-md-4 ">
                <a href="PasswordRecover.py">
                                    <div  class="portfolio-item awesome mix_all" data-cat="awesome" >


                                        <img src="ass" class="img-responsive " alt="" />
                                        <div class="overlay">
                                            <p>
                                               PASSWORD RECOVER
                                            </p>
                                            

                                        </div>
                                    </div>
                            </a>    </div>
                                <div class="col-md-4 ">

                                <a href="DeleteAccount.py">    <div  class="portfolio-item nature landscape mix_all" data-cat="nature landscape" >


                                        <img src="ass" class="img-responsive " alt="" />
                                        <div class="overlay">
                                          <p>
                                            DELETE ACCOUNT 
                                            
                                            </p>
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
except Exception as e:
        print "Content-type:text/html\r\n\r\n"
        print """<html><head><meta http-equiv='refresh' content='0;url=login_1.py' /></head><body></body></html>"""

