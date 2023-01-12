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
		include('stuff/header.php');
		include('private/check_session.php');
	?>

	<!-- Page Content -->
    <div class="container">
        <!-- Jumbotron Header -->
        <header class="jumbotron hero-spacer">
            <h2 class="text-center">APA-IUTcert CAPTURE the FLAG</h2>
			<h4 class="text-center">A challenge for experts</h4>
        </header>
    </div>
	<div class="container">


	
		<center>
			<h2>CTF-style hacking challenges</h2>
		</center>

		<p>
		On several occasions I host <i>Capture The Flag</i>-style exercise in IT security for
		teams of students. The task is to maintain a server
		running multiple services, while simultaneously trying to get access to
		the other team's servers. Each successful penetration gains points, as
		well as keeping services up and functional during the course of the game.

		<h2>Description</h2>

		The exercise consists of multiple teams, each hosting a server that has
		multiple services running, like e.g. a webserver, a mail server, or
		customized services. The services contain typical security vulnerabilities
		that allow to compromise the server to a certain extend.

		<p>
		The goal is to maintain the services up, functional and uncompromised
		for the duration of the game. Additional scores can be gained by 
		patching the vulnerabilities of the services and exploiting the knowledge
		of the found weaknesses at the other team's servers.

		<p>The focus of the exercise is on <i>application layer security</i>.

		<h2>Technical Details</h2>

		<ul>
			<li>The contest will be held within a VPN. We will use openVPN to 
					authenticate the teams and make sure that the exercise will have
					no effect on the remainder of the internet.
			<li>All traffic will be logged.
			<li>The traffic will be anonymized on the IP-layer, i.e. it's not easily
					possible to decide between other team's requests and the game
					server based on the IP. Thus filtering based on the IP is 
					useless. However, any other other mechanics to decide between game 
					server and other team on the TCP/IP-layer are <b>forbidden</b>.
			<li>All computers in a team's VPN-subnet are legible targets for attacks.
			<li>The services will be part of a VMware-image. This image will 
					be encrypted and distributed ahead of time. The key will be
					published at the begin of the exercise.
			<li>The image will contain some mean for the gamemaster to log on and
					check if the team is adhering to the rules. It is not allowed to
					de-activate this account.		
			<li>There will be an IRC-channel for discussion and answering
					technical problems.
			<li>Necessary tools to participate in this contest include per team:
					<ul>
						<li>one or two boxes as router and team-host
						<li>one computer per participant
						<li>a stable internet connection with a minimum of 1Mbit/sec that is 
								able to send and receive UDP-packets (we make use of openVPN)
						<li>we estimate that the complete setup takes about 1 day, including
								checks for safety and security
						<li>no commercial licenses are needed to participate, there are no
								fees to be paid
					</ul>
		</ul>

		<h2>Game Details</h2>

		<ul>
			<li>The vulnerable services will be custom services, i.e. the software
					that is subject to the scoring system is written specificly for 
					this contest. There will be no standard software that deliberatly 
					contains error. On the other hand, the organizers will not guarantee that
					the other software on the provided image is free of errors, but it 
					is quite safe to assume that the standard software should be secure,
					unless one team owns unpublished zero-day exploits 
			<li>The game server will contact each service on each server in variable
					intervals to check them for functionality. Points are awarded for 
					keeping the services up and running during the exercise. 
			<li>The server will also do some actions that leaves back a <i>flag</i>, 
				i.e. a certain string, and tries to retrieve the flag it left there 
					last time. If all of this is possible and the flag got not submitted 
					by other teams to the scoring system, a team gains points for having
					an uncompromised service.
			<li>A team may gain additional points by compromising a remote machine and gaining
				access to the stored <i>flags</i>. Each flag is worth an amount of 
					points, if submited to the scoring system within a few minutes after it
					got deposited. 
			<li>The following is discouraged and is possibly fined with negative 
					scores:
					<ul>
						<li>Filtering connections based on the connection layer is 
								not allowed (regardless of IP-anonymization).
						<li>Filtering requests on the application layer is 
								not allowed with means which are outside the actual CTF-service.
						<li>Automated scanning (ports, IPs, etc.) or usage of vulnerability 
								scanners.
						<li>Attacks like Denial-of-Service, Distributed-Denial-of-Service
								or Bandwith Exhaustion.
						<li>Changing the routing on any compromised host.
						<li>Destructive behaviour (e.g. deleting vital system files).
						<li>Intentionally supporting other teams is considered bad sportsmanship
								and will be fined (esp. if both teams belong to the same affiliation).
						<li>In the IRC-channel: Swearing, flooding, and similar.
						<li><i>(this list is not complete)</i>
					</ul>
			<li>The following is discouraged and is possibly fined with negative 
					scores and/or immediate dispension from the game:
					<ul>
						<li>The game server and all hosts in the organisator's network
								are off-limits.
						<li>Attacking systems outside the VPN is not allowed. All traffic
							has to happen within the VPN. Each team has to ensure themselves
								that other teams can't <i>accidently</i> harm other hosts in their
								networks.
						<li>Relaying data through other team's networks into the internet.
						<li>Cheating on the team's size leads to immediate disqualification.
						<li><i>(this list is not complete)</i>
					</ul>
		</ul>

		<A id='scoring'></a>
		<h2>Scoring details</h2>

		<ul>
			<li>The scoring system may still change in small details until the start of the contest.
				All changes will be published here. There will be no more changes after the
					beginning of the contest.
			<li>The scores for <b>defense</b> are given according to these rules:
					<ul>
						<li>Each service of each team will get checked once per interval. 
							An interval will be (most probably) between 60 seconds and 5 minutes.
						<li>If a service can be contacted and seems to works, the team receives 
							possibly some defensive points for the uptime.
						<li>If the service works correctly, i.e. if the service delivers the data and the flag
							that the gameserver asked for, the team receives defensive points
								for having a &quot;running&quot; service.
						<li>The gameserver will, in addition to just leave and retrieve the flag, check
							separate functionality of the services, which might not be important for 
								setting or reading the flag per-se. If this functionality is not there,
								the gameserver might consider tha players intentionally pruned the code 
								in order to have a smaller attack vector.<br>
								This is considered a <b>foul</b>. Within the next 5 to 10 minutes the team
								will not receive any more scores for this service. Then, the services
								is checked again, if the functionality is back.<br>
								Note that in case fo repeated and heavy fouls, a team is destined to loose
								ethical scores, too.
						<li>The gameserver will provide a limited error analysis, if the service is not
							up:
								<ul>
									<li>Wrong Flag: the service returned the wrong or no flag, but otherwise everything was OK
									<li>Output garbled: the output was so garbled, the gameserver could not even 
											recognize where the flag could have been
									<li>Network: there were problems on the network layer, the remote host was unreable,
											the network was down, or whatever
									<li>Timeout: everything just took to long to respond (note that we sometimes cannot distinguish 
										between actual network and timeout errors...)
									<li>Foul: see above
									<li>Generic Error: everything else or unknown
								</ul>
						<li>If a valid flag is submitted by another team, all defensive points awarded 
							for this flag are immediatly cancelled.
						<li>The score board will only display the <i>relative</i> amount of points
								to the leading party, instead of the absolute scores.
					</ul>
			<li>The scores for <b>offensive</b> attacks are given according to these rules:
					<ul>
						<li>All flags are valid for submition for a limited period only. After
								this period, submitting a flag will result in no effect.
						<li>A team can only submit flags from a service, if their own service
							of this type is considered &quot;up&quot; by the gameserver.
						<li>Each time, a team submits a flag, it receives a number of 
							points according to the difficulty of hacking the resp. service.<br>
						<li>The score board will only display the <i>relative</i> amount of points
								to the leading party, instead of the absolute scores.
					</ul>
			<li>In addition to defensive and offensive scores, the game features ethical scores.
					<ul>
						<li>Each team has 10 ethical scores at the start of the game.
						<li>For violations of the rules, teams may loose ethical scores. Regardsless of
								possible gains in ethical scores, teams are exlcuded from the game, if they
								lost 10 or more ethical scores bue to rule violations.
						<li>Teams can gain ethical scores for publishing advisories.
						<li>Each advisory is scored 0 to 5 ethical scores, depending on the quality of
								the text and the level of difficulty of the described bug.
							We assign scores for each disclosed vulnerablity only once, in a first come, first served fashion.
						<li>An advisory will only get scored, if it contains at least a short description of
								the bug, an exploit and a patch to remove the bug.
						<li>If an advisory scores X points, it will be disclosed to all other players
								after X * 30 minutes of time.		
				</ul>
			<li>The total score is calculated as follows: for each of the categories <i>defensive</i>,
					<i>offensive</i>, and <i>ethical scores</i> a team is assigned a value
					of relative scores to the team with the most scores in each respective category. These
					three relative scores are then added and normalized, such that the leading team
					has 100%.<br>
				<li>Note that there are some actions that are allowed but not awarded with scores. 
					These include: breaking into a team's
					router, breaking into other player's computers, and submitting own flags.
		</ul>
		
		<h2>Setup Details</h2>

		<p>Typically, each team is assigned a class-c subnet to setup their computers and
		the server. Often there are some fixed addresses that need to be used:</p>
		<ul>
			<li>10.X.Y.1 : the team's router
			<li>10.X.Y.2 : PC serving the vulnerable image (if using an extra computer, otherwiese leave empty)
			<li>10.X.Y.3 : vulnerable image
			<li>10.X.Y.10- : players
		</ul>

		<p>Teams are strongly advised to setup and test the configuration as soon as possible. Sometimes there's
		an empty test image released to test connectivity.</p>

		<p>All routing is done via the central VPN-server. Check the following image for an overview of a typical
		network structure. In this example, team 2 and 3 have a dedicated server carrying the vulnerable image, 
		while team 1 hosts the image on the router (beware CPU load!).</p>	
	
	</div>
	

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

	
	
	<!-- Designed by : J0hnTHEh4ck3r -->
	
	
	
</body>

</html>