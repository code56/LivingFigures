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


  # folder = 'elife_articles_master'


  # for filename in os.listdir(folder):
  #     infilename = os.path.join(folder, filename)
  #     print "infilename", infilename
  #     if not os.path.isfile(infilename): continue

  #     base, extension = os.path.splitext(filename)
  #     infile = open(infilename, 'r')
  #     print infile
  #     outfile = open(os.path.join(folder, '{}_edit.{}'.format(base, extension)), 'w')


  # or because the elife_articles_master is in the working directory, I can simply put 
  # from elife_articles_master 

  # for i in range(1, (len(onlyfiles)+1)):        #for all the .gbk files in the antiSMASH output files containing folder, take them one at a time
  #    #create the path for some of the input arguments of the antiSMASH_processing.py
  #     inputFilename = inputstring + '%0.3d'%i + '.gbk'                               #NC_003888.3.clusterxxx.gbk
  #     outputFilename = outputstring + '%0.3d'%i + '_cds.fasta'                       #NC_003888.3.clusterxxx_cds.fasta
  #     outputFilename2 = outputstring1 + '%0.3d'%i + 'codonFreqs.txt'                 #NC_003888.3.clusterxxxcodonFreqs.txt


  # parser = argparse.ArgumentParser()
  # parser.add_argument('inputfile', nargs='?', default=argparse.SUPPRESS)             

  # parser.add_argument('-inputfile',  dest='inputfile', default='NO FILE SUPPLIED')

  # outputstring = path_anti_folder + "/" + "fasta_files" + "/" + fileWithoutExt[0]+ ".3.cluster "  #the path to create the files created after the antiSMASH output handling- creates in fasta_files                           #folder and the files are named automatically retaining their parent cluster name.
  # outputstring1 = path_anti_folder + "/cds_files/" + fileWithoutExt[0]+ ".3.cluster "   #save the synonymous codon usage of all sequences in the cluster in a separate "cds_file" folder  
  #                         # retain the name of the input antiSMASH cluster file 




  # mgb_folder_path = path_mgb_folder + "/" + mgb_folder + "/"  # go to the path of the MGB output file folder, i.e. access the folder.

  # onlyfiles1 = [f for f in listdir(mgb_folder_path) if isfile(join(mgb_folder_path, f))] #the list that holds the number of MGB output files in the folder

  # inputstring_mgb = path_mgb_folder + "/" + mgb_folder + "/" + mgb_folder

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


