#Anybots

<center>
<img src="{{wr}}static/img/anybots/qb.jpg" class="thumbnail" width="26%">

Anybots QB

</center>


<br>
<br>


##Overview

I spent the summer of 2011 at an internship with [Anybots](http://anybots.com), a small robotics startup out in Silicon Valley. For a long time Anybots was mostly a research company, producing robots like Monty and Dexter (both pictured below). However, two years ago they began to design QB (pictured above), a telepresence robot that aims to act as a robotic avatar to allow users to project their presence to other people from afar.

During my short time at Anybots, I noticed a severe lack of infrastructure for monitoring the fleet of about 130 robots out in the world (several million dollars' worth of robots). A friend and coworker was spending a tremendous amount of time every day manually checking what robots were online by SSHing into each one and reading the logs, which were often thousands of lines long. Because scalability is one of the things that can kill a startup fast and because I wanted to free up his valuable time, I wrote Super_robert and Anystats to help him out by automatically gathering logs from robots and computing information and statistics about global robot fleet status.

<br>
<br>

<center>
<img src="{{wr}}static/img/anybots/montydexter.jpg" class="thumbnail" width="84%">

Anybots research robots Monty (left) and Dexter (right)

</center>

<br>
<br>

##Super_robert and Anystats

Super_robert is a program that attempted to procedurally log into robots out in the field, pull down their logs and compute some information about them. This information was then passed over to Anystats, which statistically tracked, analyzed and prioritized the different events that appeared in the logs. 

Depending on what state a robot was in, how long it had been that way, what the logs showed, etc., bugs and faults could be automatically tracked and diagnosed. There were several cases where a bug would be affecting robots in our office, and it was useful to see if the same bug was affecting robots worldwide. Additionally, if the robot in question was in the hands of a customer and we did discover something wrong with it, we could be proactive and contact that customer to let them know we were aware of the problem and working to fix it. Another useful feature is the ability to keep ranks of healthiest robots, sickest robots, etc. that could be broken down into sub-groups like hardware revision, location, etc. 

<br>
<br>

##Features

Some highlights of the system are:

- Present all information in an intuitive manner through a web interface
- Automatically sent daily global fleet status emails to engineering team
- Used google APIs to store data in existing google docs spreadsheets and generate attractive charts
- Kept track of "deltas" for all robots (e.g if a robot was online yesterday and offline today, we would be notified)
- Maintained various rankings for most healthy robots, sickest robots, robots with a specific error, etc.

<br>
<br>

##Other Work at Anybots

Working with the actual codebase for the robot was tough because it was very large, several years old and I only had a few months there. However, I did developed some UI features for the touchscreen on the forehead of the robot, including a "dashboard" to display internal robot device health and connectivity. I also wrote call screen to allow users to answer or deny calls made to their robot.

{{disable comments}}
