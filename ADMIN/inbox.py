#!C:\Python27\python.exe
import cgi, cgitb
cgitb . enable()
import base64

form = cgi.FieldStorage() 
sid = base64.b64decode(form.getvalue('sid'))
field = form.getvalue('field')
li = form.getvalue('li')
ln = form.getvalue('ln')
delete=form.getvalue('Delete')
no =form.getvalue('no')

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


if(li==str(1)):
        n=cursor.execute("select * from mailcon where rname like ('%"+sname+"%') and field ='"+str(ln)+"'")
else:
        n=cursor.execute("select * from mailcon where rname like ('%"+sname+"%') and field ='inbox'")



print """

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
                <a class="navbar-brand" >Intranet Mail System</a>
            </div>

            <div class="header-right">"""

 
if (delete==str(1)):
        cursor.execute("select * from mailcon where no='"+str(no)+"'")
        row=cursor.fetchall()
        for row in cursor:
                message=row[1]
                subject=row[2]
                to=row[3]
                sname=row[6]
                time=row[5]
                field=row[4]
                status=row[7]
                cursor.execute("INSERT INTO dmail (message,sub,rname,field,date,sname,status) values  ('"+message+"','"+subject+"','"+to+"','"+field+"','"+time+"','"+sname+"','"+str(1)+"')")
                sql = """commit"""
                cursor.execute(sql)
                cursor.execute("delete from mailcon where no='"+str(no)+"'")
                cursor.execute("commit")
                print "<meta http-equiv='refresh' content='0;url=inbox.py?sid="+base64.b64encode(str(sid))+"' />"            
print '<a  class="btn btn-info" title="New Message"><b>%s</b><i class="fa fa-envelope-o fa-2x"></i></a>' %(n)

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
                        <h1 class="page-head-line">INBOX</h1>
                

                    <div class="col-md-8">

                        <div class="table-responsive">
                            <table class="table table-striped table-bordered table-hover">
                                <thead>
                                    <tr>
                                        <th>#</th>
                                        <th>Sender ID</th>
                                        <th>Subject</th>
                                        <th>Date</th>
                                        <th>Delete Mail</th>
                                     </tr>
                                </thead>
                                <tbody>
                                
"""
row=cursor.fetchall()
i=0
for row in cursor:
        i=i+1
        no=row[0]
        print "<tr><td style='color=red'>",i,"</td><td>",row[6],"</td><td><a href='mail_info.py?sid="+base64.b64encode(str(sid))+"&no="+str(no)+"&rs="+str(1)+"'>",row[2],"</a></td><td>",row[5],""
        print "</td><td><a href='inbox.py?sid="+base64.b64encode(str(sid))+"&Delete="+str(1)+"&no="+str(no)+"'>Remove</a></td></tr>"

   
    
print """
           




                         
                                </tbody>
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






