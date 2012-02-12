# configuration for file generation

site_name = 'Stonelinks'
site_tag = 'The Brainchild of Lucas Doyle'

social_networks = {
'facebook' : 'https://www.facebook.com/stonelinks',
'github' : 'https://github.com/Stonelinks',
'twitter' : 'https://twitter.com/#!/Stonelinks',
'googleplus' : 'https://plus.google.com/116178490514652721625/posts',
'linkedin' : 'http://www.linkedin.com/pub/lucas-doyle/25/550/169',
'youtube' : 'http://www.youtube.com/user/RealStonelinks'
}

use_less = False

def social_small():
  s = ''
  for k, v in social_networks.iteritems():
    s += '<a href ="' + v + '" >'
    s += '<img style="position: relative; top: 4px;" src="{{wr}}static/img/icons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
  return s

def social_large():
  s = '<div class="span8" style="text-align: center;"><table>'
  for k, v in social_networks.iteritems():
    s += '<tr><td>'
    s += '<a href ="' + v + '" >'
    s += '<img src="{{wr}}static/img/lgicons/' + k + '.png">'
    s += '</a>'
    s += '&nbsp;'*2
    s += '</td><td>'
    s += '<a href ="' + v + '" ><h2>' + k.capitalize().replace('plus', ' +') + '</h2></a>'
    s += '</td></tr>'
  s += '</table></div>'
  return s
