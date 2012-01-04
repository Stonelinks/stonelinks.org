import parts
import config
import utils
import os

def title(title):
  return '<title>' + title + '</title>\n'

def md2wp(mdfile, htmldst):
    html = utils.mdfile2html(mdfile)
    html = page(html)
    filename = mdfile.split('/')[-1]
    filename = filename.split('.')[-2]
    filename = filename + '.html'
    f = open(os.path.join(htmldst, filename), 'w')
    f.write(html)
    f.close()

def page(html_content):
  s = parts.load('doctype')

  s += '<head>'

  s += title('hello world')
  s += parts.load('bootstrap_css')

  s += '</head>'

  s += '<body>'
  s += parts.load('pagehead')
  
  s += html_content
  
  s += parts.load('footer')
  s += '</body>'
  s += '</html>'
  
  s = pagefilter(s)
  
  return s
  
def pagefilter(s):
  s = s.replace('{{wr}}', config.webroot)
  return s
