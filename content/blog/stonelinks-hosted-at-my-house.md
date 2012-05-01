#Stonelinks Hosted at my House
12/21/2010

Looks like the kinks of my new [two-server](dr-serverlove-or-how-i-learned-to-stop-worrying-and-love-the-raid.html) setup are not ironed out. I just got home from RPI and the old Dell is acting wacky. I thoroughly checked both machines before I left for home, and I thought everything was okay. However, upon arriving home, I checked the web server to find that it doesn't work -- not even a 404 page or a time out error, the browser just hangs.

To use anything other than HTTP on port 80, I need to be on RIP's VPN. I log into the VPN and start with the basics. The machine (which is not behind a router) responds to ping, however ssh shows the same symptoms as apache. I don't even get a connection refused or path not found or timeout error, the login literally just hangs (I left it running for like 30 min now).

After being thoroughly baffled by this, I ran NMAP from another machine on the same network:

<pre>
[luke@void ~]$ nmap -A -T4 stonelinks.org
Starting Nmap 4.11 ( http://www.insecure.org/nmap/ ) at 2010-12-27 03:39 EST
Interesting ports on doylel2.stu.rpi.edu (128.113.38.125):
Not shown: 1676 closed ports
PORT    STATE SERVICE  VERSION
21/tcp  open  ftp?
22/tcp  open  ssh?
80/tcp  open  http?
111/tcp open  rpcbind?
</pre>

I have VPN access and control over other computers on the same network, but obviously no physical access to the machine. I have no idea what is going on here, my assumption is that the kernel is hanging on something, but I guess I'll find out when I get back. Because of the way RPI manages IP addresses, the firewall at RPI, and the uncertainty of the other computer, I'm hesitant to just tell my desktop to take the old MAC / IP for Stonelinks until I get back on campus in case I lose both machines. Luckily I had a backup of Stonelinks that I moved to my house. So until I get back on campus, I am hosting off my houses internet connection! Be warned in this time Stonelinks will be operating in a pretty crippled capacity.
