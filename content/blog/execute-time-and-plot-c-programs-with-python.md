#Execute, Time and Plot C++ Programs with Python
02/03/2011

<center>
<img src="{{wr}}static/img/misc/Fig.png" class="thumbnail" width="80%">
</center>

Hate excel? Have python take all the pain away from you! This should appeal to everyone out there who needs a quick way to analyze the runtime time of a bunch of commands to a program given an arbitrary list of arguments. Hating excel/openoffice/spreadsheets in general is optional.

Just like every programmer, I am always trying to find new and interesting ways of automating myself out of a job. To that end, I wrote a pretty cool program last night to help automate my first algorithms lab.

Consistent with the recent trend of mine, it is in python and makes use of the [subprocess](http://docs.python.org/library/subprocess.html) module to spawn and time instances of my C++ program and [pylab](http://matplotlib.sourceforge.net/) to make plotting the times super easy. The comments in my code explain things in more detail, but here is the one sentence summary: Python is being used to execute two programs written in C++ with the same set of arguments and spits out a plot of their times. In this case the two C++ programs are recursive (rfib) and iterative (ifib) implementations of the Fibonacci algorithm. The fun stuff is in the python:

<pre>
#!/usr/bin/env python

# Lucas Doyle wrote this

import subprocess
import string
import sys
import pylab  # matplotlib

def timerun(program, args) :
    print 'Starting timed execution of ' + program + ' with ' + str(len(args)) + ' arguments.'
    i = 1
    
    # Execute program, once for each n argument
    for n in args :
        
        # This was really annoying. Build the arguments to the time system call to the time command.
        # First of all, for whatever reason 'time' didn't work correctly with any arguments other than -p, 
        # so I used /usr/bin/time instead. Since I could not figure out why the output of 'time' was not
        # coming back to stdin, I use the -o (output file) and -a (append) option to just output the real
        # execution time ( thats where '-f' and '%e' comes from ) to the file.
        p = subprocess.Popen(['/usr/bin/time', '-o', 'runtimes.txt', '-a', '-f', '%e', './' + program, str(n)], stdout=subprocess.PIPE)
        
        # Read back from stdin, print where we are (not required, but its nice)
        output = p.communicate()[0]
        sys.stdout.write( str(i) + ':\tfib('+ str(n) + ') = ' + output)
        i += 1
    print 'done'
    
    # Open up, read and return the times in the output file
    f = open('runtimes.txt', 'r')
    times = f.read().splitlines()

    # Clean up old runtimes
    subprocess.Popen(['rm', 'runtimes.txt'],stdout=subprocess.PIPE)
    
    return times

def main():
    
    # Arguments we are interested in testing runtimes for
    # args = 1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43, 44, 45, 46, 47, 48
    args = range(1, 56)
    
    
    
    # Compute the runtimes of the recursive algorithm, then the iterative one
    rtimes = timerun('rfib', args)
    itimes = timerun('ifib', args)

    # Plot it with pylab
    pylab.xlabel('N')
    pylab.ylabel('Time to compute fib(N) (seconds)')
    pylab.title('Recursive vs. Iterative Execution Time for Fibionacci Sequence')
    pylab.plot(args, rtimes, 'ro-', label='Recursive')
    pylab.plot(args, itimes, 'bo-', label='Iterative')
    pylab.legend()

    # other drawing styles for plots in pylab:
    # 'r' red line, 'g' green line, 'y' yellow line 
    # 'ro' red dots as markers, 'r.' smaller red dots, 'r+' red pluses
    # 'r--' red dashed line, 'g^' green triangles, 'bs' blue squares
    # 'rp' red pentagons, 'r1', 'r2', 'r3', 'r4' well, check out the markers

    # save the plot as a PNG image
    pylab.savefig('Fig.png')

    # show the pylab plot window
    pylab.show()

if __name__ == "__main__":
    main()

</pre>

I've also attached the whole lab [here]({{wr}}static/misc/lab1.zip) in case the python does not make sense by itself. Hope someone finds this useful!

