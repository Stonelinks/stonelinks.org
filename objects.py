import os
import sys
import pages
import utils
import config
import time

class page(object):
  def __init__(self):
    self.human_name = ''
    self.name = ''
    self.path = ''
    self.addr = ''
    self.date = ''
    self.level = ''
    self.content = ''
    self.sidebar = ''
    self.omit_sidebar = False
    
    self.destination = ''
    self.is_dir = False
    self.is_auto_index = False
    self.children = []
    
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
        i+=1
      s.append(self.human_name)
      s.insert(0, '<a href="{{wr}}">Home</a>')
      
      # TODO: make this less ugly 
      s = '<small>' + ' &gt; '.join(s) + '</small><hr>'
      s = s.replace(' &gt; <a href="{{wr}}/index.html"></a>', '')
      return s

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
    s = s.replace('{{social_small}}', pages.social_small())
    s = s.replace('{{social_large}}', pages.social_large())
    
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
    
    self.build_tree(None, self.source)
    #self.print_tree()
    
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
    p.omit_sidebar = True
    
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
      s = '**[' + p.human_name + '](' + p.address() + ')**\n\n'
      for c in p.children:
        s += '- [%s](%s)\n' % (c.human_name, c.address())
      for c in p.children:
        bar = s.replace('- [%s](%s)' % (c.human_name, c.address()), '- %s' % c.human_name)
        c.sidebar = bar
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
      p.content = s
      p.is_auto_index = True
      p.destination = os.path.join(p.destination, p.name)
      return ''
    self.traverse(_gen_index)

  def gen_blog(self):
    def blog_index(p):
      if p.name == 'blog':
        n = page()
        n.human_name = 'Blog'
        n.name = 'index'
        n.level = p.level + 1
        n.path = os.path.join(p.path, 'blog')
        n.destination = os.path.join(p.destination, 'blog')
        n.omit_sidebar = False
        s = ''
        #s = '#' + n.human_name + '\n\n'
        #s += '<br>'*4 + '\n'
        sidebar = '##Archives:\n\n'
        blog = {}
        for c in p.children:
          date = c.content[c.content.find('\n') + 1:]
          date = date[:date.find('\n')]
          c.date = date
          key = time.mktime(time.strptime(date, '%m/%d/%Y'))
          blog[key] = c
        
        for k in reversed(sorted(blog.iterkeys())):
          c = blog[k]
          blog_summary = '##[' + c.human_name + '](' + c.address() +')\n'
          blog_summary += '<br>\n'
          wordlist = c.content[c.content.find('\n') + 1:]
          wordlist = wordlist[wordlist.find('\n'):]
          wordlist = wordlist.replace('#','##').split(' ')
          blog_summary += 'Date: ' + c.date + '\n\n'
          blog_summary += ' '.join(wordlist[:90])
          blog_summary += '\n'*2
          blog_summary += '[Read more...](' + c.address() +')\n'
          blog_summary += '<br>'*3 + '<hr>\n'
          s += blog_summary
          sidebar += '- [%s](%s)\n' % (c.human_name, c.address())
        n.content = s
        n.sidebar = sidebar
        p.children.append(n)
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
