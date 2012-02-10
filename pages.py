import parts
import config
import utils
import os

def title(title):
  return '<title>' + title + '</title>\n'

def md2wp(mdfile, htmldst):
  html = utils.mdfile2html(mdfile)
  html = page(html)
  filename = mdfile.split('/')[-1]
  filename = filename.split('.')[-2]
  filename = filename + '.html'
  f = open(os.path.join(htmldst, filename), 'w')
  f.write(html)
  f.close()

def nav(l):
  s = parts.load('nav.begin')
  for link, address in l:
    s += '<li><a href="' + address + '">' + link + '</a></li>\n'
  s += parts.load('nav.end')
  return s

def page(p):
  # beginning of head
  s = parts.load('doctype')
  s += '<head>'
  
  # libraries
  s += title(p.human_name)
  s += parts.load('bootstrap_less')
  
  # end head, start page
  s += '</head>'
  s += '<body>'
  s += parts.load('pagehead')
  
  # top bar and navigation
  navlist = []
  navlist.append(('herp', 'derp'))
  navlist.append(('home', 'alone'))
  navlist.append(('example', 'example2'))
  s += nav(navlist)
  
  # page content
  s += p.breadcrumb()

  if not p.name == 'map':
    s += '<div class="span4" style="float: right;">'
    s += '<b>Navigation</b>'
    s += utils.md(p.sidebar)
    s += '</div>'
  
  s += utils.md(p.content)

  # end page
  s += parts.load('footer')
  s += '</body>'
  s += '</html>'
  
  return s
