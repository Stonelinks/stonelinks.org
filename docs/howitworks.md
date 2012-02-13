#How it works

First, a website object from `objects.py` is created. When it is created, it crawls the source directory and constructs a tree out of the filenames and directory names contained inside. In the tree, each node is actually a page object. At first glance, this makes no sense because it means directories are actually being picked up as files representing webpages. However, as we will soon see, if an `index.md` file is not present under a directory, the parent directory page object will yeild an automatically generated index similar to what apache and other webservers do.

##Traversal

Once a tree has been made, whenever an operation needs to be conducted on a page by page basis (like say, generating the html for sidebar navigation on each page), there exists a utility function inside the website object called `traverse` that will visit every page in the tree breadth-first style. `traverse` accepts a functional argument that it will in turn call on every page as it traverses through the tree.

In addition to automatically generating sidebars on each page, a few other are generated using this `traverse` technique:

- Site map
- Automatic indexes
- Site compilation

##Page and site compilation

To compile a single page, take a look at `pages.py`. To see how the whole site is compiled, take a look at `gen_pages` in `objects.py`.

##Automatic indexes

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
