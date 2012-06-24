#Stonelinks web framework

<center>

<br>

<img class="thumbnail" src="{{wr}}static/img/logo-big.png" width="60%">

</center>

This project is my take on how writing a mostly static website with a lot of content should work. It is what runs this very website. It requires no server side scripting or database of any kind. In fact it is all static files that are compiled from simple markdown files. It is a not well suited for web apps with an API and lots of dynamic content.

<br>

##History

"Stonelinks" is a moniker I use for myself all over the internet and of course the name of this website. In one form or another, Stonelinks has been online since late 2008 when I decided to figure out how the internet works (a task which is still ongoing).

Since 2008, Stonelinks has gone through many incarnations. For a long time it ran on wordpress (before I knew how to program mind you!). As is the way with many wordpress sites I've been involved in, the whole thing was a bit overgrown, cluttered and hard to control. Since Stonelinks is fundamentally static content (mostly), I thought that there had to be a better way.

Fast forward to winter break 2012. I happened to have a bunch of spare time on a cruise with no internet access. Like any sensible programming addict, I really wanted a new project to occupy myself with while I sat around watching people gorge themselves on the lido deck. Hence this incarnation of Stonelinks was born!

<br>

##Design

My design goals for this was to have something that, from an authors perspective, was dead simple to use. Basically all I wanted authors to do is create a single [markdown](http://daringfireball.net/projects/markdown/) file with just the body of a page and have it automatically add the rest of the website around it. This means things like contextual sidebars, navigation, comments, links, etc.

In keeping with the goal of trying to keep this as simple as possible, this meant no server side scripting lanugages or databases. I tried to only add complexity as I need it. Therefore, all the content of this website is static HTML that was automatically generated.

In hindsight, static HTML generators like this have been done a zillion times before. Hyde and Firmant come to mind. But as with a lot of things, its feels nice to make a tool yourself and use it for yourself. Things like this also help you appreciate the work and expertise that others have done. Too many times I have heard programmers say things like "django sucks!". If django sucks so much, try to write something that does what django does (or better yet, submit a patch or something), then we'll talk! **tl;dr**: [eat your own dog food](http://en.wikipedia.org/wiki/Eating_your_own_dog_food).

<br>

##Features

- Page hierarchy
    - Store all content as markdown files structured into directories to form a hierarchy
    - Automatic generation of a site map based on hierarchy
    - Automatic generation of navigation sidebar for all pages on the same level in hierarchy
    - Automatic generation of index pages in a directory if an `index.md` file doesn't exist (sorta how a web server does)
    - Breadcrumb navigation for each page from root of tree to current page
- URL control
    - Should be able to control everything about a URL from:
        - Name of markdown file
        - Location in a directory
- Portability
    - Should be able to build locally and deploy the website anywhere
    - Preview changes to website locally without connection to internet
    - Easy and fast to deploy (deploy scripts that use rsync)
- Shortcodes:
    - Easy creation of relative links to preserve portability.
    - Enabling and disable comments
    - Easy inclusion of galleries
    - Time / date / other convenience functions
- Misc features
    - Support for a blog:
        - Sort entries based on date
        - Indexes are paginated listings of posts (like you would expect on a blog)
        - Automatic full archives
    - Write all content in markdown
    - Comments via disqus
    - Page minification

<br>

##Code

The code that runs Stonelinks is open source! See the code on github!
####[https://github.com/Stonelinks/stonelinks.org](https://github.com/Stonelinks/stonelinks.org)

<br>

##How to use
The general process of how to use the Stonelinks web framework is pretty simple:

- Pull down the git repository
- Write the content of your web pages in markdown files
- Put them in the `content` directory either alone or put related files a directory
- Change some simple settings in config.py
- Modify the makefile to deploy to your web server of choice
- Run `make site`

<br>

##How it works

First, a website object from `objects.py` is created. It crawls the source directory (in this case it is `content`) and constructs a tree out of the filenames and directory names contained inside. In the tree, each node is actually a page object. At first glance, this makes no sense because it means directories are actually being picked up as files representing web pages. However, as we will soon see, if an `index.md` file is not present under a directory, the parent directory page object will yeild an automatically generated index similar to what apache and other webservers do.

<br>

###Traversal

Once a tree has been made, whenever an operation needs to be conducted on a page by page basis (like say, generating the html for sidebar navigation on each page), there exists a utility function inside the website object called `traverse` that will visit every page in the tree breadth-first style. `traverse` accepts a functional argument that it will in turn call on every page it visits as it traverses through the tree.

In addition to automatically generating sidebars on each page, a few other things are done using this `traverse` technique:

- Site map
- Automatic indexes
- Site compilation

<br>

###Page and site compilation

To compile a single page, take a look at `pages.py`. To see how the whole site is compiled, take a look at `gen_pages` in `objects.py`.

<br>

###Automatic indexes

Lets consider a website with the following structure:

- `root` (folder)
    - `index.md`
    - `contact.md`
    - `about.md`
    - `projects` (folder)
        - `project1.md`
        - `project2.md`
        - `project3.md`

As you can see, the files `index.md`, `content.md`, `about.md`, and `projects[1-3].md` are compiled in a straightforward manner, and their html files are placed in the cooresponding location in the build directory. However, one will notice that if you were to visit `www.domain.com/projects`, no index would be presented. Therefore, when this occurs, the parent page object (created from the `projects` directory) generates a dummy index.

{{disable comments}}
