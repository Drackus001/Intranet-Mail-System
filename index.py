#!C:\python\Python35-32\python.exe
import cgi, cgitb
cgitb . enable()

form = cgi.FieldStorage()
print "Content-type:text/html"
print """
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=devidev-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title> Intranet Mail System</title>
	<script type="text/javascript" src="js/loader.js"></script>
       <script type="text/javascript" src="js/loaderonline.js"></script>
	<!-- [ FONT-AWESOME ICON ] -->
	<link rel="stylesheet" type="text/css" href="library/font-awesome-4.3.0/css/font-awesome.min.css">
	<!-- [ PLUGIN STYLESHEET ] -->
	<link rel="shortcut icon" type="image/x-icon" href="images/icon.png">
	<link rel="stylesheet" type="text/css" href="css/animate.css">
	<link rel="stylesheet" type="text/css" href="css/owl.carousel.css">
        <link rel="stylesheet" type="text/css" href="css/owl.theme.css">
	<link rel="stylesheet" type="text/css" href="css/magnific-popup.css">
	
	<!-- [ Boot STYLESHEET ] -->
	<link rel="stylesheet" type="text/css" href="library/bootstrap/css/bootstrap-theme.min.css">
	<link rel="stylesheet" type="text/css" href="library/bootstrap/css/bootstrap.css">
	
        <!-- [ DEFAULT STYLESHEET ] -->
	<link rel="stylesheet" type="text/css" href="css/style1.css">
  <link rel="stylesheet" type="text/css" href="css/style2.css">
        <link rel="stylesheet" type="text/css" href="css/responsive.css">
	<link rel="stylesheet" type="text/css" href="css/color/rose.css">
  
</head>
<body >
	<div class="preloader">
    <div class="loader theme_background_color">
        <span></span>
      
    </div>
</div>
   
<div class="wrapper">
 <nav  class=" nim-menu navbar navbar-default navbar-fixed-top">
      <div class="container">

        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">

          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
            <a class="navbar-brand" href="index.py">Intranet <span class="themecolor">Mail </span>System</a>
        </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#home" class="page-scroll">Home</a></li>
            <li><a href="#feature" class="page-scroll">Feature</a></li>
            <li><a href="#login" class="page-scroll">Log In</a></li>
            
            <li><a href="#contact" class="page-scroll">Contact</a></li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->

    </nav>
<section class="main-heading" id="home">

       <div class="overlay">
           <div class="container">
               <div class="row">
                   <div class="main-heading-content col-md-12 col-sm-12 text-center">

        <canvas id="myCanvas" ></canvas><h1 class="main-heading-title">WE PROVIDES <span class="main-element themecolor" data-elements="Simple GUI,Mailing Facility,Easy communication,Gruoping Facility,privacy,Chatting facility,security"></span></h1>
        <p class="main-heading-text">The Main objective of the project is to develop a <b>I</b>ntranet <b>M</b>ail <b>S</b>ystem <br/>that enhances communications among the members of the organization <br/>in a reliable, cost-effective, secure way and without using the internet resources.</p>
        <div class="btn-bar">
          <a href="#login" style=" background-color: #66e754" class="btn btn-custom theme_background_color">Ge Started</a>
        </div>

      </div>
               </div>
           </div>
       </div>  

   </section>
<section class="services white-background black" id="feature">
      <div class="container">
        <div class="row text-center">
          <div class="col-md-12">
              <h3 class="title">Proveided <span style="color: #ff0000">Features</span></h3>
            <p class="a-slog">The Following are some Features which is been Provided by This <b>I</b>NTRANET <b>M</b>AIL <b>S</b>YSTEM Project</p>
          </div> <!-- /col -->
        </div> <!-- /row -->
        <div class="gap"></div>

        <div class="row">
          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-diamond"></i>
              <div class="nim-service-detail">
                <h4>Simple GUI</h4>
                <p>Simple GUI Description...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-tablet"></i>
              <div class="nim-service-detail">
                <h4>Mailing</h4>
                <p> Mailing Description... </p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-magic"></i>
              <div class="nim-service-detail">
                <h4>Uses Intranet</h4>
                <p>Intranet Description...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->       
        </div> <!-- end row -->

        <div class="row">
          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-rocket"></i>
              <div class="nim-service-detail">
                <h4>Chatting</h4>
                <p>Chatting Description...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-map-marker"></i>
              <div class="nim-service-detail">
                <h4>Security</h4>
                <p>Security Description...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-paypal"></i>
              <div class="nim-service-detail">
                <h4>Privacy</h4>
                <p>Privacy Desc...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->         
        </div> <!-- end row -->

        <div class="row">
          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-bar-chart-o"></i>
              <div class="nim-service-detail">
                <h4>Groups</h4>
                <p>Groups Desc...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-delicious"></i>
              <div class="nim-service-detail">
                <h4>Easy Communication</h4>
                <p>Easy Communication...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->

          <div class="col-sm-4">
            <div class="nim-service margin-bottom">
              <i class="fa fa-pencil-square"></i>
              <div class="nim-service-detail">
                <h4>Encryption & Decryption</h4>
                <p>Encryption And Decryption Desc...</p>
              </div> <!-- /nim-service-detail -->
            </div> <!-- /nim-service margin-bottom -->
          </div> <!-- /col -->                      
        </div> <!-- end row -->

      </div>  <!-- container -->
    </section>
    

 <section >
 <center>

 
  <div id="login">
	  	<div class="container">
	  	
		      <form class="form-login" action="login_2.py" method="post"><br/>
		     <h3 class="title">sign in <span class="themecolor">Now</span></h3>

		        <div class="login-wrap"><br/>
		            <input type="text" class="form-control" placeholder="User ID" name="uname" >
		            <br>
		            <input type="password" class="form-control" placeholder="Password" name="pass">
		            <br/>
		            <button class="btn btn-theme btn-block" href="" type="submit" style="background-color:#eaaf4d; width: 35%; "><i class="fa fa-lock"></i> &nbsp;SIGN IN</button>
		           <br/>
		            <div class="registration">

		                      Don't have an account yet? &nbsp; <a class="" href="register/index.py">
		                    Create an account

		                      </a>
		            </div>
		
		        </div>
		</form>
		          <!-- Modal -->
		              </div>
		          </div>
		          <!-- modal -->
		
		     	  	
	  	
	  	
 
 </center>
 </section>
 <section class="sub-form text-center" id="contact">
  <div class="container">
   
    <div class="col-md-12">

        <h3 class="title">FOR MORE INFORMATION <span class="themecolor">Contact Us</span></h3>


    </div> 
                    
              
    <br><br>
<br><br>
        <!--social-->
       <center>
		<div>
		<ul class="social1">

<li class="facebook"><a href="#" class="entypo-facebook"></a></li>
<li class="instagrem"><a href="#" class="entypo-instagrem"></a></li>
<li class="gplus"><a href="#" class="entypo-gplus"></a></li>
<li class="mail"><a href="#" class="entypo-mail"></a></li>
<li class="phone"><a href="#" class="entypo-phone"></a></li>


		</ul>
		</div>
		</center>
	        <!--social end--> 
                    
    </div>
 
</section>
<footer class="site-footer section-spacing text-center ">
    
  <div class="container">
    <div class="row">
      
      
      <div class="col-md-4">
      
      </div>
      
      
      <div class="col-md-4"> <small>&copy; 2016-17    <b>  I</b>ntranet <b>M</b>ail <b>S</b>ystem. All rights reserved.</small></div>
      
    </div>
  </div>
</footer>


</div>
<script src="library/modernizr.custom.97074.js"></script>
	<script src="library/jquery-1.11.3.min.js"></script>
        <script src="library/bootstrap/js/bootstrap.js"></script>
	<script type="text/javascript" src="js/jquery.easing.1.3.js"></script>	
	<!-- [ PLUGIN SCRIPT ] -->
        <script src="library/vegas/vegas.min.js"></script>
	<script src="js/plugins.js"></script>
        <!-- [ TYPING SCRIPT ] -->
         <script src="js/typed.js"></script>
         <!-- [ COUNT SCRIPT ] -->
         <script src="js/fappear.js"></script>
       <script src="js/jquery.countTo.js"></script>
	<!-- [ SLIDER SCRIPT ] -->  
        <script src="js/owl.carousel.js"></script>
         <script src="js/jquery.magnific-popup.min.js" type="text/javascript"></script>
        <script type="text/javascript" src="js/SmoothScroll.js"></script>
        
        <!-- [ COMMON SCRIPT ] -->
	<script src="js/common.js"></script>
	<script src="js/index2.js"></script>
</body>


</html>
"""
