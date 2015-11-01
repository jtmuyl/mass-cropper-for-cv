__author__ = 'jt'

#This small tool sets up a json file that will help keep track of the progress
#of the image creation. It takes 2 arguments : the data folder we're working from and
#the output json file.
#When used with massCropperForCV.py, the json file will keep track of what was processed
#and what was not, making it possible to resume the process hassle free.
#Tested on Linux, no guarantee it will work elsewhere but it should.

#USE : python createJson.py -i datafolder -o outputfile.json



from os import listdir
from os.path import isfile,join
from optparse import OptionParser

def main():

    op = OptionParser()
    op.add_option("--input-folder","-i",help="Input folder.",dest="input")
    op.add_option("--output-file-name","-o",dest="filename",help="Output file. Default = imageDb.json",default="imageDb.json")

    (options,args) = op.parse_args()

    if options.input is None:
        print "No data folder was provided. You need to provide a data folder"
        op.print_help()
        exit(-1)

    files = [ f for f in listdir(options.input) if isfile(join(options.input,f))]
    idNumber = 1
    outputfile = open(options.filename,'w')
    outputString = "{\n"
    #outputString = '{"files":[\n'

    for file in files:
        row = '"' + file + '"' + ':\n' + '{"id":"' + str(idNumber) + '",\n' + '"processed":"0"}\n,\n'
        #row = '"' + file + '"' + ':[\n' + '{"id":"' + str(idNumber) + '"},\n' + '{"processed":"0"}\n],\n'
        #row = '"' + file + '":{\n"id":"' + str(idNumber) + '",\n"processed":"0"\n},\n'
        outputString += row
        idNumber += 1

    outputString = outputString[:-2]
    #outputString += "]}"
    outputString +="}"
    outputfile.write(outputString)
    print "Init finished. %d files added to file %s" % (idNumber,options.filename)

if __name__ == '__main__':
    main()