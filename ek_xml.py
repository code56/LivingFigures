hello = """ <article-categories>
         <subj-group subj-group-type="display-channel">
           <subject>Research article</subject>
         </subj-group>
         <subj-group subj-group-type="heading">
           <subject>Immunology</subject>
         </subj-group>
         <subj-group subj-group-type="heading">
           <subject>Microbiology and infectious disease</subject>
         </subj-group>
         <subj-group subj-group-type="heading">
           <subject>Microbiology and infectious disease</subject>
         </subj-group>
       </article-categories> 
"""

Hello1 = """ <article-categories>
         <subj-group subj-group-type="display-channel">
           <subject>Research article</subject>
         </subj-group>
         <subj-group subj-group-type="heading">
           <subject>Immunology</subject>
         </subj-group>
         <subj-group subj-group-type="heading">
           <subject>Microbiology and infectious disease</subject>
         </subj-group>
       </article-categories> 
"""


import xml.dom.minidom
dom = xml.dom.minidom.parseString(hello)


parser = argparse.ArgumentParser()
parser.add_argument('inputfile', nargs='?', default=argparse.SUPPRESS)             

parser.add_argument('-inputfile',  dest='inputfile', default='NO FILE SUPPLIED')

outputstring = path_anti_folder + "/" + "fasta_files" + "/" + fileWithoutExt[0]+ ".3.cluster "  #the path to create the files created after the antiSMASH output handling- creates in fasta_files                           #folder and the files are named automatically retaining their parent cluster name.
outputstring1 = path_anti_folder + "/cds_files/" + fileWithoutExt[0]+ ".3.cluster "   #save the synonymous codon usage of all sequences in the cluster in a separate "cds_file" folder  
                        # retain the name of the input antiSMASH cluster file 

for i in range(1, (len(onlyfiles)+1)):        #for all the .gbk files in the antiSMASH output files containing folder, take them one at a time
   #create the path for some of the input arguments of the antiSMASH_processing.py
    inputFilename = inputstring + '%0.3d'%i + '.gbk'                               #NC_003888.3.clusterxxx.gbk
    outputFilename = outputstring + '%0.3d'%i + '_cds.fasta'                       #NC_003888.3.clusterxxx_cds.fasta
    outputFilename2 = outputstring1 + '%0.3d'%i + 'codonFreqs.txt'                 #NC_003888.3.clusterxxxcodonFreqs.txt

path_mgb_folder = os.path.dirname(os.path.abspath(mgb_folder))    # find the path to the folder containing the MGB output files. The folder is in the current directory 

mgb_folder_path = path_mgb_folder + "/" + mgb_folder + "/"  # go to the path of the MGB output file folder, i.e. access the folder.

onlyfiles1 = [f for f in listdir(mgb_folder_path) if isfile(join(mgb_folder_path, f))] #the list that holds the number of MGB output files in the folder

inputstring_mgb = path_mgb_folder + "/" + mgb_folder + "/" + mgb_folder





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

foo = dom.getElementsByTagName("subject")
#text = handleTok(foo)

#print text
print "foo is ", foo
