#!/usr/bin/python

import sys
import os

class Create:
  def execute(self):
    if (len(sys.argv) < 3):
      print "argv error"
      pass

    dirName = sys.argv[1]
    projectName = sys.argv[2]
    # create dir
    if not os.path.exists("./"+dirName):
      os.mkdir("./"+dirName)

    #read file
    templateFile = open("template.html", "r")
    templateContent = templateFile.read()
    templateFile.close()

    #replace content
    TITLE_STRING = "###TITLE###"
    PAGE_TITLE_STRING = "###PAGE_TITLE###"
    templateContent = templateContent.replace(TITLE_STRING, projectName)
    templateContent = templateContent.replace(PAGE_TITLE_STRING, projectName)
    
    #write file
    outputFile = open("./"+dirName+"/"+projectName+".html", "wr")
    outputFile.write(templateContent)
    outputFile.close()

    #make extra dir
    dirList=["js", "css", "images"]
    for extraDir in dirList:
      fullExtraDir = "./"+dirName+"/"+extraDir
      if not os.path.exists(fullExtraDir):
        os.mkdir(fullExtraDir)



if __name__ == "__main__":
  Create().execute()