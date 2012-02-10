import os
import sys
import pages
import utils
import config
import tidy

class page(object):
  def __init__(self):
    self.human_name = ''
    self.name = ''
    self.path = ''
    self.addr = ''
    
    self.level = ''
    self.content = ''
    self.sidebar = ''
    
    self.destination = ''
    self.is_dir = False
    self.children = []

  def breadcrumb(self):
    if self.level == 1:
      return ''
    else:
      l = self.path.split('/')
      s = []
      i = 0
      for p in l:
        d = l[:i+1]
        d.append('index.html')
        s.append('<a href="{{wr}}' + '/'.join(d) + '">' + p.capitalize() + '</a>')
        i+=1
      s.append(self.human_name)
      return '<small>' + ' &gt; '.join(s) + '</small><hr>'

  def address(self):
    if self.is_dir:
      self.addr = '{{wr}}' + os.path.join(self.path, self.name, 'index.html')
    else:
      self.addr = '{{wr}}' + os.path.join(self.path, self.name + '.html')
    return self.addr
  
  def make_page(self):
    self.page_html = pages.page(self)
    self.pagefilter()
    return self.page_html
  
  def pagefilter(self):
    s = self.page_html

    s = s.replace('{{sn}}', config.site_name) # site name
    s = s.replace('{{st}}', config.site_tag) # site tag
    
    # social networks
    s = s.replace('{{social_small}}', config.social_small())
    
    # In order to make the website as portable as possible, 
    # all links generated are relative to the root
    # rli = relative link index
    rli = utils.clamp(0, self.level, self.level - 1)
    s = s.replace('{{wr}}', '../'*rli)
    self.page_html = s

  def __str__(self):
    def q(s):
      return ' '*3 + str(s) + '\n'
    s = q(self.human_name + ':')
    s += q(self.name)
    s += q(self.path)
    s += q(self.address())
    s += q(self.level)
    s += q(self.content)
    s += q(self.destination)
    s += '\n'*3
    return s
    
class site(object):
  def __init__(self):
    self.source = 'content'
    self.to = 'build'

    self.root = None
    self.state = None
    
    self.state = 'init'
    self.build_tree(None, self.source)
    self.print_tree()
    
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
    
  def print_tree(self):
    print_func = lambda p: '  '*p.level + '- ' + p.human_name + '\n'
    print self.traverse(print_func)
  
  def page_obj(self, d, level, is_dir=False):
    path = '/'.join(d.split('/')[1:-1])
    filename = d.split('/')[-1].split('.')[0]
    
    oldpath = os.path.join(self.source, path)
    newpath = os.path.join(self.to, path)
    p = page()
    p.level = level
    p.path = path
    #p.parent = '/'.join(d.split('/')[:-1]) + '/index.html'
    if is_dir:
      p.human_name = filename.capitalize()
      p.name = filename
      p.is_dir = True
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
      p.destination = newpath
    return p

  #dfs style traversal
  def build_tree(self, parent, d='.', level=0):
    basedir = d
    subdirlist = []
    
    is_dir=os.path.isdir(d)
    p = self.page_obj(d, level, is_dir=is_dir)
    p.children = []
    if self.root == None:
      self.root = p
    else:
      parent.children.append(p)
    
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
    
    s = '#Site Map\n\n'
    map_func = lambda p: '    '*p.level + \
               '- [' + p.human_name + '](' + p.address() +')\n'
    s += self.traverse(map_func)

    p.content = s
    self.root.children.append(p)

  def gen_sidebars(self):
    def _gen_sidebar(p):
      s = '\n'
      for c in p.children:
        s += '- [%s](%s)\n' % (c.human_name, c.address())
      for c in p.children:
        bar = s.replace('- [%s](%s)' % (c.human_name, c.address()), '- %s' % c.human_name)
        c.sidebar = bar
      return ''
    self.traverse(_gen_sidebar)

  def gen_special_pages(self):
    self.gen_map()
    self.gen_sidebars()

  def gen_pages(self):
    self.state = 'generate'
    def _gen_page(p):
      if p.is_dir:
        pass
      else:
        basepath = os.path.join(self.to, p.path)
        if not os.path.isdir(basepath):
          os.makedirs(basepath)
        dst = os.path.join(p.destination, p.name + '.html')
        utils.filewrite(dst, p.make_page())
      return ''
    self.traverse(_gen_page)
