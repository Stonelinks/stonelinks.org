import parts
import config
import utils
import os

def tag(tag, content):
  return '<' + tag + '>' + content + '</' + tag + '>'

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
  s = '<!DOCTYPE html><html>'
  s += '<head>'
  
  s += tag('title', p.human_name)
  
  s += parts.load('js_libs')

  # style
  if config.use_less:
    s += parts.load('bootstrap_less')
  else:
    s += parts.load('bootstrap_css')
  
  # end head, start page
  s += '</head><body>'
  s += '<div class="container">'
  s += '<div class="content">'
  s += '<div class="wrapper">'
  
  # top bar and navigation
  navlist = []
  navlist.append(('Luke', '{{wr}}luke'))
  navlist.append(('Blog', '{{wr}}blog'))
  navlist.append(('Site Map', '{{wr}}map'))
  s += nav(navlist)
  
  # page content
  s += p.breadcrumb()

  if not p.omit_sidebar:
    s += '<div class="span4" style="float: right;">'
    #s += '<b>Navigation</b>'
    s += utils.md(p.sidebar)
    s += '</div>'
  
  s += utils.md(p.content)
  
  # end page
  s += '</div>'
  s += parts.load('footer')
  s += '</div>'
  s += '</div>'
  s += '</body>'
  s += '</html>'
  
  return s
