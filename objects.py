import os
import sys
import pages
import utils
import config

class page(object):
  def __init__(self):
    self.human_name = ''
    self.name = ''
    self.path = ''
    self.addr = ''
    
    self.level = ''
    self.content = ''

    self.destination = ''
    self.parent = ''
    self.is_dir = False

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
    rli = utils.clamp(0, self.level, self.level - 1)
    s = s.replace('{{wr}}', '../'*rli)
    s = s.replace('{{sn}}', config.site_name)
    s = s.replace('{{st}}', config.site_tag)
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
    self.source = ''
    self.to = ''

    self.pages = []
    self.state = None
    
  def init(self):
    self.state = 'init'
    self.traverse(self.source)
    
  #dfs style traversal
  def traverse(self, d = '.', level = 0):
    basedir = d
    subdirlist = []

    path = '/'.join(d.split('/')[1:-1])
    filename = d.split('/')[-1].split('.')[0]
    
    oldpath = os.path.join(self.source, path)
    newpath = os.path.join(self.to, path)
    
    if os.path.isfile(d):
      f = open(d, 'r')
      firstline = f.readline()
      f.close()
      if firstline[0] == '#':
        title = firstline[1:-1]
      else:
        title = filename.capitalize()
      
      #print level, ": creating", newpath

      content = utils.fileread(d)

      p = page()
      p.human_name = title
      p.name = filename
      p.level = level
      p.path = path
      p.content = content
      p.destination = newpath
      p.parent = self.find_parent()
      self.pages.append(p)
    else:
      # create dummy page for the dir
      dir = page()
      dir.human_name = filename.capitalize()
      dir.name = filename
      dir.level = level
      dir.path = path
      dir.is_dir = True
      dir.parent = self.find_parent()
      self.pages.append(dir)
      for item in sorted(os.listdir(d)):
        if not os.path.isfile(item):
          subdirlist.append(os.path.join(basedir, item))
      for subdir in sorted(subdirlist):
        self.traverse(subdir, level + 1)
  
  # finds the parent of the newest page
  def find_parent(self):
    i = len(self.pages) - 1
    while i >= 0:
      if self.pages[i].is_dir:
        return self.pages[i].address()
      i-=1
    return ''

  def page_find(self, address):
    for p in self.pages:
      if address is p.address():
        print "found", p.address()
        return p
    return None
      
  def print_pages(self):
    for page in self.pages:
      print page
  
  def gen_map(self):
    p = page()
    p.human_name = 'Site Map'
    p.name = 'map'
    p.level = 1
    p.path = ''
    p.destination = self.to

    s = '#Site Map\n\n\n'
    for d in self.pages:
      s += 4*d.level*' '
      s += '- [' + d.human_name + '](' + d.address() + ')\n'

    p.content = s
    self.pages.append(p)

  def gen_special_pages(self):
    self.gen_map()

  def gen_pages(self):
    self.state = 'generate'
    for p in self.pages:
      if p.is_dir:
        continue
      else:
        basepath = os.path.join(self.to, p.path)
        if not os.path.isdir(basepath):
          os.makedirs(basepath)
        dst = os.path.join(p.destination, p.name + '.html')
        html = p.make_page()
        utils.filewrite(dst, html)
