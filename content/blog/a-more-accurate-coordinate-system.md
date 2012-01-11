#A More Accurate Coordinate System

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="src" value="http://www.youtube.com/v/c72tK4KTTj0?fs=1&amp;hl=en_US" /><param name="allowfullscreen" value="true" /><embed type="application/x-shockwave-flash" width="480" height="385" src="http://www.youtube.com/v/c72tK4KTTj0?fs=1&amp;hl=en_US" allowscriptaccess="always" allowfullscreen="true"> </embed></object>
<h3><strong>Intro</strong></h3>
<hr />Unfortunately RPI health and safety inspections did not take as kindly to my <a href="http://stonelinks.org/?p=856">door mounted Robo-Schwarzenegger</a> as I would have hoped. Apparently having a computer and a camera mounted to your door is fine, and so is having the whole affair viewable and controllable from any internet browser on campus, but the power cord across the doorway is a tripping hazard. Whether I agree with this or not, I took it down and brought the bot home with me over the break with the goal of teaching myself some python and jumping into OpenCV.

I played with both OpenCV and Python a few years ago when I more or less <a href="http://blog.jozilla.net/2008/06/27/fun-with-python-opencv-and-face-detection/">followed this tutorial</a>, but ultimately could not garner decent control of the camera (lack of sophistication in protocol design by me between the PC / microcontroller). Also, the script I wrote had a memory leak I didn't know how to fix, presumably because I was a python noob. Don't get me wrong, I still am a python noob, just slightly less of one after the improvements described here.

As you can see from the video, I have pretty good control over where the camera points. This was accomplished with a rewrite of the code running on the Arduino as well as python running on the PC. First I'll talk about the Arduino and then the python.<!--more-->
<h3><strong>The Arduino</strong></h3>
<hr />The old way I had of doing things on the Arduino was very simplistic and took no advantage of any Arduino libraries. Essentially the protocol between the computer and the arduino was a single character corresponding to a single action. Like many modern PC games, movement of the camera was set up in standard WASD fashion ("W" moved the Y axis up, "S" moved it down, "A" moved the X axis left, etc). From a programming perspective, this was trivial to code: an if-else block that would do things like "if W comes down the serial line, increment the current Y pulse width by 10". At the end of the if-else block, if it was time to make a pulse the program would bring the pins connected to the servo high, wait for the pulse width, then bring it back low. There was also a hard coded center, and limits set up so the servos did not go past their limits. All in all, very simplistic, but it got the job done.

The new way of doing things is a little more complicated, but is much more useful in terms of precision. It takes inspiration from this <a href="http://principialabs.com/arduino-python-4-axis-servo-control/">wonderful tutorial</a> to take advantages of the Arduino servo libraries and simplify things. First, a three part protocol between the PC and Arduino is established:
<ol>
	<li><span>The PC sends a '255' to the Arduino to let it know that we want to move servos. This is good for future expansion because we can use 0-254 to do other things with the micro-controller. For example, send something like '254' to move speed controllers or get a reading from a GPS.</span></li>
	<li><span>The PC sends a number corresponding to the index of a servo on the Arduino. In my setup, 1 means the X axis and 2-means the Y axis. This tells the Arduino what servo to move.</span></li>
	<li><span>Last, an angle between 0 and 180 is sent telling the Arduino where to move the servo.</span></li>
</ol>
Very simply, number two in that list is used to pick a servo object to apply the <a href="http://arduino.cc/en/Reference/ServoWrite">write()</a> function that takes the angle in number three as its argument. The Arduino does the rest! There is a catch though -- in order for the Arduino to properly instantiate a servo object, you need to use the attach() function. Since there are minimum and maximum pulse widths (hardware limits) we care about so the pan tilt module doesn't rip itself apart, those minimum and maximum pulse widths need to be known. I actually used the old version of my code and a couple print statements to write a diagnostic program I could use to figure out the pulse width limits. I have that attached as well as the real code.
<h3><strong>The Python</strong></h3>
<hr />Now not to diss PHP or anything, but python just seems like a more grown up scripting language. There is a lot to like about it. Every time I read or hear about something cool being done, it is almost always involves python! So far with the tutorials out there it has been awesome. The python segments here are short and not very advanced.

I wrote one important function - move(). It takes an angle and a servo as arguments and -- you guessed it -- moves the specified servo to their specified angle. One problem though -- due to me being an imperfect craftsman and not mounting the servos perfectly straight, the angular position of 90,90 does not make the camera point straight ahead as one would expect. Therefore I wrote another simple diagnostic function to allow the interactive centering of the servos. Once I had the middle for the X and Y axis, I could use this in the move function to shift the centers:

<code> # hardware corrections for pantilt
# shift angle according according to measured centers
if (servo == 1) : middle = 99
if (servo == 2) : middle = 118
angle = angle + middle - 90</code>

<code># truncate angle to something realistic
if (angle &lt; 0) : angle = 0
if (angle &gt; 180) : angle = 180</code>

<code> </code>

<code> # write the angle to the serial port
ser.write(chr(angle))
</code>

Once move was done, I wrote some test code and it worked like a champ! I then started stacking calls to move() inside of loops and I wrote some code to make the camera move in simple rectangles. Some problems then became clear: the pan tilt module either moves too slow, too fast or just spazzes out if you issue enough commands to it. Increasing the baud rate helped to speed things up, however it would still freak out if you told it to move really fast. I determined that there needs to be some delay between move() calls. Once again, I wrote some diagnostic code to determine this. The pan tilt module would move in rectangles with increasingly longer pauses between move() calls. At some critical delay value, the pan tilt module stopped jittering and moved smoothly (but still pretty fast) around the perimeter of the rectangle (turned out to be .003 seconds).

As a final example of what the system can do, I wrote the spiral code that appears in the video above. It is only a few lines of python, but I spaced them out and commented them for ease of understanding:

<code>a = .01;  # "stretch" factor for sin and cosine
t = 0;    # time value</code>

<code># time loop that stops when the stretch factor is 1
while (a &lt; 1) :</code>

<code># increase the time step
t+=1</code>

<code># if 50 time steps have gone by, increment a
if (t % 50 == 0) : a+=.01

# move the servos to middle, plus or minus some scaled
# value of sin or cosine. Change 'a' to something fixed
# between 0 and 1 and the spiral is now a circle
servo.move(1, 90 + a * math.degrees(math.cos(math.radians(t))))
servo.move(2, 90 + a * math.degrees(math.sin(math.radians(t))))

</code>

<code> # delay between the move calls
time.sleep(.0045)
</code>
<h3><strong>Conclusion &amp; Attachments</strong></h3>
<hr />So that was it! Now I have unrestricted access to use python to do {almost} whatever I want! Looking at the python bindings for OpenCV next!

<a href="http://dl.dropbox.com/u/4428042/stonelinks_public/main.cpp">Arduino main code</a>
<a href="http://dl.dropbox.com/u/4428042/stonelinks_public/servolimits.cpp">Arduino servo pulsewidth diagnostic code</a>
<a href="http://dl.dropbox.com/u/4428042/stonelinks_public/main.py">Python main code</a>
<a href="http://dl.dropbox.com/u/4428042/stonelinks_public/servo.py">Python servo module</a>
