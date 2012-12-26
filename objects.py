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
    
    self.hidden = False
    
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
      s = s.replace(' &rarr; <a href="{{wr}}index.html"></a>', '')
      return s

  def address(self):
    if self.is_dir:
      return '{{wr}}' + os.path.join(self.path, self.name, 'index.html')
    else:
      return '{{wr}}' + os.path.join(self.path, self.name + '.html')
  
  def make_page(self):
    self.page_html = pages.page(self)
    self.short_tags()
    return self.page_html

  def compute_short_tags(self):
    if self.content is None:
      return
    else:
      if '{{disable sidebar}}' in self.content:
        self.omit_sidebar = True
      if '{{disable comments}}' in self.content:
        self.enable_comments = False
      if '{{hidden}}' in self.content:
        self.hidden = True

  def short_tags(self):
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
    
    s = s.replace('{{hidden}}', '')
    
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
    self.destination = 'build'

    self.root = None
    
    self.build_tree(None, self.source)
    
    # fix root node
    self.root.human_name = 'Home'
    self.root.name = ''
    
  def traverse(self, t_func):
    def _traverse(p, t_func):
      s = ''
      if not p.is_dir:
        return t_func(p)
      else:
        r = t_func(p)
        if r is not None:
          s += r
        for c in p.children:
          r = _traverse(c, t_func)
          if r is not None:
            s += r
        return s
    return _traverse(self.root, t_func)
    
  def page_obj(self, d, level, is_dir=False):
    
    path = '/'.join(d.split('/')[1:-1])
    filename = d.split('/')[-1].split('.')[0]
    
    oldpath = os.path.join(self.source, path)
    newpath = os.path.join(self.destination, path)
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
    p.compute_short_tags()
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
    p.destination = self.destination
    p.omit_sidebar = True
    p.enable_comments = False
    
    s = '#Site Map\n\n'
    
    def _gen_map(p):
      if not p.hidden:
        t = '    '*p.level
        t += '- [' + p.human_name + '](' + p.address() +')\n'
      else:
        t = ''
      return t
    
    s += self.traverse(_gen_map)

    p.content = s
    self.root.children.append(p)

  def gen_sidebars(self):
    def _gen_sidebar(p):
      if p.name == 'blog' or p.hidden:
        return
      else:
        s = '<h3><a href="%s">%s</a></h3>' % (p.address(), p.human_name)
        s += '<ul class="nav nav-list">'
        for c in p.children:
          if c.hidden:
            pass
          else:
            s += '<li><a href="%s">%s</a></li>' % (c.address(), c.human_name)
        
        for c in p.children:
          c.sidebar = s.replace('<li><a href="%s">%s</a></li>' % (c.address(), c.human_name), \
                      '<li class="active"><a href="%s">%s</a></li>' % (c.address(), c.human_name))
          if c.level > 1:
            c.sidebar += '<li class="divider"></li>'
            c.sidebar += '<li><a onclick="goBack()"><b>&larr; Go Back</b></a></li>'
          c.sidebar += '</ul>'
    self.traverse(_gen_sidebar)

  def gen_indexes(self):
    def _gen_index(p):
      if p.name in ['index', 'blog'] or not p.is_dir or p.hidden:
        return
      else:
        for c in p.children:
          if c.name == 'index' or c.hidden:
            return
        print "generating index for ", p.human_name
        p.omit_sidebar = True
        s = '#' + p.human_name + '\n\n'
        for c in p.children:
          s += '- ##[%s](%s)\n' % (c.human_name, c.address())
        s += '\n\n<hr><a href="../"><h2>&larr; Back up</h2></a>'
        p.content = s
        p.is_auto_index = True
        p.destination = os.path.join(p.destination, p.name)
    self.traverse(_gen_index)

  def gen_blog(self):
    def _blog(p):
      if p.name == 'blog':
        blog.make_blog(p)
    self.traverse(_blog)

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
        basepath = os.path.join(self.destination, p.path)
        if not os.path.isdir(basepath):
          os.makedirs(basepath)
        if p.is_auto_index:
          p.level += 1
          dst = os.path.join(p.destination, 'index.html')
        else:
          dst = os.path.join(p.destination, p.name + '.html')
        utils.filewrite(dst, p.make_page())
    self.traverse(_gen_page)
