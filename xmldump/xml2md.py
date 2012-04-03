"""

this is to help give me a leg up converting over what is already in stonelinks from a wordpress xml dump

"""


import string
from xml.dom import minidom


def convert(infile, outdir):
    # First we parse the XML file into a list of posts.
    # Each post is a dictionary
    
    dom = minidom.parse(infile)

    blog = [] # list that will contain all posts

    for node in dom.getElementsByTagName('item'):
      post = dict()

      post["title"] = node.getElementsByTagName('title')[0].firstChild.data
      post["date"] = node.getElementsByTagName('pubDate')[0].firstChild.data
      try:
        post["author"] = node.getElementsByTagName('dc:creator')[0].firstChild.data
      except:
        post["author"] = "batman"
      
      post["id"] = node.getElementsByTagName('wp:post_id')[0].firstChild.data
      
      if node.getElementsByTagName('content:encoded')[0].firstChild != None:
          post["text"] = node.getElementsByTagName('content:encoded')[0].firstChild.data
      else:
          post["text"] = ""
      
      # Add post to the list of all posts
      blog.append(post)
      
    
    # Then we create the directories and HTML files from the list of posts.
    
    for post in blog:
        # And finally the file itself
        title = post["title"].encode('utf-8')
        filename = outdir + '/' + format_filename(title) + '.md'
        
        # Add a meta tag to specify charset (UTF-8) in the HTML file
        
        f = open(filename, 'w')
        f.write("#" + title + "\n"*2)
        
        text = post["text"].encode('utf-8')
        
        #text = text.replace("", "<br/>\n")
        
        f.write(text)
        f.close()

if __name__ == "__main__":
  convert('stonelinks_xml_dump.xml', 'md')
