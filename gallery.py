import os
import config

gallery_begin = '<ul class="thumbnails">'

gallery_end = '</ul>'

def gallery_element(picture_address):
  s = '<li class="span3">'
  s += '<a href="' + picture_address + '" rel="lightbox" class="thumbnail">'
  s += '<img src="' + picture_address + '" alt="" /></a>'
  s += '</a></li>'
  return s

def make_gallery(gallery):
  s = gallery_begin
  for file in os.listdir(os.path.join(config.gallery_root, gallery)):
    img_address = os.path.join('{{wr}}' + config.gallery_root, gallery, file)
    s += gallery_element(img_address)
  s += gallery_end
  return s
