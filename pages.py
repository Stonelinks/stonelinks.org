import parts
import config
import utils
import os

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
  if '{{disable comments}}' in p.content:
    p.enable_comments = False
  
  if p.is_auto_index or p.is_dir:
    p.enable_comments = False
  
  if p.enable_comments:
    comment_html = '<br>'
    comment_html += parts.load('comments')
    
    # id based on address
    comment_html = comment_html.replace('{{disqus_identifier}}', p.address())
    return comment_html
  else:
    print "page", p.human_name, "has comments disabled"
  return ''

def page(p):
  print "building page", p.human_name
  
  
  # beginning of head
  s = '<!DOCTYPE html><html>'
  s += '<head>'
  
  s += '<title>{{sn}} | ' + p.human_name + '</title>'
  
  s += utils.minify(parts.load('favicon'))

  # style
  if config.use_less:
    s += utils.minify(parts.load('bootstrap_less'))
  else:
    s += utils.minify(parts.load('bootstrap_css'))

  s += utils.minify(parts.load('js_libs'))
  s += utils.minify(parts.load('google_analytics'))
  
  # end head, start page
  s += '</head><body>'
  
  # main wrapper
  s += '<div id="wrapper">'

  # top bar and navigation
  navlist = []
  navlist.append(('Luke', '{{wr}}luke'))
  navlist.append(('Projects', '{{wr}}projects'))
  navlist.append(('Blog', '{{wr}}blog'))
  navlist.append(('Site Map', '{{wr}}map'))
  s += utils.minify(nav(navlist))
  
  # start bg wrapper
  s += '<div id="bg-wrapper">'

  if not p.omit_sidebar:
    s += '<div class="span3" id="sidebar">'
    s += '<div class="well sidebar-nav">'
    s += p.sidebar
    s += '</div>'
    s += '</div>'
  
  # start container
  s += '<div class="container" style="width: 800px;">'

  # start content
  s += '<div id="page-body">'
  s += p.breadcrumb()
  s += utils.md(p.content)
  s += '<hr>'
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
