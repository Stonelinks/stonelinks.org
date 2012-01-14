import os
import sys
import pages
import utils

#dfs style traversal of
def traverse(d = '.', level = 0):
  basedir = d
  subdirlist = []

  path = '/'.join(d.split('/')[1:-1])
  filename = d.split('/')[-1]
  oldpath = os.path.join(source, path)
  newpath = os.path.join(to, path)

  if os.path.isfile(d):
    # create and / or map the file 
    if not os.path.isdir(newpath):
      os.makedirs(newpath)
    if state is not 'init':
      print level, ": creating", newpath
      pages.md2wp(os.path.join(oldpath, filename), newpath)
    else:
      print "mapping file", filename
      name = filename.split('.')[0]
      address = '{{wr}}/' + os.path.join(path, name) + '.html'
      map(name, address, level)
  else:
    if state is 'init':
      print "mapping dir", filename
      dirname = filename.split('.')[0]
      address = '{{wr}}/' + os.path.join(path, dirname + "/index.html")
      map(dirname, address, level)
    for item in sorted(os.listdir(d)):
      if not os.path.isfile(item):
        subdirlist.append(os.path.join(basedir, item))
    for subdir in sorted(subdirlist):
      traverse(subdir, level + 1)

def map(name, address, level):
  """if filename == 'index':
    filename = path.split('/')[-1]
    level -= 1
    if level == -1:
      level = 0
  if filename == '':
      filename = 'Home'
      address = 'index.html'
  """
  try:
      global structure
      structure += 4*level*' '
  except:
      globals()['structure'] = '#Site Map\n\n\n'
  structure += '- [' + name + '](' + address + ')\n'

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

  print '\n'*3, "phase 1...", '\n'*3
  gen_special_pages()
  print '\n'*3, "phase 2...", '\n'*3
  gen_pages()
