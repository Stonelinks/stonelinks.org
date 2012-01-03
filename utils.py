import contrib.markdown as markdown

def md(string):
    md = markdown.Markdown()
    return md.convert(str(string))

def md2file(path, filename, filecontents):
    f = open(path + filename, 'w')
    f.write(md(filecontents))
    f.close()

def md2html(mdfile, destination):
    f = open(mdfile, 'r')
    html = md(f.read())
    f.close()
    filename = mdfile.split('/')[-1]
    filename = filename.split('.')[-2]
    filename = filename + '.html'
    f = open(destination + '/' + filename, 'w')
    f.write(html)
    f.close()
