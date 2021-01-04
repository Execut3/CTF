<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>PNT Company</title>
    <link href="./css/bootstrap.min.css" rel="stylesheet">
    <link href="css/heroic-features.css" rel="stylesheet">

</head>

<body>
	
	<?php  
		session_start();  
		if(!isset($_SESSION['username']))  
		{  
			header("Location: login.php");//redirect to login page to secure the welcome page without login access.  
		}    
	?>  
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="welcome.php">PNT Company</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
						<a href="contact.php">Contact</a>
                    </li>
					<li>
						<a href="search.php">Search</a>
                    </li>
                </ul>
				<ul class="nav navbar-nav pull-right">
					<li class="pull-right">
						<a href="profile.php?id=<?php echo $_SESSION['id'] ?>">your-profile</a>
					</li>
					<li class="pull-right">
                        <a href="logout.php">Logout</a>
                    </li>
				</ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">

        <!-- Jumbotron Header -->
        <header class="jumbotron hero-spacer">
            <h2 class="v-center">Welcome to PNT HomePage</h2>
		<h3>PNT (Product New Technology) is one of the pioneers in network security.</h3>
        </header>

        <hr>

        <!-- Title -->
        <div class="row">
            <div class="col-lg-12">
                <h3>Latest Products</h3>
            </div>
        </div>
        <!-- /.row -->

        <!-- Page Features -->
        <div class="row text-center">

            <div class="col-md-4 col-sm-6 hero-feature">
                <div class="thumbnail">
                    <img src="./pics/network_security_technology_slide2.jpg" alt="">
                    <div class="caption">
                        <h3>McAfee Bolters Network Security Platform</h3>
                        <p>McAfee recently announced enhancements to its
						Network Security Platform. The security company’s 
						latest release includes virtual network inspection 
						technology to enable the platform sensors to examine 
						traffic between virtual machines and detect attacks 
						against virtual data center environments. McAfee also
						enhanced its reputation-based capabilities to fight 
						botnets, and added traffic redirection capabilities 
						to allow arbitrary network traffic to be inspected by
						McAfee and third-party products</p>
                        <p>
                        <a href="./products/index.php?id=1" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-sm-6 hero-feature">
                <div class="thumbnail">
                    <img src="./pics/network_security_technology_slide3.jpg" alt="">
                    <div class="caption">
                        <h3>Cisco SecureX framework</h3>
                        <p>Pictured here is one of the Cisco ASA 5500 Series
						Adaptive Security Appliances. At the RSA Security 
						Conference in San Francisco earlier this year, Cisco
						announced it would be bringing context-aware firewalling
						and policy enforcement to these appliances. The capabilities
						are part of what Cisco calls its SecureX Architecture, 
						which also encompasses pieces like Cisco AnyConnect and
						extensible APIs (application programming interfaces) that
						permit Cisco's management systems and partners to plug in
						to complete the security ecosystem. The context-aware 
						capabilities will be added to the Cisco ASA 5500 Series 
						this summer.</p>
                        <p>
                        <a href="./products/index.php?id=2" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>

            <div class="col-md-4 col-sm-6 hero-feature">
                <div class="thumbnail">
                    <img src="./pics/network_security_technology_slide4.jpg" alt="">
                    <div class="caption">
                        <h3>CheckPoint Adds New Blades</h3>
                        <p>Check Point R75 was released in February, and offers four
						software blades: Application Control, Identity Awareness, 
						Data Loss Prevention and Mobile access. The Application 
						Control Software Blade was brand new in the release, and 
						integrates Check Point’s UserCheck technology to “engage 
						employees in the remediation process” and leverages the 
						Check Point AppWiki, which includes more than 100,000 Web
						2.0 application and widgets. The Identity Awareness blade 
						is also brand new, and allows organizations to create 
						policies based on identity.</p>
                        <p>
                          <a href="./products/index.php?id=3" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>
                

        </div>
		<div class="row text-center">
		
		</div>
		<!-- /.row -->
            <div class="col-md-4 col-sm-6 hero-feature">
                <div class="thumbnail">
                    <img src="./pics/network_security_technology_slide5.jpg" alt="">
                    <div class="caption">
                        <h3>Juniper Networks Looks To Unify Network Access</h3>
                        <p>Juniper Networks announced the availability of its
						MAG Series Junos Pulse Gateways April 13. Offered in 
						four models, the Juniper Networks MAG Series Junos Pulse
						Gateways deliver SSL VPN connectivity and network access
						control (NAC) capabilities.</p>
                        <p>
                         <a href="./products/index.php?id=4" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>
			
			<div class="col-md-4 col-sm-6 hero-feature">
                <div class="thumbnail">
                    <img src="./pics/network_security_technology_slide6.jpg" alt="">
                    <div class="caption">
                        <h3>PacketMotion Eyes Virtual Networks</h3>
                        <p>PacketMotion released the PacketSentry Virtual Probe
						to help organizations monitor access to data in VMware 
						clusters and secure and audit communications between virtual
						machines (VMs). PacketSentry Virtual Probe is delivered as a
						guest VM. Among the applications monitored are databases,
						fileshares and Web applications.</p>
                        <p>
                         <a href="./products/index.php?id=5" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>
			
			<div class="col-md-4 col-sm-6 hero-feature">
				<div class="thumbnail">
                    <img src="./pics/network_security_technology_slide7.jpg" alt="">
                    <div class="caption">
                        <h3>Fortinet Targets the Data Center</h3>
						<p>The FortiGate-3140B security appliance is aimed at large
						enterprises and their data centers. The appliance offers a 
						total of 22 ports, and can be deployed either as a firewall 
						or unified threat management solution configured to support VPN,
						IPS, application control, anti-spam and antivirus.</p>
                        <p>
                         <a href="./products/index.php?id=6" class="btn btn-default">More Info</a>
                        </p>
                    </div>
                </div>
            </div>
        <hr>


    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>