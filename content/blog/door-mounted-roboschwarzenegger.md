#Door Mounted Robo-Schwarzenegger

<a href="{{wr}}static/img/old/downsize_4.jpg"><img class="aligncenter size-medium wp-image-861" title="downsize_4" src="{{wr}}static/img/old/downsize_4-225x300.jpg" alt="" width="225" height="300" /></a>I don't get to fool around with my own projects nearly as much as I would like, but this weekend I did devote a few hours to finishing up a robotic internet controlled camera on our apartment door. The pre-existing peep hole didn't exactly work, and I'm tired of people knocking and having no idea who is at the door, so I felt like this was an appropriate solution. The story of exactly how and why I made this thing can find their roots back in the summer.

One day in August I had this idea of creating a Generic Web Enabled Robotic Operating System (GWEROS... yeah I know it's a pretty stupid sounding acronym, give me a break) that would essentially allow you to create an awesome, high functioning robot out of a wide variatey of off the shelf hardware so long as it had a few basic things: a web server, a webcam, a serial port attached to a micro controller (arduino, pic, whatever) and some servos, motors, wheels or whatever. The aspiring robot enthusiast would cobble together whatever hardware he or she can manage, install GWEROS (make the install/update process simple like <a href="http://codex.wordpress.org/Installing_WordPress">wordpress</a>) and be up and running in no time. Basically it would be like a less hardcore version of <a href="http://www.ros.org/wiki/">ROS</a> (which is totally badass) for use exclusively in the browser.

I even think if done properly and given enough time to gather community support, people much smarter than myself could write plugins that would allow GWEROS users to do powerful things with their robots <a href="http://mjpg-streamer.svn.sourceforge.net/viewvc/mjpg-streamer/mjpg-streamer/www/javascript_motiondetection.html?revision=83&amp;view=markup&amp;pathrev=83">from their web browser</a> typically reserved high end or high price robots.

Needless to say it was a bit ambitious for a project for the middle of summer and while I wish I had the time to pour into making it a reality, I had more than enough on my plate at the Center for Astrophysics. Therefore I only started writing the interface and just finished writing some basic camera / telemetry code this weekend. The end result is what you see here:

<a href="{{wr}}static/img/old/downsize_2.jpg"><img class="alignnone size-thumbnail wp-image-859" title="downsize_2" src="{{wr}}static/img/old/downsize_2-150x150.jpg" alt="" width="150" height="150" /></a><a href="{{wr}}static/img/old/downsize.jpg"><img class="alignnone size-thumbnail wp-image-858" title="downsize" src="{{wr}}static/img/old/downsize-150x150.jpg" alt="" width="150" height="150" /></a><a href="{{wr}}static/img/old/downsize_3.jpg"><img class="alignnone size-thumbnail wp-image-860" title="downsize_3" src="{{wr}}static/img/old/downsize_3-150x150.jpg" alt="" width="150" height="150" /></a><a href="{{wr}}static/img/old/Screenshot.png"><img class="alignnone size-thumbnail wp-image-864" title="Screenshot" src="{{wr}}static/img/old/Screenshot-150x150.png" alt="" width="150" height="150" /></a>

The best part about it? Nobody even knows it's there because it is disguised as Arnold Schwarzenegger.