#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     GeoLinked App to Facilitate Mappings and Processing
#
# Author:      Holly Tina Ferguson hfergus2@nd.edu
#
# Created:     06/10/2015
# Copyright:   (c) Holly Tina Ferguson 2015
# Licence:     The University of Notre Dame
#-------------------------------------------------------------------------------

# #!/usr/bin/python
import sys
import getopt
import os
from Geo_Link import Geo_Link


def main(argv, inputfile='C:/Users/Holly2012/Desktop/GeoLinked/sample_files/ifcxml/L_2Floor.ifcxml', outputpath='output.csv'):
    #C:/Users/Holly2012/Desktop/GeoLinked/sample_files/
    #C:/Users/hfergus2/Desktop/GeoLinked/sample_files/
    #C:/Users/hfergus2/Desktop/GeoLinked/sample_files/gbxml/Single_Room_GBXML.xml
        #Single_Room_GBXML.xml              #  4.61 s
        #4_Room_GBXML.xml                   #  5.36 s
        #Vet_Center_GBXML.xml               #  15.35 s
        #L_1Floor_GBXML.xml                 #  20.21 s
        #L_2Floor_GBXML.xml                 #  1 m 18.95 s
    #C:/Users/hfergus2/Desktop/GeoLinked/sample_files/ifcxml/Single_Room_IFCxml.ifcxml
        #Single_Room_IFCxml.ifcxml          #  13.91 s
        #4Room.ifcxml                       #  34.59 s
        #Vet_Center_Model.ifcxml            #  17 m 9.21 s     But IFC turns this into 300+ surfaces and is over 100,000 lines compared to gbxml 23,000+ lines and 182 Surfaces
        #L_1Floor.ifcxml                    #  40 m 11.06 s
        #L_2Floor.ifcxml                    # was at 1h24m at 3:41

    print "Main Started"

    # Get the input file
    #inputfile = sys.argv[0]
    #Single_Room_GBXML
    #Single_Room_IFCxml
    mypath = os.path.abspath(inputfile)
    #print "inputfile", mypath, type(inputfile).__name__

    geo_link = Geo_Link()
    geo_link.inputfile = mypath
    geo_link.run()

    #outputfile = open(outputpath) #output.csv in the main folder
    #with open(outputpath, 'r') as f:
        #Add whatever stuff
        #for line in f:
        #    outputfile.write(line)
    #outputfile.close()
    sys.stdout.write("Main Finished")

if __name__ == "__main__":
    #logging.basicConfig()
    main(sys.argv[1:])
    #main(inputfile, outputfile)




