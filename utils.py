import contrib.markdown as markdown

def md(string):
  md = markdown.Markdown()
  return md.convert(unicode(string))

def filewrite(file, contents):
  f = open(file, 'w')
  f.write(contents)
  f.close()

def fileread(file):
  f = open(file, 'r')
  s = f.read()
  f.close()
  return s

def mdfile2html(mdfile):
  f = open(mdfile, 'r')
  html = md(f.read())
  f.close()
  return html

def page_link(p):
  return '<a href="%s">%s</a>' % (p.address(), p.human_name)

def clamp(a, b, c):
  if c <= a:
    return a
  elif c > b:
    return b
  else:
    return c

