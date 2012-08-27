#Awesome Backup System
<center>

<br>

<img src="{{wr}}static/img/ABSlogo.png">

</center>

The The Awesome Backup System (ABS) is a cross platform file backup solution. It consists of a server and three native clients for OS X, Windows and Linux. They all communicate with the server through a common API. It was written for a Software Design and Documentation class at RPI in the fall of 2011 by Lucas Doyle, Peter Fernandes, Kevin Todisco and Jeff Hui. Because of this, the majority of the time making ABS was actually spent documenting things.

<br>

##Demo
###You can see and use ABS right now!
###Check out [stonelinks.org/ABS/](http://stonelinks.org/ABS/)
(Please don't fill my server up with crap!)

<br>

##Features

***Native clients:*** One of the design goals for ABS was that all clients are native to their platforms. We really wanted to stay away from cross platform tools like java or Qt for the GUI. Using these tools would have cut down on development time, but we felt that a customer's has the right to expect a certain look and feel to their applications that are consistent with the platform they are running on.
 
***API:*** A common API for our server was developed using django to allow different languages and platforms to use ABS, as well as enforce implementation consistency for all clients. The API includes features for uploading and downloading files, managing different computers, authentication, and more. Additionally, the development API makes it easy to add new clients without changing anything on the server.

***Minimal bandwidth usage:*** The API was also designed so that clients would only have to transfer the minimal amount of file content to the server. During a backup cycle, the client downloads a list of hashes from the server that correspond to files that have already been backed up. The client starts generating hashes for all the files it is currently trying to back up, and if any of them match the old hashes downloaded from the server, then that particular file is already backed up and the upload is skipped.

<br>

##Possible Future Improvements:

***Security:*** ABS is lacking is in the security department. It being more or less a prototype we wrote for a class, security wasn't the first thing we designed it for. Still, we are using HTTPS (though we feel like that alone isn't a very good security measure) and never store or transfer passwords in plaintext. In fact, because the clients (and HTTPS technically) are stateless entities, every API request needs to be authenticated for it to do anything. This means no cookies or any artifiact of your authentication other than a hashed password remains on the client.

***Minimize disk space:*** Similar to git and other version control systems, one of the ways we could cut down on disk storage space for files is storing incremental "diffs" for changes between backup cycles.

<br>

##Code

ABS is open source! See the code that runs ABS on github!
###[https://github.com/Lorem/ABS](https://github.com/Lorem/ABS)

{{disable comments}}
