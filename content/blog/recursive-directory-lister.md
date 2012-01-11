#Recursive Directory Lister

<span style="color: #ff0000;">*edit* This is old. Look at posts if you want to see current versions of my projects. This was like the first thing of great significance I did with Stonelinks on my own (read: I didn't know what I was doing). Similar to the Windows based webcam thing, I thought it was a big deal at the time. Looking back it is funny how trivial this would be to implement nowadays. Oh also, there are things in here that are just plain wrong and/or bad practice (left as an exercise to the reader to find).</span>
<h3>Purpose and Demonstration</h3>
<hr />You may notice that I have little collapsible trees all over the place on this website. I wanted a quick, easy and effective way to integrate entire directories of files on my computer on to webpages. Wasn't really happy with anything currently out there, so I made this myself. However, using <a href="http://jquery.com/">jquery</a> made things extremely easy.<!--more-->
<h3>The HTML</h3>
<hr />Put this in your header! It loads the necessary files from the jquery treeview plugin. I recommend saving them somewhere local on your server.
<pre class="brush:html"><script src="/trees/jquery-latest.js"><!--mce:0--></script>
<script src="/trees/jquery.cookie.js" type="text/javascript"><!--mce:1--></script>
<script src="/trees/jquery.treeview.js" type="text/javascript"><!--mce:2--></script>
<script type="text/javascript"><!--mce:3--></script></pre>
<h3>The PHP</h3>
<hr />It doesn't matter where this goes, but calling the function getDirectory() will echo the tree back on to your webpage.
<pre class="brush:php">// Use this to format filesizes into things that are human readable.
function format_bytes($size) {
    $units = array(' B', ' KB', ' MB', ' GB', ' TB');
    for ($i = 0; $size &gt;= 1024 &amp;&amp; $i &lt; 4; $i++) $size /= 1024;
    return round($size, 2).$units[$i];
}

function getDirectory($path='.',$level=0)
{
	// ignore anything that appears in this array
	$ignore=array('cgi-bin','.','..');

	// open the directory handle at the given path
	$dh=@opendir($path);

	// if this is the first level, set the class of the unordered list to match our javascript stuff
	if($level == 0)
	{
		echo'
<ul id="tree" class="filetree">
	<li>
<ul>';
	}
	echo'<span>';

	// while there are still directories to read
	while(false!==($file=readdir($dh)))
	{
		// if we should not ignore it
		if(!in_array($file,$ignore))
		{
			// if it is a directory
			if(is_dir("$path/$file"))
			{
				// if we're over the first level
				if($level&gt;=0)
				{
					// display the folder closed by default
					echo'
	<li class="closed">';
				}
				else
				{
					// otherwise just use normal tags
					echo'</li>
	<li>';
				}

				// write the folder to the webpage
				echo'<span class="folder"><strong>',$file,'</strong></span>';

				// now recursively call the function again to [hopefully] display any other files / folders
				getDirectory("$path/$file",($level+1));

				// close tags from our first few echos
				echo"</li>
</span></ul>
</li>
';
	}
	else
	{
		// if this is our second or more time, just use a normal unordered list tag
		echo'

";
			}
			// it isnt a directory, so its a file
			else
			{
				// display a link to the file along with the filesize
				echo'
	<li><span class="default"><a href="; 				echo &quot;">',' ',$file,'</a>    ('.format_bytes(filesize( $path.'/'.$file)).')</span></li>
';
			}
		// end ignore case
		}
	// end while loop
	}
	// close the handle
	closedir($dh);

	// added this so people know they can contribute to files on stonelinks
	echo'<a href="../stonelinks-uploader">
<h2>Contribute</h2>
</a>';
}</ul>
</pre>
