#Explode (C)

<hr>

<b>Guest at 2010-03-22 04:53:36:</b><br /><br />

Computer Program
Language: C

Prelim:

usage: explode [program].c

output: [program]_main.c [prog]_[func1].c [prog]_[func2.c] ... Makefile

function: explode a C progam file into separate function files

how it works:

- keep track of scope
    - { = scope++
    - } = scope--
    - if scope == 0 && encounters a function header
        - open new file and copy function
    - \#include extern files in [prog]_main.c
    - write makefile
