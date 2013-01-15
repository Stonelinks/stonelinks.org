import os
import sys
import pages
import utils
import objects
import buildjs


if __name__ == "__main__":
  s = objects.site()
  print '\n'*3, "phase 1...", '\n'*3
  s.gen_special_pages()
  print '\n'*3, "phase 2...", '\n'*3
  s.gen_pages()
  print '\n'*3, "phase 3...", '\n'*3
  buildjs.build_js('static/js')
