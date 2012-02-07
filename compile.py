import os
import sys
import pages
import utils
import objects

if __name__ == "__main__":
  s = objects.site()
  s.source = 'content'
  s.to = 'build'

  print '\n'*3, "phase 1...", '\n'*3
  s.init()
  print '\n'*3, "phase 2...", '\n'*3
  s.gen_special_pages()
  print '\n'*3, "phase 3...", '\n'*3
  s.gen_pages()
