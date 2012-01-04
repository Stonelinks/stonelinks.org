import contrib.markdown as markdown

def md(string):
    md = markdown.Markdown()
    return md.convert(str(string))

def md2file(path, filename, filecontents):
    f = open(path + filename, 'w')
    f.write(md(filecontents))
    f.close()

def filewrite(file, contents):
    f = open(file, 'w')
    f.write(contents)
    f.close()

def mdfile2html(mdfile):
    f = open(mdfile, 'r')
    html = md(f.read())
    f.close()
    return html

