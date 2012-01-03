def load_part(partname):
  try:
    f = open(partname + '.part.html', 'r')
    print 'Loaded part %s' % str(partname)
    return f.read()
  except IOError:
    print 'Couldn\'t find part: %s' % str(partname)
    return None
