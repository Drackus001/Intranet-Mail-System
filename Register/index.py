#!C:\Python27\python.exe

import cgi, cgitb
import base64
cgitb . enable()

val=0
val2=0
form = cgi.FieldStorage() 
user=form.getvalue('submit')
import MySQLdb
import sys
db = MySQLdb.connect("localhost","root","system","IMS" )
cursor = db.cursor()
print "Content-type:text/html\r\n\r\n"
print"""<html >
<head>
  <meta charset="UTF-8">
  <title>Register User</title>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">

  
      <style>
      /* NOTE: The styles were added inline because Prefixfree needs access to your styles and they must be inlined if they are on local disk! */
      * {
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

body {
  background: #333;
  font: 100%/1 "Helvetica Neue", Arial, sans-serif;
}

.Register {
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -10rem 0 0 -10rem;
  width: 24rem;
  height: 20rem;
  padding: 20px;
  background: #fff;
  border-radius: 5px;
  overflow: hidden;
}
.Register:hover > .Register-header, .Register.focused > .Register-header {
  width: 2rem;
}
.Register:hover > .Register-header > .text, .Register.focused > .Register-header > .text {
  font-size: 1rem;
  transform: rotate(-90deg);
}
.Register.loading > .Register-header {
  width: 20rem;
}
.Register.loading > .Register-header > .text {
  display: none;
}
.Register.loading > .Register-header > .loader {
  display: block;
}

.Register-header {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 1;
  width: 24rem;
  height: 20rem;
  background: orange;
  transition: width 0.5s ease-in-out;
}
.Register-header > .text {
  display: block;
  width: 100%;
  height: 100%;
  font-size: 5rem;
  text-align: center;
  line-height: 20rem;
  color: #fff;
  transition: all 0.5s ease-in-out;
}
.Register-header > .loader {
  display: none;
  position: absolute;
  left: 5rem;
  top: 5rem;
  width: 10rem;
  height: 10rem;
  border: 2px solid #fff;
  border-radius: 50%;
  animation: loading 2s linear infinite;
}
.Register-header > .loader:after {
  content: "";
  position: absolute;
  left: 4.5rem;
  top: -0.5rem;
  width: 1rem;
  height: 1rem;
  background: #fff;
  border-radius: 50%;
  border-right: 2px solid orange;
}
.Register-header > .loader:before {
  content: "";
  position: absolute;
  left: 4rem;
  top: -0.5rem;
  width: 0;
  height: 0;
  border-right: 1rem solid #fff;
  border-top: 0.5rem solid transparent;
  border-bottom: 0.5rem solid transparent;
}

@keyframes loading {
  50% {
    opacity: 0.5;
  }
  100% {
    transform: rotate(360deg);
  }
}
.Register-form {
  margin: 0 0 0 2rem;
  padding: 0.5rem;
}

.Register-input {
  display: block;
  width: 100%;
  font-size: 2rem;
  padding: 0.5rem 1rem;
  box-shadow: none;
  border-color: #ccc;
  border-width: 0 0 2px 0;
}
.Register-input + .Register-input {
  margin: 10px 0 0;
}
.Register-input:focus {
  outline: none;
  border-bottom-color: orange;
}

.Register-btn {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  width: 5rem;
  height: 5rem;
  border: none;
  background: orange;
  border-radius: 50%;
  font-size: 0;
  border: 0.6rem solid transparent;
  transition: all 0.3s ease-in-out;
}
.Register-btn:after {
  content: "";
  position: absolute;
  left: 1rem;
  top: 0.8rem;
  width: 0;
  height: 0;
  border-left: 2.4rem solid #fff;
  border-top: 1.2rem solid transparent;
  border-bottom: 1.2rem solid transparent;
  transition: border 0.3s ease-in-out 0s;
}
.Register-btn:hover, .Register-btn:focus, .Register-btn:active {
  background: #fff;
  border-color: orange;
  outline: none;
}
.Register-btn:hover:after, .Register-btn:focus:after, .Register-btn:active:after {
  border-left-color: orange;
}

    </style>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>

</head>"""
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
                        cursor.execute("INSERT INTO user (User_id,First_name,Last_name,Gender,Email_addr,Bdate,Id_no,Mobile_no,Designation,Account_type,Password,status) values  ('"+U+"','"+F+"','"+L+"','"+G+"','"+E+"','"+D+"','"+I+"','"+M+"','"+DE+"','"+AT+"','"+base64.b64encode(P)+"','"+str(0)+"')")
                        sql = """commit"""
                        cursor.execute(sql)
                        href='index_admin.py?sid="+str(sid)+"'
                        print "<meta http-equiv='refresh' content='0;url=../index.py' />"
                else:
                        val2=1
        else:
                val=1
print"""

<body>
  
<div class="Register">
  <header class="Register-header"><span class="text">Register</span><span class="loader"></span></header>
  <form class="Register-form">"""
if(val==1):
	print"<h1 style='color:#e30000'>Enter All info.</h1>"
if(val2==1):
	print"<h1 style='color:#e30000'>Enter Same Password</h1>"
print"""    <input class="Register-input" name="UI" type="text" placeholder="Username"/>
    <input class="Register-input" name="P" type="password" placeholder="Password"/>
    <input class="Register-input" name="C" type="password" placeholder="Confirm Password"/>
    <button class="Register-btn" name="submit" type="submit" value="1">Register</button>
  </form>
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>

</body>
</html>"""
