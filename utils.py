import contrib.markdown as markdown
import re

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

def minify(t):
  comment_re0 = re.compile(' \/\/.*\\n')
  comment_re1 = re.compile('\\n\/\/.*\\n')
  comment_re2 = re.compile('[^:]\/\/.*\\n')
  comment_re3 = re.compile('\/\*.*\*\/')
  
  re_list = [comment_re0, comment_re1, comment_re2, comment_re3]
  for _re in re_list:
    for comment in _re.findall(t):
      t = t.replace(comment, '')

  t = t.replace('\n', ' ')
  while '  ' in t:
    t = t.replace('  ', ' ')
  t = t.replace('> <', '><')
  return t
