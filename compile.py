import os
import sys
import pages
import utils

def filehandler(f, level):
  path = '/'.join(f.split('/')[1:-1])
  filename = f.split('/')[-1]
  oldpath = os.path.join(source, path)
  newpath = os.path.join(to, path)
  if not os.path.isdir(newpath):
    os.makedirs(newpath)
  if state is not 'init':
    pages.md2wp(os.path.join(oldpath, filename), newpath)
    print level, ": ", newpath
  else:
    map(filename, path, level)

def traverse(d = '.', level = 0):
  print d
  basedir = d
  subdirlist = []
  if os.path.isfile(d):
    filehandler(d, level)
  else:
    for item in os.listdir(d):
      if not os.path.isfile(item):
        subdirlist.append(os.path.join(basedir, item))
    for subdir in subdirlist:
      traverse(subdir, level + 1)

def map(filename, path, level):
  filename = filename.split('.')[0]
  address = os.path.join(path, filename) + '.html'
  if filename == 'index':
    filename = path.split('/')[-1]
    level -= 1
    if level == -1:
      level = 0
  if filename == '':
      filename = 'Home'
      address = 'index.html'
  try:
      global structure
      structure += 4*level*' '
  except:
      globals()['structure'] = '#Site Map\n'
  structure += '- [' + filename + ']({{wr}}/' + address + ')\n'

def printusage():
  print "usage: python compile.py <source dir> <build dir>"

def gen_special_pages():
    globals()['state'] = 'init'
    traverse(source)
    utils.filewrite(os.path.join(source, 'map.md'), structure)

    
def gen_pages():
  globals()['state'] = 'generate'
  traverse(source)
  
if __name__ == "__main__":
  globals()['source'] = 'content'
  globals()['to'] = 'build'
  
  gen_special_pages()
  gen_pages()
