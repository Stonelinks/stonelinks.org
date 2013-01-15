import os
import codecs
import re

try:
  from closure_linter import error_fixer
  from closure_linter import runner
  fixer = error_fixer.ErrorFixer()
  uselinter = True
except ImportError:
  uselinter = False

def linter(fname):
  print fname
  if uselinter:
    runner.Run(fname, fixer)

def write_header(filename):
  header = u'// stonelinks js library \n'
  header += u'// compiled on ' + time.ctime() + 2*u'\n'
  with codecs.open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
  text = header + text

  # get rid of any goog.provide and goog.require statements
  text = re.sub(r'goog\.provide\([\"\']\w*[\"\']\);|goog\.require\([\"\']\w*[\"\']\);', '', text)

  with codecs.open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

def recursive_file_list(root):
  r = []
  for folder, subs, files in os.walk(root):
    for filename in files:
      r.append(os.path.abspath(os.path.join(folder, filename)))
  return r

def build_js(outputdir):
  output = os.path.join(os.path.abspath(outputdir), 'app.js')
  jspath = os.path.join(os.path.dirname(__file__), 'js')

  third_party_dir = os.path.join(jspath, '3rd_party')
  third_party_files = recursive_file_list(third_party_dir)

  sources = []
  files_to_lint = []
  
  print 'running linter...'
  files = recursive_file_list('js/src')
  for fname in files + third_party_files:
    if os.path.splitext(fname)[1] == '.js':
      linter(fname)

  compilerjar = os.path.join(jspath, 'closure_compiler', 'compiler.jar')
  closureexternsfile = os.path.join(jspath,'utils','externs.js')

  # compile js to a separate file in case this script is run multiple times
  closure_base = u'java -jar {0} --externs {1} --language_in=ECMASCRIPT5_STRICT --jscomp_off=globalThis --jscomp_off=checkTypes --js {2} {3} {4} '.format(compilerjar, closureexternsfile, os.path.join(jspath, 'utils', 'dependency.js'), ' --js '.join(sorted(third_party_files)), ' --js '.join(sorted(sources)))
  closure_debug = closure_base + u'--js_output_file {0} --formatting=PRETTY_PRINT --compilation_level=WHITESPACE_ONLY'.format(output)
  
  print 'compiling js...'
  print closure_debug
  os.system(closure_debug)
  
  write_header(output)
