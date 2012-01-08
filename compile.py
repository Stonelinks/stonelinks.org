import os
import sys
import pages

def filehandler(f):
  path = '/'.join(f.split('/')[1:-1])
  filename = f.split('/')[-1]
  oldpath = os.path.join(source, path)
  newpath = os.path.join(to, path)
  if not os.path.isdir(newpath):
      os.makedirs(newpath)
  pages.md2wp(os.path.join(oldpath, filename), newpath)
  print newpath

def traverse(d = '.'):
  basedir = d
  subdirlist = []
  if os.path.isfile(d):
    filehandler(d)
  else:
    for item in os.listdir(d):
      if not os.path.isfile(item):
        subdirlist.append(os.path.join(basedir, item))
    for subdir in subdirlist:
      traverse(subdir)

def printusage():
  print "usage: python compile.py <source dir> <build dir>"

if __name__ == "__main__":
  try:
    globals()['source'] = 'content'
    globals()['to'] = 'build'
  except IndexError:
    printusage()
    sys.exit()
    
  try:
    traverse(source)
  except OSError:
    print "error. you sure you have the right directory?"
  except IndexError:
    print "error. please provide a directory to compile"
