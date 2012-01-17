import os

def load(partname):
  partname += '.part.html'
  path = os.path.dirname(__file__)
  try:
    f = open(os.path.join(path, partname), 'r')
    #print 'Loaded part %s' % str(partname)
    return f.read()
  except IOError:
    print 'Couldn\'t find part: %s' % str(partname)
    return None
