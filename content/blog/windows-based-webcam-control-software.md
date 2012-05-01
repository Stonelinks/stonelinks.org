#Windows Based Webcam Control Software
09/30/2010

**Edit:** This is old. It is also the first implementation of my remote-controlled camera... under windows. It is really really bad and nobody should use it. However, I thougt I was pretty cool when I made it, and maybe it will be useful to somebody here, so I'll leave it up. I put a much more improved version this software to use on [the border patrol robot]({{wr}}static/misc/IED_tech_report_final.pdf). Check out page 48 of the report to see the final results and the page 118 for the code behind it.

##Intro

I love nothing more in life than creating and tinkering with the stuff around me. Over the years, this love has taken many different forms. It started out somewhere in elementary school with Legos and taking stuff apart and has evolved over the years into weekend projects such as the one you see here. [![image]({{wr}}static/img/old/2010-02-08-193147-150x150.jpg "2010-02-08-193147")]({{wr}}static/img/old/2010-02-08-193147.jpg)

One weekend early in the semester, I found myself with some rare free time and so I chose to make my own internet-aware pan-tilt fixture for my webcam. To my room mates [delight](http://en.wikipedia.org/wiki/Sarcasm), I have placed the controls on this website. Projects such as this are just the kind of thing that I love taking time to do. They span concepts that go from very low level micro controller programming to high level web programming, using all sorts of code and hardware as intermediaries. It required quite a lot of different skill sets and knowledge of systems integration to work. I'll describe how I did it starting very low level at the and working my way up.

##Step 0: The Hardware

###The Microcontroller

[![image]({{wr}}static/img/old/2010-02-08-193359-150x150.jpg "2010-02-08-193359")]({{wr}}static/img/old/2010-02-08-193359.jpg)

This summer I came into possession of an [Arduino](http://www.arduino.cc/) micro controller and [some servos](http://www.rcuniverse.com/product_guide/servoprofile.cfm?servo_id=67). As you can see from the pictures, I connected the servos up to the micro controller, making Y-cables for the power, ground, and signal pins of the servos. I also added a laser diode for good measure. All output pins were of course wired to the digital I/O port on the controller. Once I had everything wired up, I stuffed the Arduino in a metal box I had lying around and hot glued everything together. Predictably, the webcam itself did not require much work. It was actually given to me for free! (previous owner couldn't find drivers for it). All in all, this was not complicated to build at all and has performed very well for what it was designed to do.

* * * * *

###The Web Server

[![image]({{wr}}static/img/old/2010-02-08-193241-150x150.jpg "2010-02-08-193241")]({{wr}}static/img/old/2010-02-08-193241.jpg)

The Arduino is cool and all, but since the ultimate goal of this project is to control it over the internet, having a web server is an obvious requirement. Unfortunately for me, my web server also happens to be my self-built desktop that I use for almost all my engineering work. Because of this, I need access to few applications ( Solidworks, LabVIEW, Photoshop, Steam, etc.. ) that are only available for Windoze. Therefore I am forced into the unfortunate position of hosting this website and making this project work under Windows 7. This is an example of [the wrong tool for the job](http://www.burtonco.com/xsites/Appraisers/burtonco1/content/uploadedFiles/wrong%20tool.jpg), and it actually caused me quite a lot of headaches down the line. In the future when I have another computer to spare and improve on this project, I will use the [right tool](http://blog.taragana.com/wp-content/uploads/2008/03/linux-logo.jpg). After all that rambling, you're probably wondering how I have my web server configured. The only relevant details are that I am running [WampServer](http://www.wampserver.com/en/) with PHP 5.3.0 with short tags enabled.

* * * * *

##Step 1: Establishing Basic Control of the Camera

* * * * *

###Microcontroller Code

I wrote the following code to establish basic control of the Arduino over its USB to serial adapter. The comments explain what is going on, but for further background reading you can check out this about[PWM control](http://en.wikipedia.org/wiki/Pulse-width_modulation) and this about [what EEPROM is](http://en.wikipedia.org/wiki/EEPROM). Sorry ahead of time that the formatting of the code is all mangled, it was the best I could do.

<pre>
/*
 * File:          pantilt.c
 * Description:   An program for asynchronously controlling
 *          servos (via EEPROM and PWM) for use on a pan / tilt
 *          setup on my robot
 * Author:          Lucas Doyle
 * Creation Date:   October 16, 2009
 * Revision Date:   Jan 31, 2010
 */

// Since the Arduino resets itself every time a serial connection is
// made in windows (if you're writing characters from PHP or something),
// I have chosen to use the Arduinos EEPROM to store the positions
// between resets. Therefore we include the EEPROM header.

#include EEPROM

// variables dealing with the pins
char servoPinX    =  2;    // control pin for the first servo
char servoPinY    =  3;    // control pin for the second
char laserpin     = 13;    // the camera has a little laser diode on it

// PWM variables
int minPulseX    =  600;  // minimum servo position
int maxPulseX    =  2400; // maximum servo position
int minPulseY    = 500;   // same thing for other servo
int maxPulseY  = 1850;
char turnRate     =  100;  // servo turn rate increment (larger value, faster rate)
char refreshTime  =  20;   // time (ms) between pulses (50Hz)

// The Arduino will calculate these values
int centerServoX;         // center servo position
int centerServoY;
int pulseWidthX;          // servo pulse width
int pulseWidthY;
char moveServo;            // raw user input

long lastPulse   = 0;     // recorded time (ms) of the last pulse

// mode variables
int laseron      = 0;     // start out with the laser off by default
int partymode    = 0;     // party mode, some stupid idea i had to have the camera
        // spaz out and strobe the laser, has not been written yet
        // because i have not had time

// This function writes an int to eeprom at p_address
// Adapted from Marc Cardinals work:
// http://blog.ncode.ca/wp-content/uploads/2008/08/eeprom-int-readwrite.pde
void EEPROMWriteInt(int p_address, int p_value)
{
  byte lowByte = ((p_value >> 0) & 0xFF);
  byte highByte = ((p_value >> 8) & 0xFF);

  EEPROM.write(p_address, lowByte);
  EEPROM.write(p_address + 1, highByte);
}

// This function reads the int back
// Also adapted from Marc Cardinals work:
// http://blog.ncode.ca/wp-content/uploads/2008/08/eeprom-int-readwrite.pde
unsigned int EEPROMReadInt(int p_address)
{
  byte lowByte = EEPROM.read(p_address);
  byte highByte = EEPROM.read(p_address + 1);
  return ((lowByte << 0) & 0xFF) + ((highByte << 8) & 0xFF00); }
  
  
void setup()
{
  // Set up servo and laser pins as an output  
  pinMode(servoPinX, OUTPUT);  
  pinMode(laserpin, OUTPUT);
  pinMode(servoPinY, OUTPUT);  
  
  // calculate center positions for both servos  
  centerServoX = maxPulseX - ((maxPulseX - minPulseX)/2);  
  centerServoY = maxPulseY - (((maxPulseY - minPulseY)/2)-280);  
  
  // If you're running this for the first time on your arduino,  
  // uncomment the next two lines to initialize the EEPROM
  // EEPROMWriteInt(0, centerServoX);  
  // EEPROMWriteInt(2, centerServoY);  
  
  pulseWidthX = EEPROMReadInt(0);  
  pulseWidthY = EEPROMReadInt(2);  
  
  // begin serial communication  
  Serial.begin(9600);  
  
  //Serial.println("Arduino Serial Pan/tilt Control");
  //Serial.println("Standard WASD to move, spacebar to center");
  //Serial.println("L toggles the laser, TFGH goes to the extremes");
}

void loop()
{  
  // wait for serial input
  if (Serial.available() > 0)
  {
    // read the incoming byte:
    moveServo = Serial.read();

    // if party mode is off, read in commands
    //if (partymode == 0)
    {
      //if (moveServo == (char) " ") {/*nothing happens*/}

      // move left
      if (moveServo == 'a') { pulseWidthX = pulseWidthX - turnRate; }

      // move right
      else if (moveServo == 'd') { pulseWidthX = pulseWidthX + turnRate; }

      // move up
      else if (moveServo == 'w') { pulseWidthY = pulseWidthY - turnRate; }

      // move down
      else if (moveServo == 's') { pulseWidthY = pulseWidthY + turnRate; }

      // center
      else if (moveServo == 'c') { pulseWidthX = centerServoX; pulseWidthY = centerServoY;}

      // move hard left
      else if (moveServo == 'f') {pulseWidthX = minPulseX; }

      // move hard right
      else if (moveServo == 'h') {pulseWidthX = maxPulseX; }

      // move hard up
      else if (moveServo == 't') {pulseWidthY = minPulseY; }

      // move hard down
      else if (moveServo == 'g') {pulseWidthY = maxPulseY; }

      // toggle the laser
      else if (moveServo == 'l')
      {
        if (laseron == 0) { digitalWrite(laserpin, HIGH); laseron = 1; }
        else if (laseron == 1) { digitalWrite(laserpin, LOW); laseron = 0; }
      }
    }

    // however if party mode is enabled
    //else if (partymode == 1)
    //{
      // do some awesome stuff (not yet implemented)
    //  Serial.print("Party!!! ");
    //}

    // party mode
    //else if (moveServo == 'p')
    //{
    //  if (partymode == 0) { partymode = 1; }
    //  else if (partymode == 1) { partymode = 0; }
    //}
  }

  // stop servo pulse at min and max
  if (pulseWidthX > maxPulseX) { pulseWidthX = maxPulseX; }
  if (pulseWidthX < minPulseX) { pulseWidthX = minPulseX; }
  if (pulseWidthY > maxPulseY) { pulseWidthY = maxPulseY; }
  if (pulseWidthY < minPulseY) { pulseWidthY = minPulseY; }
  
  // print pulseWidth back to the Serial Monitor (uncomment to debug)
  // Serial.print("Pulse Width: ");
  // Serial.print(pulseWidth);
  // Serial.println("us");   // microseconds
  
  // pulse the servo every 20 ms (refreshTime) with current pulseWidth
  // this will hold the servo's position if unchanged, or move it if changed
  if (millis() - lastPulse >= refreshTime)
  {
    EEPROMWriteInt(0, pulseWidthX);
    EEPROMWriteInt(2, pulseWidthY);

    digitalWrite(servoPinX, HIGH);   // start the pulse
    delayMicroseconds(pulseWidthX);  // pulse width
    digitalWrite(servoPinX, LOW);    // end the pulse

    digitalWrite(servoPinY, HIGH);   // start the pulse for servo 2
    delayMicroseconds(pulseWidthY);  // pulse width
    digitalWrite(servoPinY, LOW);    // stop the pulse

    lastPulse = millis();            // save the time of the last pulse
  }
}
</pre>

##Establishing Serial Communication

* * * * *

If you load the above code into the Arduino's IDE and download it on to your controller, you end up with a nice, intuitive way of manually controlling your pan / tilt mechanism. You can try things out by opening the Serial Monitor in the Arduino IDE and moving around using WASD, or move to the extremes using TFGH. Pressing 'C' centers the camera back and 'L' [fires the laser](http://spf.fotolog.com/photo/47/10/95/vanguardista2104/1211331863_f.jpg). Arguably, you could stop here and technically still have a way of controlling the camera over the internet with the power of linux. All one would need to do is open up a terminal or ssh into a remote workstation and run the following command:

<pre>
 ~$ screen /dev/ttyUSB0
</pre>

This was not good enough for me though, as I wanted to control this through a web browser, which brings us to...

* * * * *

##Step 2: Interfacing with the Internet

* * * * *

###Nightmare in PHP land

I thought this would be easy. Since PHP is a server side scripting language, it has libraries that allow it to read and write to and from serial ports. So one would think that the following would work:

<pre>
$fp =fopen("COM3", "w");
fwrite($fp, chr('c')); // write your character to the Arduino here
sleep(1);
fclose($fp);
</pre>

However, for reasons I do not completely understand, this did not work for me under Windows 7, but it did with Linux (substituting COM3 for /dev/ttyUSB0 of course). This problem persisted, as I also tried using the [PHP serial class](http://www.phpclasses.org/browse/package/3679.html), but it too proved to be equally as ineffective. I finally circumvented the need for PHP to communicate with the COM port entirely by compiling several very basic exe's in [processing](http://processing.org/) that sent commands to the Arduino and then called them using the exec() function in PHP. This, while extremely inefficient, was the quickest, most reliable, consistent and intuitive solution to my problem. Of course, this would all have been avoided in the first place had I been using Linux, as PHP has no problem writing to /dev/ttyUSB0 like it would a normal file, such as in my example above.

* * * * *

##Building the Webpage

By using the [PHP $\_GET](http://www.w3schools.com/PHP/php_get.asp) function, I was able to incorporate controls into a webpage. The PHP included in the header of the page is shown here:

<pre>
//check the GET action var to see if an action is to be performed
if (isset($_GET['action']))
{
   //Action required! Build our command...
   $basecmd = "F:\\wamp\\www\\luke\\Projects\\personal_robot\\personal robot\\commands\\";
   $cmd = $basecmd . $_GET['action'] . "\\application.windows\\" . $_GET['action'] . ".exe";
   exec($cmd);
}
</pre>

And the HTML I used to create a basic control panel is simply a 3x3 table with some hyperlinks to the right URLs to control PHP.

* * * * *

##Step 3: Enjoy your Remote Webcam!

###Remarks

To manage the webcam feed, I am using a program called [Fwink](http://www.lundie.ca/fwink/) to take a picture every second and then using AJAX to automatically refresh the image once the page is loaded. However, there are hundreds of ways to manage a webcam feed and the details of how you do it is out of the scope of what I'm talking about here.

* * * * *

##Conclusions / Future Improvements

As expected, performance with this setup is less than impressive, although I have no doubts in my mind it is due to the wonky way in which I have to execute system calls to run the Processing exe's. For the future, as this is a rough prototype, it can and will be running a lot faster under Linux. Additionally, this is the vision component to my personal robot, and its brains (a first generation ASUS eeepc netbook) are currently on loan to a friend of mine. Next time I see him I'll get the machine back and we'll start cooking with gas! (and by gas I mean Linux).
