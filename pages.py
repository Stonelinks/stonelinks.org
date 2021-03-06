import parts
import config
import utils
import os

def nav_html():
  navlist = []
  navlist.append(('About Me', '{{wr}}luke/index.html'))
  navlist.append(('Projects', '{{wr}}projects/index.html'))
  navlist.append(('Blog', '{{wr}}blog/index.html'))
  navlist.append(('Site Map', '{{wr}}map.html'))
  
  s = parts.load('nav.begin')
  for link, address in navlist:
    s += '<li><a href="' + address + '">' + link + '</a></li>\n'
  s += parts.load('search')
  s += parts.load('nav.end')
  return s

def social_small():
  s = ''
  for k, v in config.social_networks.iteritems():
    s += '<a href ="' + v + '" >'
    s += '<img style="position: relative;" src="{{wr}}static/img/icons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
  return s

def social_large():
  s = '<div class="row-fluid"><div class="span4" style="text-align: center;"><table>'
  for k, v in config.social_networks.iteritems():
    s += '<tr><td>'
    s += '<a href ="' + v + '" >'
    s += '<img src="{{wr}}static/img/lgicons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
    s += '</td><td>'
    s += '<a href ="' + v + '" ><h2>' + k.capitalize().replace('plus', ' +') + '</h2></a>'
    s += '</td></tr>'
  s += '</table></div></div>'
  return s

def comments(p):
  if p.is_auto_index or p.is_dir:
      p.enable_comments = False

  if p.enable_comments:
    comment_html = '<br>'
    comment_html += parts.load('comments')
    
    # id based on address
    comment_html = comment_html.replace('{{disqus_identifier}}', p.address())
    return comment_html
  else:
    return ''

def sidebar(p):
  s = ''
  if not p.omit_sidebar:
    s += '<div class="span3" id="sidebar">'
    s += '<div class="well sidebar-nav">'
    s += p.sidebar
    s += '</div>'
    s += '</div>'
  return s

def page(p):
  print "building page", p.human_name
  
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
  
  # minify everything we have so far
  s = utils.minify(s)
  
  # main wrapper
  s += '<div id="wrapper">'

  # top bar and navigation
  s += utils.minify(nav_html())
  
  # start bg wrapper
  s += '<div id="bg-wrapper">'

  # sidebar
  s += sidebar(p)
  
  # start container
  s += '<div class="container" style="width: 800px;">'

  # start content
  s += '<div id="page-body">'
  s += p.breadcrumb()
  s += utils.md(p.content)
  
  s += utils.minify(comments(p))
  
  # end content
  s += '</div>'

  # end container
  s += '</div>'
  
  # end bg wrapper
  s += '</div>'
  s += '<div class="push"></div>'
  
  # end main wrapper
  s += '</div>'
  s += utils.minify(parts.load('footer'))
  s += '</body>'
  s += '</html>'
  
  return s
