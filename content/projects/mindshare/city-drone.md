#City Drone

<hr>

<b>Guest at 2010-06-04 06:52:03:</b><br /><br />

I think it would be a cool idea to make a robot that either roved around the city at night autonomously (aggregating data or something) or was driven by a user.

The main thing I am interested in is how to get good control over the robot VIA the internet. With my experience so far, I am mostly used to having the robot automatically connect to a wireless network. So far things have worked out pretty well because I've been on college campuses where one giant network usually blankets an area that the robot operates in.

I'd like to develop a system that gets around this for the robot. Basically, as the robot drives through the city it updates it's IP address based on which wifi networks it can access.

How it will access networks:

Walking around an area like Cambridge and looking at the numerous networks, it is easy to see that they all have varying degrees of security. For the spirit of this project i'm going to avoid using the harvard wireless network as much as possible.

Connection logic:

For each wireless connection successfully made (i'll define 'successful' as able to send and receive HTTP), the robot must do the following:

- Forward the relevant ports (namely port 80, maybe 22 for SSH, maybe some other port for a webcam stream) to itself on the router (using UPnP probably). This is not necessary when the connection metric of the wireless interface is 0 (meaning that the robot is connected directly to the internet). This is easy to test for in linux. 
- Register the WAN IP of the router with some DNS server so that I can go to a domain and control the thing despite the ever-changing IP address as it drives out of range in one network. The annoying thing is that DNS servers are usually slow (ttl is usually like 60 seconds) which means that there will be delays between each network change that will be as long as it takes to successfully connect, and then contact the DNS server.

Now for the connection logic itself. The key problem being solved here is how to automatically and forcefully connect to a wireless network. We are making assumptions about these networks: That they are sufficiently dense such that some are left unsecured or partially secured and are therefore able to be used by the robot. We are also assuming the network topology is random. This means that every time the robot goes out of range on a network that was working for it, it needs to re-figure everything out to establish a new reliable connection. This means that some kind of decision making priority structure needs to be established (calling that the connection logic). For example, the best case scenario (and therefore the first thing the robot would test for when making a networt hop) would be an unsecured network with high signal strength. The worst case scenario (and lowest on the priority) is that it cannot find anything to use and therefore must reconnect to and remain in the old networks range.

Actions after a network hop is to be made:

- An unsecured wireless network with a decent signal strength exists within the vicinity of the robot. Connect to it, attempt to establish internet connection. Forward the appropriate ports. If two way traffic is accomplished, then update the DNS with the current IP and quit (successful).
- If above fails at any point, try to find a network in range with decent signal strength that is secured with WEP. Attempt to crack this with aircrack. If successfully cracked, again attempt to establish internet connection. Forward the appropriate ports. If two way traffic is accomplished, then update the DNS with the current IP and quit (successful).
- If above fails, reconnect to the old network and notify the user that the hop was unsuccessful

The robot should probably aggregate information in a database as it goes along. Things like network names, types, locations (GPS?) would be useful. Considerations also need to be made for bandwidth usage. We want the UI to be useful but not wasteful. Upstream speeds on most home modems are pitifully low. Last, this may seem like solving a problem that does not exist because you could get around all of this by using 3g. My answer to that is that I don't want to pay for a data plan and have to worry about tethering and whatnot. Besides with 3g you lack anonymity. The ever-changing IP address model ensures that the robot is using other peoples IP address to connect and can't easily be traced back to someone. Besides this whole thing is a very good exercise in automation, linux, and networking protocols.

It is undoubtedly a huge project, but I already have most of the hardware and some of the knowledge and software to do this.

Thoughts? <hr>

<b>Guest at 2010-06-04 07:11:30:</b><br /><br />

I should also say that if there are duplicates within type in the connection logic, it should prioritize based on signal strength.

So if these networks are in range of the robot:

<pre>
SSID     Protection     Strength
foo      WEP            89%
bar      none           30%
cake     WEP            30%
ass      none           40%
burgers  WEP            50%
feet     none           50%
</pre>

It should try establishing connections in this order:
feet
ass
bar
foo
burgers
cake

Depending on how long it takes to crack WEP I might change this to prioritize based on strength instead of type of protection. Also of worth noting is that anything other than WEP or no protection will be filtered out of the potential network pool (so things like WPA, 802.1x, WPA2, etc) wont show up as well as whatever the old network was. For instance if the above networks were again in range, however the robot had just come off the 'foo' network it would not consider it when making a new connection.

Another thing about the port forwarding. That may end up being a pain in the ass to do correctly. Maybe doing everything through UDP traffic would be better. This would, however, require major changes in the software. Part of the reason I want to do this project is because I already have software written to control the robot over a web browser. HTTP however is a TCP protocol so I would have to rewrite EVERYTHING which would not be cool.
