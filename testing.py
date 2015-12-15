import glob, os
import errno
import sys
import xml.dom.minidom






# for root,dirs,files in os.walk("elife_articles_master"):
#     for name in files:
#       if name.endswith('.xml'):
#         try:
#           with open(name) as f:
#             sys.stdout.write(f.read())
#             for line in f:
#               print line 
#         except IOError as exc:
#           if exc.errno != errno.EISDIR:
#             raise 

          # f = open(file, 'r')
          # f.readlines()
          # f.close


# os.listdir() to list all files in a directory - returns just the filenames, not the full path
# os.path module - gives tools to construct filenames as needed 

def main():


#  path_elife_articles_folder = os.path.dirname(os.path.abspath("elife_articles_master"))    
# path to the folder containing the MGB output files. The folder is in the current directory 

#read_xml = read_all_xml_files()
  
  # foo = dom.getElementsByTagName("subject")
  # text = handleTok(foo)

  # print text
  # print "foo is ", foo


# iterate (and read) all xml files in a directory 

  path = 'elife_articles_master'
  

  for infile in glob.glob(os.path.join(path, '*.xml')):
    print "current file is: " + infile
    f = open(infile, 'r')
      #read_the_file = f.readlines()
      #print read_the_file 
    dom = xml.dom.minidom.parse(f)
    foo = dom.getElementsByTagName("subject")
    text = handleTok(foo)


    print text
    print "foo is ", foo
    f.close




def getText(nodelist):
  rc = ""
  dict_cat = {}
  for node in nodelist:
    if node.nodeType == node.TEXT_NODE:
             #rc.append(node.data)
      rc = node.data 
      if not rc in dict_cat:
        dict_cat[rc] = 1
      else:
        dict_cat[rc] = +1
       #return ''.join(rc)
    print "dict of categories is", dict_cat 
    return dict_cat 


def handleTok(tokenlist):
  texts = ""
  for token in tokenlist:
    texts = getText(token.childNodes)
    print "the texts are", texts
  return texts




if __name__ == "__main__":
  main()


