import os
import sys
import pages
import utils
import config
import time
import gallery
import re
import blog

class page(object):
  def __init__(self):
    self.human_name = ''
    self.name = ''
    self.path = ''
    self.date = ''
    self.level = ''
    self.content = ''
    self.sidebar = ''
    self.omit_sidebar = False
    
    self.destination = ''
    self.is_dir = False
    self.is_auto_index = False
    self.children = []
    
    self.enable_comments = True
    
  def breadcrumb(self):
    if self.level == 1:
      return ''
    else:
      l = self.path.split('/')
      s = []
      i = 0
      for p in l:
        d = l[:i + 1]
        d.append('index.html')
        s.append('<a href="{{wr}}' + '/'.join(d) + '">' + p.capitalize() + '</a>')
        i += 1
      s.append(self.human_name)
      s.insert(0, '<a href="{{wr}}">Home</a>')
      
      s = '<small>' + ' &rarr; '.join(s) + '</small><hr>'
      s = s.replace(' &rarr; <a href="{{wr}}/index.html"></a>', '')
      return s

  def address(self):
    if self.is_dir:
      return '{{wr}}' + os.path.join(self.path, self.name, 'index.html')
    else:
      return '{{wr}}' + os.path.join(self.path, self.name + '.html')
  
  def make_page(self):
    self.page_html = pages.page(self)
    self.page_filter()
    return self.page_html

  def page_filter(self):
    s = self.page_html

    s = s.replace('{{sn}}', config.site_name) # site name
    s = s.replace('{{st}}', config.site_tag) # site tag
    
    # galleries
    gallery_re = re.compile('\{\{gallery=".*"\}\}')
    for gal in gallery_re.findall(s):
      gallery_address = gal.split('"')[1]
      s = s.replace(gal, gallery.make_gallery(gallery_address))

    # social networks
    s = s.replace('{{social_small}}', pages.social_small())
    s = s.replace('{{social_large}}', pages.social_large())
    
    s = s.replace('{{disable comments}}', '')
    s = s.replace('{{disable sidebar}}', '')
    
    s = s.replace('{{ctime}}', time.ctime(time.time()))
    
    
    # In order to make the website as portable as possible, 
    # all links generated are relative to the root
    # rli = relative link index
    rli = utils.clamp(0, self.level, self.level - 1)
    s = s.replace('{{wr}}', '../'*rli)
    self.page_html = s

class site(object):
  def __init__(self):
    self.source = 'content'
    self.to = 'build'

    self.root = None
    
    self.build_tree(None, self.source)
    
    # fix root node
    self.root.human_name = 'Home'
    self.root.name = ''
    
  def traverse(self, t_func):
    def _traverse(p, lvl, t_func):
      s = ''
      if not p.is_dir:
        return t_func(p)
      else:
        s += t_func(p)
        for c in p.children:
          s += _traverse(c, lvl + 1, t_func)
        return s
    return _traverse(self.root, 0, t_func)
    
  def page_obj(self, d, level, is_dir=False):
    
    # oh god...
    path = '/'.join(d.split('/')[1:-1])
    filename = d.split('/')[-1].split('.')[0]
    
    oldpath = os.path.join(self.source, path)
    newpath = os.path.join(self.to, path)
    p = page()
    p.level = level
    p.path = path
    p.destination = newpath
    if is_dir:
      p.human_name = filename.capitalize()
      p.name = filename
      p.is_dir = True
      p.content = None
    else:
      f = open(d, 'r')
      firstline = f.readline()
      f.close()
      if firstline[0] == '#':
        title = firstline[1:-1]
      else:
        title = filename.capitalize()
      p.human_name = title
      p.name = filename
      p.content = utils.fileread(d)
    return p

  def build_tree(self, parent, d='.', level=0):
    basedir = d
    subdirlist = []
    
    is_dir = os.path.isdir(d)
    p = self.page_obj(d, level, is_dir=is_dir)
    p.children = []
    if self.root == None:
      self.root = p
    else:
      if is_dir:
        parent.children.append(p)
      else:
        extension = d.split('/')[-1].split('.')[-1]
        if extension == 'md':
          parent.children.append(p)
        else:
          print d, "is not a markdown file!"
    
    if is_dir:
      for item in sorted(os.listdir(d)):
        if not os.path.isfile(item):
          subdirlist.append(os.path.join(basedir, item))
      
    for subdir in sorted(subdirlist):
      self.build_tree(p, subdir, level + 1)
  
  def gen_map(self):
    p = page()
    p.human_name = 'Site Map'
    p.name = 'map'
    p.level = 1
    p.path = ''
    p.destination = self.to
    p.omit_sidebar = True
    p.enable_comments = False
    
    s = '#Site Map\n\n'
    map_func = lambda p: '    '*p.level + \
               '- [' + p.human_name + '](' + p.address() +')\n'
    s += self.traverse(map_func)

    p.content = s
    self.root.children.append(p)

  def gen_sidebars(self):
    def _gen_sidebar(p):
      if p.name == 'blog':
        return ''
      else:
        s = '<h3><a href="%s">%s</a></h3>' % (p.address(), p.human_name)
        s += '<ul class="nav nav-list">'
        for c in p.children:
          s += '<li><a href="%s">%s</a></li>' % (c.address(), c.human_name)
        
        for c in p.children:
          c.sidebar = s.replace('<li><a href="%s">%s</a></li>' % (c.address(), c.human_name), \
                      '<li class="active"><a href="%s">%s</a></li>' % (c.address(), c.human_name))
          if c.level > 1:
            c.sidebar += '<li class="divider"></li>'
            c.sidebar += '<li><a onclick="goBack()"><b>&larr; Go Back</b></a></li>'
          c.sidebar += '</ul>'
        return ''
    self.traverse(_gen_sidebar)

  def gen_indexes(self):
    def _gen_index(p):
      if p.name in ['index', 'blog'] or not p.is_dir:
        return ''
      for c in p.children:
        if c.name == 'index':
          return ''
      print "generating index for ", p.human_name
      p.omit_sidebar = True
      s = '#' + p.human_name + '\n\n'
      for c in p.children:
        s += '- ##[%s](%s)\n' % (c.human_name, c.address())
      s += '\n\n<hr><a href="../"><h2>&larr; Back up</h2></a>'
      p.content = s
      p.is_auto_index = True
      p.destination = os.path.join(p.destination, p.name)
      return ''
    self.traverse(_gen_index)

  def gen_blog(self):
    def blog_index(p):
      if p.name == 'blog':
        blog.make_blog(p)
      return ''
    self.traverse(blog_index)

  def gen_special_pages(self):
    self.gen_indexes()
    self.gen_blog()
    self.gen_map()
    self.gen_sidebars()

  def gen_pages(self):
    def _gen_page(p):
      if p.content is None:
        pass
      else:
        basepath = os.path.join(self.to, p.path)
        if not os.path.isdir(basepath):
          os.makedirs(basepath)
        if p.is_auto_index:
          p.level += 1
          dst = os.path.join(p.destination, 'index.html')
        else:
          dst = os.path.join(p.destination, p.name + '.html')
        utils.filewrite(dst, p.make_page())
      return ''
    self.traverse(_gen_page)
