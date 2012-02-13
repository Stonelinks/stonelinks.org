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
  s += parts.load('search')
  s += parts.load('nav.end')
  return s


def social_small():
  s = ''
  for k, v in config.social_networks.iteritems():
    s += '<a href ="' + v + '" >'
    s += '<img style="position: relative; top: 4px;" src="{{wr}}static/img/icons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
  return s

def social_large():
  s = '<div class="span8" style="text-align: center;"><table>'
  for k, v in config.social_networks.iteritems():
    s += '<tr><td>'
    s += '<a href ="' + v + '" >'
    s += '<img src="{{wr}}static/img/lgicons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
    s += '</td><td>'
    s += '<a href ="' + v + '" ><h2>' + k.capitalize().replace('plus', ' +') + '</h2></a>'
    s += '</td></tr>'
  s += '</table></div>'
  return s

def page(p):
  # beginning of head
  s = '<!DOCTYPE html><html>'
  s += '<head>'
  
  s += tag('title', '{{sn}} | ' + p.human_name)
  
  s += parts.load('js_libs')
  s += parts.load('favicon')

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
  navlist.append(('Projects', '{{wr}}projects'))
  navlist.append(('Blog', '{{wr}}blog'))
  navlist.append(('Site Map', '{{wr}}map'))
  s += nav(navlist)
  
  # page content
  s += p.breadcrumb()

  if not p.omit_sidebar:
    s += '<div style="clear: both;"></div>'
    s += '<div class="span4" style="float: right;">'
    s += utils.md(p.sidebar)
    s += '</div>'
  
  s += utils.md(p.content)
  
  # end page
  s += '</div>'
  s += parts.load('footer')
  s += '</div>'
  s += '</div>'
  s += '<br>'*10
  s += '</body>'
  s += '</html>'
  
  return s
