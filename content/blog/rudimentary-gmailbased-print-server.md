#Rudimentary Gmail-based Print Server
01/26/2011

Another example of python being super useful. I found myself today with a need to network a printer so my room mates and I could print from anywhere on campus. However, figuring out what ports to forward, trying to get IPP to work and just being generally unhappy with CUPS and the way RPIs network restricts printer traffic / discovery lead me to consider alternate solutions.

Enter python and Gmail! I wanted to be able to have someone email me a message with a few keywords in the subject line that would tag any attachments for printing. I then had python log into my email and download the most recent email for printing, and if the attachment was new to it, print it. I wrote a nice little script that does just that:

[Here it is on github](https://github.com/Stonelinks/gmail-printsrv)

All you gotta do is edit the username and password at the top of the script, and set up a cron job to call the script on the machine with the printer attached.

A couple of other comments about this: It is dangerous! Someone could email you a file with a malformed name and escape out of the print command that gets called by the subprocess. Not good. There are probably other security risks (like the fact that your password is stored in plaintext). Thats it! have fun kids!
