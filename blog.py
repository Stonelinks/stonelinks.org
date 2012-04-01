import config
import time
import objects
import os

def make_blog(p):
  blog = {}
  for c in p.children:
    date = c.content[c.content.find('\n') + 1:]
    date = date[:date.find('\n')]
    c.date = date
    key = time.mktime(time.strptime(date, '%m/%d/%Y'))
    
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
    blog[key] = (c, blog_summary)
  
  blog_list = []
  for k in reversed(sorted(blog.iterkeys())):
    blog_list.append(blog[k])
    
  i = 0
  for j in range(0, len(blog_list), config.blog_entries_per_page):
    segment = blog_list[j:j + config.blog_entries_per_page]
    
    s = ''
    sidebar = '<h3>Other Posts</h3>'
    sidebar += '<ul class="nav nav-list">'

    for c, summary in segment:
      s += summary
      sidebar += '<li><a href="%s">%s</a></li>' % (c.address(), c.human_name)
    sidebar += '</ul>'
    
    for c, _ in segment:
      c.sidebar = sidebar.replace('<li><a href="%s">%s</a></li>' % (c.address(), c.human_name), \
                  '<li class="active"><a href="%s">%s</a></li>' % (c.address(), c.human_name))
    
    n = objects.page()
    n.human_name = 'Blog'
    n.name = 'index'
    if i > 0:
      n.name += str(i)
      n.human_name = 'Page ' + str(i + 1)
    i += 1
    n.level = p.level + 1
    n.path = os.path.join(p.path, 'blog')
    n.destination = os.path.join(p.destination, 'blog')
    n.omit_sidebar = False
    n.sidebar = sidebar
    n.content = s
    p.children.append(n)
  
  full_archives = objects.page()
  full_archives.human_name = 'Full Archives'
  full_archives.name = 'archives'
  full_archives.level = p.level + 1
  full_archives.path = os.path.join(p.path, 'blog')
  full_archives.destination = os.path.join(p.destination, 'blog')
  full_archives.omit_sidebar = False
  full_archives.sidebar = '<h3>Archives</h3>'
  full_archives.sidebar += '<ul class="nav nav-list">'
  full_archives.content = '#Full Archives\n\n'
  for c, summary in blog_list:
    full_archives.content += summary
    full_archives.sidebar += '<li><a href="%s">%s</a></li>' % (c.address(), c.human_name)
  full_archives.sidebar += '</ul>'
  p.children.append(full_archives)



