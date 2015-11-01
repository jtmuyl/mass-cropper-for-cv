__author__ = 'jt'

import numpy as np
import cv2
from matplotlib import pyplot as plt
from utils import *
from optparse import OptionParser
import json
from clickandcrop import *
import os


def main():
    #python massCropperForCV.py -i testdata/ -o testOutput/ -j testdata.json -p testPref
    op = OptionParser()
    op.add_option("--input-folder","-i",dest="input",help="input folder",default=".")
    op.add_option("--output-folder","-o",dest="output",help="output folder",default=".")
    op.add_option("--jsonfile","-j",dest="jsonfilename",help="Json file. See Readme for more details",default="imageDb.json")
    op.add_option("--prefix","-p",dest="prefix",help="the prefix used for every output file. Default = 'cropped'",default="cropped")

    (options,args) = op.parse_args()
    if options.jsonfilename is None:
        print "No Json file was provided. You need to provide a Json file"
        op.print_help()
        exit(-1)

    #load json file
    with open(options.jsonfilename) as jsonfile:
        data = json.load(jsonfile)
        outData = []
    # loop on input files
    for file,values in data.iteritems():
        #check if a file was already processed or not
        if values['processed'] == "0":
            (outData,interruptSignal) = cropper(file,options.prefix,options.input,options.output,data)
            #save a temporary snapshot of the json new state
            with open(options.jsonfilename + ".temp",'w') as tempfile:
                json.dump(outData,tempfile)
            #if the user pressed the interrupt key in the last image, break from the loop, save state and quit.
            if interruptSignal:
                break

    if outData != []:
        #save new state
        with open(options.jsonfilename,'w') as outjsonfile:
            json.dump(outData,outjsonfile)
            #cleanup the temp file
        os.remove(options.jsonfilename + ".temp")
    else:
        print "Nothing to do !"






if __name__ == '__main__':
    main()