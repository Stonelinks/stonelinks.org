# configuration for file generation

site_name = 'Stonelinks'
site_tag = 'The Brainchild of Lucas Doyle'

social_networks = {
'facebook' : 'https://www.facebook.com/stonelinks',
'github' : 'https://github.com/Stonelinks',
'twitter' : 'https://twitter.com/#!/Stonelinks',
'googleplus' : 'https://plus.google.com/116178490514652721625/posts',
'linkedin' : 'http://www.linkedin.com/pub/lucas-doyle/25/550/169',
}

def social_small():
  s = ''
  for k, v in social_networks.iteritems():
    s += '<a href ="' + v + '" >'
    s += '<img src="{{wr}}static/img/icons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
  return s


