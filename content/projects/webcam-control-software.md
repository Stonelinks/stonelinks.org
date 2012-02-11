#Webcam Control Software

***This is old. Look at posts if you want to see current versions of my projects. This is the first implementation of my remote-controlled camera... under windows. It is ugly and inefficient as sin, but I thougt I was pretty cool when I made it, and maybe it will be useful to somebody here, so I'll leave it up ***

##Introduction

I love nothing more in life than creating and tinkering with the stuff around me. Over the years, this love has taken many different forms. It started out somewhere in elementary school with Legos and taking stuff apart and has evolved over the years into weekend projects such as the one you see here.

[![image]({{wr}}static/img/old/2010-02-08-193147-150x150.jpg "2010-02-08-193147")]({{wr}}static/img/old/2010-02-08-193147.jpg)
One weekend early in the semester, I found myself with some rare free time and so I chose to make my own internet-aware pan-tilt fixture for my webcam. To my room mates [delight](http://en.wikipedia.org/wiki/Sarcasm), I have placed the [controls]({{wr}}?page_id=114) on this website. Projects such as this are just the kind of thing that I love taking time to do. They span concepts that go from very low level microcontroller programming to high level web programming, using all sorts of code and hardware as intermediaries. It required quite a lot of different skill sets and knowledge of systems integration. I'll describe how I did it starting very low level at the and working my way up

##Step 0: Initial Setup

* * * * *

###The Microcontroller

[![image]({{wr}}static/img/old/2010-02-08-193359-150x150.jpg "2010-02-08-193359")]({{wr}}static/img/old/2010-02-08-193359.jpg)

This summer I came into possession of an [Arduino](http://www.arduino.cc/) micro controller and [some servos](http://www.rcuniverse.com/product_guide/servoprofile.cfm?servo_id=67). As you can see from the pictures below, I connected the servos up to the micro controller, making Y-cables for the power, ground, and signal pins of the servos. I also added a laser diode for good measure. All output pins were of course wired to the digital I/O port on the controller.

Once I had everything wired up, I stuffed the Arduino in a metal box I had lying around and hot glued everything together. Predictably, the webcam itself did not require much work. It was actually given to me for free! (previous owner couldn't find drivers for it). All in all, this was not complicated to build at all and has performed very well for what it was designed to do.

###The Web Server

[![image]({{wr}}static/img/old/2010-02-08-193241-150x150.jpg "2010-02-08-193241")]({{wr}}static/img/old/2010-02-08-193241.jpg)
The Arduino is cool and all, but since the ultimate goal of this project is to control it over the internet, having a web server is an obvious requirement. Unfortunately for me, my web server also happens to be my self-built desktop that I use for almost all my engineering work. Because of this, I need access to few applications ( Solidworks, LabVIEW, Photoshop, Steam, etc.. ) that are only available for Windoze. Therefore I am forced into the unfortunate position of hosting this website and making this project work under Windows 7. This is an example of [the wrong tool for the job](http://www.burtonco.com/xsites/Appraisers/burtonco1/content/uploadedFiles/wrong%20tool.jpg), and it actually caused me quite a lot of headaches down the line. In the future when I have another computer to spare and improve on this project, I will use the [right tool](http://blog.taragana.com/wp-content/uploads/2008/03/linux-logo.jpg).

After all that rambling, you're probably wondering how I have my web server configured. The only relevant details are that I am running [WampServer](http://www.wampserver.com/en/) with PHP 5.3.0 with short tags enabled.

##Step 1: Establishing Basic Control of the Camera

* * * * *

###Microcontroller Code


I wrote the following code to establish basic control of the Arduino over its USB to serial adapter. The comments explain what is going on, but for further background reading you can check out this about[PWM control](http://en.wikipedia.org/wiki/Pulse-width_modulation) and this about [what EEPROM is](http://en.wikipedia.org/wiki/EEPROM). Sorry ahead of time that the formatting of the code is all mangled, it was the best I could do.

###Establishing Serial Communication

If you load the above code into the Arduino's IDE and download it on to your controller, you end up with a nice, intuitive way of manually controlling your pan / tilt mechanism. You can try things out by opening the Serial Monitor in the Arduino IDE and moving around using WASD, or move to the extremes using TFGH. Pressing 'C' centers the camera back and 'L' [fires the laser](http://spf.fotolog.com/photo/47/10/95/vanguardista2104/1211331863_f.jpg).

Arguably, you could stop here and technically still have a way of controlling the camera over the internet with the power of linux. All one would need to do is open up a terminal or ssh into a remote workstation and run the following command:

 ~$ screen /dev/ttyUSB0 

This was not good enough for me though, as I wanted to control this through a web browser, which brings us to...

##Step 2: Interfacing with the Internet

* * * * *

##Nightmare in PHP land

I thought this would be easy. Since PHP is a server side scripting language, it has libraries that allow it to read and write to and from serial ports. So one would think that the following would work:

$fp =fopen("COM3", "w");
fwrite($fp, chr('c')); // write your character to the Arduino here
sleep(1);
fclose($fp);

However, for reasons I do not completely understand, this did not work for me under Windows 7, but it did with Linux (substituting COM3 for /dev/ttyUSB0 of course). This problem persisted, as I also tried using the [PHP serial class](http://www.phpclasses.org/browse/package/3679.html), but it too proved to be equally as ineffective.

I finally circumvented the need for PHP to communicate with the COM port entirely by compiling several very basic exe's in [processing](http://processing.org/) that sent commands to the Arduino and then called them using the exec() function in PHP. This, while inefficient, was the most reliable, consistent and intuitive solution to my problem. Of course, this would all have been avoided in the first place had I been using Linux, as PHP has no problem writing to /dev/ttyUSB0 like it would a normal file, such as in my example above.

###Building the Webpage

By using the [PHP $\_GET](http://www.w3schools.com/PHP/php_get.asp) function, I was able to incorporate controls into a webpage. The PHP included in the header of the page is shown here:

//check the GET action var to see if an action is to be performed
if (isset($_GET['action']))
{
    //Action required! Build our command...
   $basecmd = "F:\\wamp\\www\\luke\\Projects\\personal_robot\\personal robot\\commands\\";
   $cmd = $basecmd . $_GET['action'] . "\\application.windows\\" . $_GET['action'] . ".exe";
        exec($cmd);
}

And the HTML / PHP I used to create a basic control panel is shown below. Note the use of short tags in the hyper links. Again wordpress absolutely massacred my formatting on this for some reason.

##Step 3: Enjoy your Remote Webcam!

###Remarks

To manage the webcam feed, I am using a program called [Fwink](http://www.lundie.ca/fwink/) to take a picture every second and then using simple AJAX to automatically refresh the image once the page is loaded. However, there are hundreds of ways to manage a webcam feed and the details of how you do it is out of the scope of what I'm talking about here.

* * * * *

##Conclusions / Future Improvements

As expected, performance with this setup is less than impressive, although I have no doubts in my mind it is due to the wonky way in which I have to execute system calls to run the Processing exe's.

For the future, as this is a rough prototype, it can and will be running a lot faster under Linux. Additionally, this is the vision component to my personal robot, and its brains (a first generation ASUS eeepc netbook) are currently on loan to a friend of mine. Next time I see him I'll get the machine back and we'll start cooking with gas! (and by gas I mean Linux).
