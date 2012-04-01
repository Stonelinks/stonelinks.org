import parts
import config
import utils
import os

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
  s = '<div class="span4" style="text-align: center;"><table>'
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

def comments(p):
  if '{{disable comments}}' in p.content:
    print "disabling comments for ", p.human_name
    p.enable_comments = False
  
  if p.is_auto_index or p.is_dir:
    p.enable_comments = False
  
  if p.enable_comments:
    comment_html = '<br><hr>'
    comment_html += parts.load('comments')
    
    # id based on address
    comment_html = comment_html.replace('{{disqus_identifier}}', p.address())
    return comment_html
  else:
    print "page", p.human_name, "has comments disabled"
  return ''


def page(p):
  # beginning of head
  s = '<!DOCTYPE html><html>'
  s += '<head>'
  
  s += '<title>{{sn}} | ' + p.human_name + '</title>'
  
  s += parts.load('favicon')

  # style
  if config.use_less:
    s += parts.load('bootstrap_less')
  else:
    s += parts.load('bootstrap_css')

  s += parts.load('js_libs')
  s += parts.load('google_analytics')

  # end head, start page
  s += '</head><body>'

  # top bar and navigation
  navlist = []
  navlist.append(('Luke', '{{wr}}luke'))
  navlist.append(('Projects', '{{wr}}projects'))
  navlist.append(('Blog', '{{wr}}blog'))
  navlist.append(('Site Map', '{{wr}}map'))
  s += nav(navlist)

  s += '<div id="bg-wrapper">'

  if not p.omit_sidebar:
    s += '<div class="span3" id="sidebar">'
    s += '<div class="well sidebar-nav">'
    s += p.sidebar
    s += '</div>'
    s += '</div>'

  s += '<div class="container" style="width: 800px;">'

  # page content
  s += '<div id="page-body">'
  s += p.breadcrumb()
  s += utils.md(p.content)
  s += '<hr>'
  s += comments(p)
  s += '</div>'

  # end page
  s += '</div>'
  s += '</div>'
  s += parts.load('footer')
  s += '</body>'
  s += '</html>'
  
  return s
